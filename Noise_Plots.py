import numpy as np
import pandas as pd
import pprint
import seaborn as sns
import matplotlib

matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

hp_logo = plt.imread("Images/HPP.png")

master_df = pd.read_csv("Noise_Data/Wing_SD8_X32.csv")
master_df["Device"] = master_df["Device"].replace("WC", "Wing Compact")

sd8_noise = master_df[master_df["Device"] == "SD8"]
wc_noise = master_df[master_df["Device"] == "Wing Compact"]
x32_noise = master_df[master_df["Device"] == "X32"]

combined_150 = master_df[master_df["Output impedance"] == 150]

plot_width = 20
plot_height = 10

# Combined EIN

plot_style = {
    "axes.edgecolor": "black",
    "figure.figsize": (plot_width, plot_height),
    "figure.dpi": 600,
}

plot_style_gpt = {
    "axes.facecolor": "#212121",
    "figure.facecolor": "#121212",
    "figure.edgecolor": "black",
    "axes.edgecolor": "gray",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": "#555555",
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "axes.labelcolor": "white",
    "axes.titlesize": 16,
    "axes.titleweight": "bold",
    "axes.labelsize": 14,
    "xtick.color": "white",
    "ytick.color": "white",
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "lines.color": "white",
    "lines.linewidth": 2,
    "font.size": 12,
    "text.color": "white",
    "legend.frameon": True,
    "legend.loc": "upper right",
    "figure.figsize": (plot_width, plot_height),
    "figure.dpi": 600,
}
sns.set_theme(rc=plot_style_gpt)
sns.set_context("poster")
combined_ein = sns.lineplot(
    data=combined_150, x="Gain", y="EIN", marker="o", hue="Device", palette="bright"
)
combined_ein.set_title("Wing Compact and SD8 EIN at 150 Ω vs input gain", pad=30)
plt.xlabel(xlabel="Input gain (dB)", labelpad=20)
plt.ylabel(ylabel="EIN (dBu-A)", labelpad=20)
combined_ein.set_xticks(range(0, 50, 5))
combined_ein.set_yticks(range(-131, -91, 3))
combined_ein.set_xlim(-1, 47)
combined_ein.set_ylim(-131, -91)
plt.tick_params(axis="both", pad=10)

plot_dpi = plt.gcf().get_dpi()

image_width_px = hp_logo.shape[1]
image_height_px = hp_logo.shape[0]

xpos = (plot_width * plot_dpi - image_width_px) / 4
ypos = (plot_height * plot_dpi - image_height_px) / 5

plt.figimage(X=hp_logo, xo=xpos, yo=ypos, origin="upper", zorder=1, alpha=0.6)
plt.savefig("Plots/EIN/Combined_EIN.png")
plt.clf()

# Wing Compact EIN

wc_ein = sns.lineplot(
    data=wc_noise,
    x="Gain",
    y="EIN",
    marker="o",
    hue="Output impedance",
    palette="bright",
)
wc_ein.set_title("Wing Compact EIN at 150 Ω, 300 Ω, 450 Ω vs input gain", pad=30)
plt.xlabel(xlabel="Input gain (dB)", labelpad=20)
plt.ylabel(ylabel="EIN (dBu-A)", labelpad=20)
wc_ein.set_xticks(range(0, 50, 5))
wc_ein.set_yticks(range(-131, -91, 3))
wc_ein.set_xlim(-1, 47)
wc_ein.set_ylim(-131, -91)
plt.tick_params(axis="both", pad=10)

wc_ein_labels = ["150 Ω", "300 Ω", "450 Ω"]
for t, l in zip(wc_ein.legend_.texts, wc_ein_labels):
    t.set_text(l)

plot_dpi = plt.gcf().get_dpi()

image_width_px = hp_logo.shape[1]
image_height_px = hp_logo.shape[0]

xpos = (plot_width * plot_dpi - image_width_px) / 4
ypos = (plot_height * plot_dpi - image_height_px) / 5

plt.figimage(X=hp_logo, xo=xpos, yo=ypos, origin="upper", zorder=1, alpha=0.6)
plt.savefig("Plots/EIN/WC_EIN.png")
plt.clf()

# SD8 EIN

sd8_ein = sns.lineplot(
    data=sd8_noise,
    x="Gain",
    y="EIN",
    marker="o",
    hue="Output impedance",
    palette="bright",
)
sd8_ein.set_title("SD8 EIN at 150 Ω, 300 Ω, 450 Ω vs input gain", pad=30)
plt.xlabel(xlabel="Input gain (dB)", labelpad=20)
plt.ylabel(ylabel="EIN (dBu-A)", labelpad=20)
sd8_ein.set_xticks(range(0, 50, 5))
sd8_ein.set_yticks(range(-131, -91, 3))
sd8_ein.set_xlim(-1, 47)
sd8_ein.set_ylim(-131, -91)
plt.tick_params(axis="both", pad=10)

sd8_ein_labels = ["150 Ω", "300 Ω", "450 Ω"]
for t, l in zip(sd8_ein.legend_.texts, sd8_ein_labels):
    t.set_text(l)

plot_dpi = plt.gcf().get_dpi()

image_width_px = hp_logo.shape[1]
image_height_px = hp_logo.shape[0]

xpos = (plot_width * plot_dpi - image_width_px) / 4
ypos = (plot_height * plot_dpi - image_height_px) / 5

plt.figimage(X=hp_logo, xo=xpos, yo=ypos, origin="upper", zorder=1, alpha=0.6)
plt.savefig("Plots/EIN/SD8_EIN.png")
plt.clf()

# X32 EIN

x32_ein = sns.lineplot(
    data=sd8_noise,
    x="Gain",
    y="EIN",
    marker="o",
    hue="Output impedance",
    palette="bright",
)
x32_ein.set_title("X32 EIN at 150 Ω, 300 Ω, 450 Ω vs input gain", pad=30)
plt.xlabel(xlabel="Input gain (dB)", labelpad=20)
plt.ylabel(ylabel="EIN (dBu-A)", labelpad=20)
x32_ein.set_xticks(range(0, 50, 5))
x32_ein.set_yticks(range(-131, -91, 3))
x32_ein.set_xlim(-1, 47)
x32_ein.set_ylim(-131, -91)
plt.tick_params(axis="both", pad=10)

x32_ein_labels = ["150 Ω", "300 Ω", "450 Ω"]
for t, l in zip(x32_ein.legend_.texts, x32_ein_labels):
    t.set_text(l)

plot_dpi = plt.gcf().get_dpi()

image_width_px = hp_logo.shape[1]
image_height_px = hp_logo.shape[0]

xpos = (plot_width * plot_dpi - image_width_px) / 4
ypos = (plot_height * plot_dpi - image_height_px) / 5

plt.figimage(X=hp_logo, xo=xpos, yo=ypos, origin="upper", zorder=1, alpha=0.6)
plt.savefig("Plots/EIN/X32_EIN.png")
plt.clf()
