import pandas as pd
import numpy as np
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# we just keep the columns that we need for the graph.
df_subsample = df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

# GDP Per Capita has a REALLY long right tail, so we want to log it for readability.
df_subsample["Log GDP Per Capita"] = np.log(
    df_subsample["GDP per capita (constant 2010 US$)"]
)

my_chart = (
    so.Plot(
        df_subsample,
        x="Log GDP Per Capita",
        y="Mortality rate, infant (per 1,000 live births)",
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and Under-5 Mortality")
).show()
my_chart
print("Done!")
