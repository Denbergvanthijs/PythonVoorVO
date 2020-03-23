import matplotlib.pyplot as plt  # Package om grafieken (plots) te tekenen
import seaborn as sns  # Package om geavanceerde plots te maken. Wij gebruiken hier alleen de kleuren van.

sns.set()  # Kleuren toevoegen, optioneel

x_jaartallen = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y_vrouwen = [19170, 19053, 19283, 19386, 19411, 19587, 19612, 19989, 19949, 20106]
y_mannen = [18189, 17589, 17766, 18022, 18018, 18199, 18225, 18469, 18463, 18668]
# Bron: https://opendata.cbs.nl/statline/#/CBS/nl/dataset/03759ned/table?dl=1C5E5

plt.bar(x_jaartallen, y_vrouwen, label="Aantal vrouwen", align="edge")  # Grafiek maken met x- en y-as. label is optioneel
plt.bar(x_jaartallen, y_mannen, label="Aantal mannen", align="center")  # Grafiek maken met x- en y-as. label is optioneel
# plt.ylim(17_500, 22_500)  # Grafiek afbakenen, optioneel

plt.title("Aantal inwoners in Wageningen in de jaren 2010-2019")
plt.xlabel("Jaren 2010-2019")
plt.ylabel("Aantal inwoners")

plt.grid(True)  # Gridlijnen tekenen, optioneel
plt.legend(loc="lower right")  # Legenda tekenen, optioneel. Werkt alleen als label="" is ingevuld bij plt.bar()
plt.show()  # Grafiek laten zien, verplicht
