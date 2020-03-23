import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

sns.set()
# Zie ook: https://stackoverflow.com/questions/10138085/python-pylab-plot-normal-distribution

# Soldaten
gem_soldaten = 183
sd_soldaten = 7
x_waarden = np.linspace(gem_soldaten - 3*sd_soldaten, gem_soldaten + 3*sd_soldaten, 100)  # Genereer 100 gelijk verdeelde waarden
y_waarden = stats.norm.pdf(x_waarden, gem_soldaten, sd_soldaten)  # y-waarde horende bij x-waarde
plt.plot(x_waarden, y_waarden, label="Lengte van soldaten")

# Mannen
gem_mannen = 180.3
sd_mannen = 7.74
waarden = np.linspace(gem_mannen - 3*sd_mannen, gem_mannen + 3*sd_mannen, 100)  # Genereer 100 gelijk verdeelde waarden
y_waarden = stats.norm.pdf(waarden, gem_soldaten, sd_soldaten)  # y-waarde horende bij x-waarde
plt.plot(x_waarden, y_waarden, label="Lengte van mannen")

# Overige opties
plt.xlim(160, 210)  # Grafiek afbakenen, optioneel
plt.ylim(bottom=0)  # Grafiek afbakenen, optioneel

plt.title("Lengte van verschillende groepen mensen")
plt.xlabel("Lengte [cm]")
plt.ylabel("Kans")

plt.grid(True)  # Gridlijnen tekenen, optioneel
plt.legend(loc="upper right")  # Legenda tekenen, optioneel. Werkt alleen als label="" is ingevuld bij plt.bar()
plt.show()  # Grafiek laten zien, verplicht
