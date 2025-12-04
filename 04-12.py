import geopandas as gpd
import seaborn as sns
from matplotlib import pyplot as plt

df_geo = gpd.read_file("Москва_Moscow.geojson")

out = ["Троицкий административный округ", "район Кунцево", 
       "район Силино", 
       "район Старое Крюково", "район Крюково",
       "район Матушкино", "район Савелки"]

