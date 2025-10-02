# попытка 1
wcloud = WordCloud().generate(text_norm)
plt.imshow(wcloud)
plt.axis("off")
plt.show()

# попытка 2
fig, ax = plt.subplots(figsize = (16, 9), dpi = 300)
ax.imshow(wcloud)
ax.axis("off")

# попытка 3
wcloud = WordCloud(stopwords = stop_ru, 
                  background_color = "white",
                  width = 1600,
                  height = 900).generate(text_norm)

fig, ax = plt.subplots(figsize = (16, 9), dpi = 300)
ax.imshow(wcloud)
ax.axis("off")
fig.savefig("wordcloud.png")

# попытка 4 – с маской
wcloud = WordCloud(stopwords = stop_ru, 
                  background_color = "white",
                  mask = my_mask,
                  colormap = "magma").generate(text_norm)

fig, ax = plt.subplots(dpi = 300)
ax.imshow(wcloud)
ax.axis("off")




