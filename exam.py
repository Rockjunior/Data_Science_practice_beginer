#Exam
import pandas as pd
import numpy as np

exam = pd.read_csv('DataScience/exams.csv')
print(exam.axes)
exam.head()
exam.tail()


#grouping
#sum
exam.groupby('gender').math_score.sum()
#mean
exam.groupby('gender').math_score.mean()
