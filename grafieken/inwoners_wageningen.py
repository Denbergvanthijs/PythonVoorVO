import matplotlib.pyplot as plt  # Package om grafieken (plots) te tekenen
import seaborn as sns  # Package om geavanceerde plots te maken. Wij gebruiken hier alleen de kleuren van.

sns.set()  # Kleuren toevoegen, optioneel

x_jaartallen = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y_inwoners = [37359, 36642, 37049, 37408, 37429, 37786, 37837, 38458, 38412, 38774]
# Bron: https://opendata.cbs.nl/statline/#/CBS/nl/dataset/03759ned/table?dl=1C5E5

plt.plot(x_jaartallen, y_inwoners, label="Aantal inwoners")  # Grafiek maken met x- en y-as. label is optioneel
plt.xlim(2010, 2019)  # Grafiek afbakenen, optioneel
plt.ylim(35_000, 40_000)  # Grafiek afbakenen, optioneel

plt.title("Aantal inwoners in Wageningen in de jaren 2010-2019")
plt.xlabel("Jaren 2010-2019")
plt.ylabel("Aantal inwoners")

plt.grid(True)  # Gridlijnen tekenen, optioneel
plt.legend()  # Legenda tekenen, optioneel. Werkt alleen als label="" is ingevuld bij plt.plot()
plt.show()  # Grafiek laten zien, verplicht
