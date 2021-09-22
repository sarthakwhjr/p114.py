
import numpy as np
import pandas as pd
import plotly.express as pe
df=pd.read_csv("data.csv")
Score =df["TOEFL Score"].tolist()
Admitchances=df["Chance of Admit "].tolist()
NpScore=np.array(Score)
NpAdmitchances=np.array(Admitchances)
m,c=np.polyfit(NpScore,NpAdmitchances,1)
y=[]

for i in NpScore:
    yval=m*i+c
    y.append(yval)


graph=pe.scatter(x=NpScore,y=NpScore)
graph.update_layout(shapes=[dict(
    type="line",
    y0=min(y),
    y1=max(y),
    x0=min(NpScore),
    x1=max(NpScore)
)])
graph.show()
x=160
y=m*x+c
print(f"Chances of Admission if the Toffle Score  {x} is {y}")
