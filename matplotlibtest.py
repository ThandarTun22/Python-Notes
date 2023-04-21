
# import matplotlib.pyplot as plt

# plt.xkcd()
# years = [2020,2021,2022,2023,2024,2025]
# salaryMgMg = [300,400,500,600,800,900]
# plt.plot(years, salaryMgMg,label="MgMg's salary", color="green",marker="o", linewidth=3, markersize=10)

# salaryKoKo = [380,450,500,700,600,600]
# plt.plot(years,salaryKoKo, label="KoKo's salary", linestyle="dashed", color="#FFDCAC")

# plt.title("Salary Graph")
# plt.xlabel("Years")
# plt.ylabel("Salaries in years")
# plt.savefig("Salary.png")

# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt

# plt.xkcd()
# slice=[30,70,90,120]
# myLabel=["30","70","90","120"]
# myColor = ['black', "#FBFFD6","yellow","pink"]

# plt.pie(slice, labels=myLabel, colors=myColor)
# plt.title("My Pie chart")
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BasicStat_5May2022.csv')
# print(df.columns)
# print(type(df.Population))

singapore = df[df.Country == "Singapore"]
thailand = df[df.Country == "Thailand"]

plt.plot(singapore.Year, singapore.Population, label="Myanmar")
plt.plot(thailand.Year, thailand.Population, label="Thailand")

plt.legend()
plt.show()