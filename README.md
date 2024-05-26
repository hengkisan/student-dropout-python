# Predictive Modeling and Factor Analysis on Student Dropout Using Machine Leaning Techniques

## 📚 Introduction
This study explore the application of machine learning models in predicting student dropout tendencies. Utilizing a diverse dataset encompassing academic, demographic, and socio-economic factors, the study employs machine learning algorithms to automate predictions and provide insights into the factors influencing student retention.

## 💻 Tools and Analysis
The dataset used in this study is sourced from the UC Irvine Machine Learning Repository and focuses on predicting students' dropout and academic success. It encompasses a wide array of information ranging from academic performance to socio-economic factors. Key variables include academic qualifications, curricular units, demographic details, and target labels indicating dropout, graduation, or enrollment status.

![image](https://github.com/hengkisan/student-dropout-python/assets/122197570/ae3e0e05-2863-4567-b3c5-11d797c30fd3)

Programming languages such as Python were employed for data preprocessing, exploratory data analysis (EDA), and model development. Categorical features are re-mapped into new values, resulted in lower dimensionality of the data and better interpretation ([mapping dictionary here](https://github.com/hengkisan/azure-supermarket-datawarehouse)). Machine learning libraries such as Scikit-Learn and CatBoost were utilized for implementing classification algorithms like Random Forest and CatBoost.

![image](https://github.com/hengkisan/student-dropout-python/assets/122197570/a04e215e-39b3-45a3-93b0-166ab004a993)

## 💡 Conclusion
The study concludes that Random Forest and CatBoost classifiers are effective in predicting student dropout rates. Balancing the dataset using techniques like Synthetic Minority Over-sampling Technique (SMOTE) significantly improved model accuracy and recall for dropout predictions.

![image](https://github.com/hengkisan/student-dropout-python/assets/122197570/ebf9a7e0-42a9-46ea-819d-d1d3180588d5)

Key findings include:
- Random Forest and CatBoost demonstrated comparable performance metrics, with precision values for dropout prediction ranging around 88% and recall around 78%.
- Feature importance analysis revealed that variables related to academic performance, such as curricular units and grades, significantly influenced dropout predictions.
- Interpretation using logistic regression highlighted the impact of categorical variables like financial status, gender, and parental qualifications on dropout rates.
