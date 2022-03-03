from numpy import absolute, quantile
import pandas as pd



food = pd.read_csv("food.csv")
restaurant = pd.read_csv("restaurant.csv")
types=["japan","korea","china","taiwan","usa","thai","southeast"]
prefs=[]
calories = 2500
price = 400
options = "breakfast"
defalut_percentage = {"breakfast":[0.3,0.35,0.35],"lunch":[0.2,0.5,0.3],"dinner":[0.2,0.3,0.5]}
def f():
    for key in defalut_percentage:
        if key == options:
            if key == "breakfast":
                p = 0
                # b = calories*defalut_percentage[key][0]
                df_b = food[(food["food_breakfast"]=="Y") | (food["food_breakfast"]=="A")]
                # print(df_b)
                # print(len(df_b))
                df_b = df_b[df_b["calories"]>= quantile(df_b["calories"].tolist(),0.75)]
                # print(len(df_b))
                df_b_1 = df_b.sample()
                # print(df_b_1)
                remain = calories - int(df_b_1["calories"])
                # print(remain)
                s=10000
                for times in range(50):
                    df_l = food[food["food_breakfast"]!="Y"]
                    df_d = food[food["food_breakfast"]!="Y"]
                    df_l_0 = df_l.sample()
                    df_d_0 = df_d.sample()
                    t = abs(int(df_l_0["calories"])+int(df_d_0["calories"])-remain)
                    if t < s:
                        s = t
                        df_l_1 = df_l_0
                        df_d_1 = df_d_0
                
                return df_b_1,df_l_1,df_d_1
            else:
                b = calories*defalut_percentage[key][0]
                l = calories*defalut_percentage[key][1]
                d = calories*defalut_percentage[key][2]
        else:
            pass

a,b,c =f()
print(a)
print(b)
print(c)
