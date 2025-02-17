# Movie Recommendation

## ❗ 주제 설명

- 시간 순으로 정렬된 영화 시청 이력에서 중간의 일부 데이터가 누락된 상황일 때, 그 누락된 아이템들과 마지막 아이템을 예측



## 👋 팀원 소개

|[강신구](https://github.com/Kang-singu)|[김백준](https://github.com/middle-100)|[김혜지](https://github.com/h-y-e-j-i)|[이상연](https://github.com/qwedsazxc456)|[전인혁](https://github.com/inhyeokJeon)|
| :-------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: |
|  [![Avatar](https://user-images.githubusercontent.com/58590260/163955612-1e3c1752-9c68-4cb1-af8f-c99b99625750.jpg)](https://github.com/Kang-singu) |  [![Avatar](https://user-images.githubusercontent.com/58590260/163910764-69f88ef5-5d66-4cec-ab17-a53b12463c7d.jpg)](https://github.com/middle-100) | [![Avatar](https://user-images.githubusercontent.com/58590260/163910721-c067c68a-9612-4e70-a464-a4bb84eea97e.jpg)](https://github.com/h-y-e-j-i) | [![Avatar](https://user-images.githubusercontent.com/58590260/163955925-f5609908-6984-412f-8df6-ae490517ddf4.jpg)](https://github.com/qwedsazxc456) | [![Avatar](https://user-images.githubusercontent.com/58590260/163956020-891ce159-3233-469d-a83c-4c0926ec438a.jpg)](https://github.com/inhyeokJeon) |



## 🔨 Installation

- numpy==1.22.2
- pandas==1.4.1
- pytz==2021.3
- python-dateutil==2.8.2
- scipy==1.8.0
- six==1.16.0
- torch==1.10.2
- tqdm==4.62.3
- typing_extensions==4.1.1
- Python==3.8.5

```python
$ pip install -r $ROOT/level2-movie-recommendation-level2-recsys-06/requirements.txt
```

## 🏢 Structure

```bash
level2-movie-recommendation-level2-recsys-06
|-- EASE
|   |-- README.md
|   |-- models.py|   
|   `-- run_ease.py
|-- EDA
|   `-- EDA_hyeji.ipynb
|-- Ensemble
|   `-- ensemble.ipynb
|-- README.md
|-- RecVAE
|   |-- README.md
|   |-- model.py
|   |-- preprocesing.py
|   |-- run.py
|   `-- utils.py
`-- requirements.txt
```

## 🖼️ 실행 결과

| 모델명 | Recall@10 | 최종 순위 |
| --- | --- | --- |
| RecVAE + EASE 앙상블 | 0.1630 | private 6등 |


## 📜 참고자료
1. Diane Bouchacourt, Ryota Tomioka, Sebastian Nowozin, 2017. Multi-Level Variational Autoencoder: Learning Disentangled Representations from Grouped Observations
2. Dawen Liang, Rahul G. Krishnan, Matthew D. Hoffman, Tony Jebara, 2018. Variational Autoencoders for Collaborative Filtering
3. Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, Xiuqiang He, 2017. DeepFM: A Factorization-Machine based Neural Network for CTR Prediction
4. Wang-Cheng Kang, Julian McAuley, 2018. Self-Attentive Sequential Recommendation
5. Fei Sun, Jun Liu, Jian Wu, Changhua Pei, Xiao Lin, Wenwu Ou, and Peng Jiang, 2019. BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer
6. Ilya Shenbin, Anton Alekseev, Elena Tutubalina, Valentin Malykh, Sergey I. Nikolenko, 2019. RecVAE: a New Variational Autoencoder for Top-N Recommendations with Implicit Feedback
7. Harald Steck. 2019. Embarrassingly Shallow Autoencoders for Sparse Data
8. Daeryong Kim, Bongwon Suh, 2019. Enhancing VAEs for Collaborative Filtering: Flexible Priors & Gating Mechanisms
9. Pavel Kordik, Vojtech Vancura, 2021. Deep Variational Autoencoder with Shallow Parallel Path for Top-N Recommendation (VASP)

 
