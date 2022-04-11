import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np

from modules import Encoder, LayerNorm


class MultiVAE(nn.Module):
    """
    Container module for Multi-VAE.
    Multi-VAE : Variational Autoencoder with Multinomial Likelihood
    See Variational Autoencoders for Collaborative Filtering
    https://arxiv.org/abs/1802.05814
    """
    # [200, 600, n_items]
    def __init__(self, p_dims, q_dims=None, dropout=0.5):
        super(MultiVAE, self).__init__()
        self.p_dims = p_dims
        if q_dims:
            assert q_dims[0] == p_dims[-1], "In and Out dimensions must equal to each other"
            assert q_dims[-1] == p_dims[0], "Latent dimension for p- and q- network mismatches."
            self.q_dims = q_dims
        else:
            self.q_dims = p_dims[::-1]

        # Last dimension of q- network is for mean and variance
        temp_q_dims = self.q_dims[:-1] + [self.q_dims[-1] * 2]
        # 6807 => 600 => 200
        self.q_layers = nn.ModuleList([nn.Linear(d_in, d_out) for
            d_in, d_out in zip(temp_q_dims[:-1], temp_q_dims[1:])])
        self.p_layers = nn.ModuleList([nn.Linear(d_in, d_out) for
            d_in, d_out in zip(self.p_dims[:-1], self.p_dims[1:])])
        
        self.drop = nn.Dropout(dropout)
        self.init_weights()
    
    def forward(self, input):
        mu, logvar = self.encode(input)
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar
    
    def encode(self, input):
        h = F.normalize(input)
        h = self.drop(h)
        
        for i, layer in enumerate(self.q_layers):
            h = layer(h)
            if i != len(self.q_layers) - 1:
                h = F.tanh(h)
            else:
                mu = h[:, :self.q_dims[-1]]
                logvar = h[:, self.q_dims[-1]:]
        return mu, logvar

    def reparameterize(self, mu, logvar):
        if self.training:
            std = torch.exp(0.5 * logvar)
            eps = torch.randn_like(std)
            return eps.mul(std).add_(mu)
        else:
            return mu
    
    def decode(self, z):
        h = z
        for i, layer in enumerate(self.p_layers):
            h = layer(h)
            if i != len(self.p_layers) - 1:
                h = F.tanh(h)
        return h

    def init_weights(self):
        for layer in self.q_layers:
            # Xavier Initialization for weights
            size = layer.weight.size()
            fan_out = size[0]
            fan_in = size[1]
            std = np.sqrt(2.0/(fan_in + fan_out))
            layer.weight.data.normal_(0.0, std)

            # Normal Initialization for Biases
            layer.bias.data.normal_(0.0, 0.001)
        
        for layer in self.p_layers:
            # Xavier Initialization for weights
            size = layer.weight.size()
            fan_out = size[0]
            fan_in = size[1]
            std = np.sqrt(2.0/(fan_in + fan_out))
            layer.weight.data.normal_(0.0, std)

            # Normal Initialization for Biases
            layer.bias.data.normal_(0.0, 0.001)




def loss_function_vae(recon_x, x, mu, logvar, anneal=1.0):
    BCE = -torch.mean(torch.sum(F.log_softmax(recon_x, 1) * x, -1))
    KLD = -0.5 * torch.mean(torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=1))

    return BCE + anneal * KLD

def loss_function_dae(recon_x, x):
    BCE = -torch.mean(torch.sum(F.log_softmax(recon_x, 1) * x, -1))
    return BCE

def focal_loss(recon_x, x):
    alpha, gamma = 0.25, 2
    alpha = torch.tensor([alpha, 1-alpha]).cuda()
    
    #BCE = torch.mean(torch.sum(F.log_softmax(recon_x, 1) * x, -1))
    BCE = nn.CrossEntropyLoss()(recon_x, x)
    pt = torch.exp(-BCE)
    F_loss = alpha * (1-pt)**gamma * BCE

    return F_loss.mean()



# # https://velog.io/@heaseo/Focalloss-%EC%84%A4%EB%AA%85
# def focal_loss(recon_x, x):

#     alpha, gamma = 0.25, 2
#     alpha = torch.tensor([alpha, 1-alpha]).cuda()
#     gamma = gamma

#     BCE_loss = F.binary_cross_entropy_with_logits(recon_x, x, reduction='none')
#     x = x.type(torch.long)
#     at = alpha.gather(0, x.data.view(-1))
#     pt = torch.exp(-BCE_loss)
#     F_loss = at*(1-pt)**gamma * BCE_loss

#     return F_loss.mean()

# https://github.com/h-y-e-j-i/boost-camp_image-classification/blob/master/baseline/loss.py
# RuntimeError: 0D or 1D target tensor expected, multi-target not supported
# def focal_loss(recon_x, x):

#     weight = 0.25
#     weight = torch.tensor([weight, 1-weight]).cuda()
#     gamma = 2
#     reduction = 'mean'

#     log_prob = F.log_softmax(recon_x, dim=-1)
#     prob = torch.exp(log_prob)

#     return F.nll_loss(
#         ((1 - prob) ** gamma) * log_prob,
#         x,
#         weight=weight,
#         reduction=reduction
#     )
