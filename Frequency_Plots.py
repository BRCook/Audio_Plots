import numpy as np
import pandas as pd
import pprint
import seaborn as sns
import matplotlib

matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

hp_logo = plt.imread("Images/HPP.png")

sd8_from_sd8, sd8_from_wc, sd8_from_x32 = (
    pd.read_csv(
        "REW_Data/SD8 into SD8 -7 0.5.txt", names=["Frequency", "Gain", "Phase"]
    ),
    pd.read_csv(
        "REW_Data/WC into SD8 -7 0.5.txt", names=["Frequency", "Gain", "Phase"]
    ),
    pd.read_csv(
        "REW_Data/X32 into SD8 -7 0.5.txt", names=["Frequency", "Gain", "Phase"]
    ),
)
sd8_from_sd8["Output device"] = "SD8"
sd8_from_wc["Output device"] = "Wing Compact"
sd8_from_x32["Output device"] = "x32"

def combine_dataframes(df_list):
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df = combined_df[(combined_df["Frequency"] >= 20) & (combined_df["Frequency"] <= 20000)]
    return combined_df

plot_instructions_FR = [
    {
        "title": "Wing Compact input frequency response by output device\n-32 dBu input and 45 dB gain",
        "path": "Input FR by output",
        "filename": "WC_frequency_-32in_45gain",
        "files": [
            "WC into WC -52 45", "X32 into WC -52 45", "SD8 into WC -52 45"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "X32 Compact input frequency response by output device\n-32 dBu input and 45.5 dB gain",
        "path": "Input FR by output",
        "filename": "X32_frequency_-32in_45gain",
        "files": [
            "WC into X32 -52 45.5", "X32 into X32 -52 45.5", "SD8 into X32 -52 45.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "SD8 input frequency response by output device\n-32 dBu input and 45.5 dB gain",
        "path": "Input FR by output",
        "filename": "SD8_frequency_-32in_45gain",
        "files": [
            "WC into SD8 -52 45.5", "X32 into SD8 -52 45.5", "SD8 into SD8 -52 45.5"
            ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
            ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "Wing Compact input frequency response by output device\n-2 dBu input and 15 dB gain",
        "path": "Input FR by output",
        "filename": "WC_frequency_-2in_0gain",
        "files": [
            "WC into WC -22 15", "X32 into WC -22 15", "SD8 into WC -22 15"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "X32 input frequency response by output device\n-2 dBu input and 15.5 dB gain",
        "path": "Input FR by output",
        "filename": "X32_frequency_-2in_0gain",
        "files": [
            "WC into X32 -22 15.5", "X32 into X32 -22 15.5", "SD8 into X32 -22 15.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "SD8 input frequency response by output device\n-2 dBu input and 15.5 dB gain",
        "path": "Input FR by output",
        "filename": "SD8_frequency_-2in_0gain",
        "files": [
            "WC into SD8 -22 15.5", "X32 into SD8 -22 15.5", "SD8 into SD8 -22 15.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "Wing Compact input frequency response by output device\n13 dBu input and 0 dB gain",
        "path": "Input FR by output",
        "filename": "WC_frequency_13in_0gain",
        "files": [
            "WC into WC -7 0", "X32 into WC -7 0", "SD8 into WC -7 0"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "X32 input frequency response by output device\n13 dBu input and 0.5 dB gain",
        "path": "Input FR by output",
        "filename": "X32_frequency_13in_0gain",
        "files": [
            "WC into X32 -7 0.5", "X32 into X32 -7 0.5", "SD8 into X32 -7 0.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "SD8 input frequency response by output device\n13 dBu input and 0.5 dB gain",
        "path": "Input FR by output",
        "filename": "SD8_frequency_13in_0gain",
        "files": [
            "WC into SD8 -7 0.5", "X32 into SD8 -7 0.5", "SD8 into SD8 -7 0.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "Wing Compact input frequency response by output device\n19 dBu input and 0 dB gain",
        "path": "Input FR by output",
        "filename": "WC_frequency_19in_0gain",
        "files": [
            "WC into WC -1 0", "X32 into WC -1 0", "SD8 into WC -1 0"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "X32 input frequency response by output device\n19 dBu input and 0.5 dB gain",
        "path": "Input FR by output",
        "filename": "X32_frequency_19in_0gain",
        "files": [
            "WC into X32 -1 0.5", "X32 into X32 -1 0.5", "SD8 into X32 -1 0.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "SD8 input frequency response by output device\n19 dBu input and 0.5 dB gain",
        "path": "Input FR by output",
        "filename": "SD8_frequency_19in_0gain",
        "files": [
            "WC into SD8 -1 0.5", "X32 into SD8 -1 0.5", "SD8 into SD8 -1 0.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "Wing Compact input frequency response by output device\n19 dBu input and 2.5 dB gain",
        "path": "Input FR by output",
        "filename": "WC_frequency_19in_3gain",
        "files": [
            "WC into WC -1 2.5", "X32 into WC -1 2.5", "SD8 into WC -1 2.5"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "X32 input frequency response by output device\n19 dBu input and 3 dB gain",
        "path": "Input FR by output",
        "filename": "X32_frequency_19in_3gain",
        "files": [
            "WC into X32 -1 3", "X32 into X32 -1 3", "SD8 into X32 -1 3"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "SD8 input frequency response by output device\n19 dBu input and 3 dB gain",
        "path": "Input FR by output",
        "filename": "SD8_frequency_19in_3gain",
        "files": [
            "WC into SD8 -1 3", "X32 into SD8 -1 3", "SD8 into SD8 -1 3"
        ],
        "add_col": "Output device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Output device"
    },
    {
        "title": "Wing Compact output frequency response by input device\n-32 dBu output and 45 dB gain",
        "path": "Output FR by input",
        "filename": "WC_output_frequency_-32out_45gain",
        "files": [
            "WC into WC -52 45", "WC into X32 -52 45.5", "WC into SD8 -52 45.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "X32 output frequency response by input device\n-32 dBu output and 45 dB gain",
        "path": "Output FR by input",
        "filename": "X32_output_frequency_-32out_45gain",
        "files": [
            "X32 into WC -52 45", "X32 into X32 -52 45.5", "X32 into SD8 -52 45.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "SD8 output frequency response by input device\n-32 dBu output and 45 dB gain",
        "path": "Output FR by input",
        "filename": "SD8_output_frequency_-32out_45gain",
        "files": [
            "SD8 into WC -52 45", "SD8 into X32 -52 45.5", "SD8 into SD8 -52 45.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact output frequency response by input device\n-2 dBu output and 15 dB gain",
        "path": "Output FR by input",
        "filename": "WC_output_frequency_-2out_15gain",
        "files": [
            "WC into WC -22 15", "WC into X32 -22 15.5", "WC into SD8 -22 15.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "X32 output frequency response by input device\n-2 dBu output and 15 dB gain",
        "path": "Output FR by input",
        "filename": "X32_output_frequency_-2out_15gain",
        "files": [
            "X32 into WC -22 15", "X32 into X32 -22 15.5", "X32 into SD8 -22 15.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "SD8 output frequency response by input device\n-2 dBu output and 15 dB gain",
        "path": "Output FR by input",
        "filename": "SD8_output_frequency_-2out_15gain",
        "files": [
            "SD8 into WC -22 15", "SD8 into X32 -22 15.5", "SD8 into SD8 -22 15.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact output frequency response by input device\n13 dBu output and 0 dB gain",
        "path": "Output FR by input",
        "filename": "WC_output_frequency_13out_0gain",
        "files": [
            "WC into WC -7 0", "WC into X32 -7 0.5", "WC into SD8 -7 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "X32 output frequency response by input device\n13 dBu output and 0 dB gain",
        "path": "Output FR by input",
        "filename": "X32_output_frequency_13out_0gain",
        "files": [
            "X32 into WC -7 0", "X32 into X32 -7 0.5", "X32 into SD8 -7 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "SD8 output frequency response by input device\n13 dBu output and 0 dB gain",
        "path": "Output FR by input",
        "filename": "SD8_output_frequency_13out_0gain",
        "files": [
            "SD8 into WC -7 0", "SD8 into X32 -7 0.5", "SD8 into SD8 -7 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact output frequency response by input device\n19 dBu output and 0 dB gain",
        "path": "Output FR by input",
        "filename": "WC_output_frequency_19out_0gain",
        "files": [
            "WC into WC -1 0", "WC into X32 -1 0.5", "WC into SD8 -1 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "X32 output frequency response by input device\n19 dBu output and 0 dB gain",
        "path": "Output FR by input",
        "filename": "X32_output_frequency_19out_0gain",
        "files": [
            "X32 into WC -1 0", "X32 into X32 -1 0.5", "X32 into SD8 -1 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "SD8 output frequency response by input device\n19 dBu output and 0 dB gain",
        "path": "Output FR by input",
        "filename": "SD8_output_frequency_19out_0gain",
        "files": [
            "SD8 into WC -1 0", "SD8 into X32 -1 0.5", "SD8 into SD8 -1 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact input frequency response by input level\nOutput from Wing Compact",
        "path": "Input FR by level",
        "filename": "WC_frequency_from_WC",
        "files": [
            "WC into WC -1 2.5", "WC into WC -1 0", "WC into WC -7 0", "WC into WC -22 15", "WC into WC -52 45"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 2.5 dB", "19 dBu, 0 dB", "13 dBu, 0 dB", "-2 dBu, 15 dB", "-32 dBu, 45 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "Wing Compact input frequency response by input level\nOutput from X32",
        "path": "Input FR by level",
        "filename": "WC_frequency_from_X32",
        "files": [
            "X32 into WC -1 2.5", "X32 into WC -1 0", "X32 into WC -7 0", "X32 into WC -22 15", "X32 into WC -52 45"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 2.5 dB", "19 dBu, 0 dB", "13 dBu, 0 dB", "-2 dBu, 15 dB", "-32 dBu, 45 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "Wing Compact input frequency response by input level\nOutput from SD8",
        "path": "Input FR by level",
        "filename": "WC_frequency_from_SD8",
        "files": [
            "SD8 into WC -1 2.5", "SD8 into WC -1 0", "SD8 into WC -7 0", "SD8 into WC -22 15", "SD8 into WC -52 45"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 2.5 dB", "19 dBu, 0 dB", "13 dBu, 0 dB", "-2 dBu, 15 dB", "-32 dBu, 45 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "X32 input frequency response by input level\nOutput from Wing Compact",
        "path": "Input FR by level",
        "filename": "X32_frequency_from_WC",
        "files": [
            "WC into X32 -1 3", "WC into X32 -1 0.5", "WC into X32 -7 0.5", "WC into X32 -22 15.5", "WC into X32 -52 45.5"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 3 dB", "19 dBu, 0.5 dB", "13 dBu, 0.5 dB", "-2 dBu, 15.5 dB", "-32 dBu, 45.5 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "X32 input frequency response by input level\nOutput from X32",
        "path": "Input FR by level",
        "filename": "X32_frequency_from_X32",
        "files": [
            "X32 into X32 -1 3", "X32 into X32 -1 0.5", "X32 into X32 -7 0.5", "X32 into X32 -22 15.5", "X32 into X32 -52 45.5"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 3 dB", "19 dBu, 0.5 dB", "13 dBu, 0.5 dB", "-2 dBu, 15.5 dB", "-32 dBu, 45.5 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "X32 input frequency response by input level\nOutput from SD8",
        "path": "Input FR by level",
        "filename": "X32_frequency_from_SD8",
        "files": [
            "SD8 into X32 -1 3", "SD8 into X32 -1 0.5", "SD8 into X32 -7 0.5", "SD8 into X32 -22 15.5", "SD8 into X32 -52 45.5"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 3 dB", "19 dBu, 0.5 dB", "13 dBu, 0.5 dB", "-2 dBu, 15.5 dB", "-32 dBu, 45.5 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "SD8 input frequency response by input level\nOutput from Wing Compact",
        "path": "Input FR by level",
        "filename": "SD8_frequency_from_WC",
        "files": [
            "WC into SD8 -1 3", "WC into SD8 -1 0.5", "WC into SD8 -7 0.5", "WC into SD8 -22 15.5",
            "WC into SD8 -52 45.5"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 3 dB", "19 dBu, 0.5 dB", "13 dBu, 0.5 dB", "-2 dBu, 15.5 dB", "-32 dBu, 45.5 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "SD8 input frequency response by input level\nOutput from X32",
        "path": "Input FR by level",
        "filename": "SD8_frequency_from_X32",
        "files": [
            "X32 into SD8 -1 3", "X32 into SD8 -1 0.5", "X32 into SD8 -7 0.5", "X32 into SD8 -22 15.5",
            "X32 into SD8 -52 45.5"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 3 dB", "19 dBu, 0.5 dB", "13 dBu, 0.5 dB", "-2 dBu, 15.5 dB", "-32 dBu, 45.5 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "SD8 input frequency response by input level\nOutput from SD8",
        "path": "Input FR by level",
        "filename": "SD8_frequency_from_SD8",
        "files": [
            "SD8 into SD8 -1 3", "SD8 into SD8 -1 0.5", "SD8 into SD8 -7 0.5", "SD8 into SD8 -22 15.5",
            "SD8 into SD8 -52 45.5"
        ],
        "add_col": "Input level, gain",
        "add_entries": [
            "19 dBu, 3 dB", "19 dBu, 0.5 dB", "13 dBu, 0.5 dB", "-2 dBu, 15.5 dB", "-32 dBu, 45.5 dB"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input level, gain"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at -32 dBu input and 45 dB gain\nOutput from Wing Compact",
        "path": "Combined input FR by output",
        "filename": "All_frequency_-32_from_WC",
        "files": [
            "WC into WC -52 45", "WC into X32 -52 45.5", "WC into SD8 -52 45.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at -2 dBu input and 15 dB gain\nOutput from Wing Compact",
        "path": "Combined input FR by output",
        "filename": "All_frequency_-2_from_WC",
        "files": [
            "WC into WC -22 15", "WC into X32 -22 15.5", "WC into SD8 -22 15.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 13 dBu input and 0 dB gain\nOutput from Wing Compact",
        "path": "Combined input FR by output",
        "filename": "All_frequency_13_from_WC",
        "files": [
            "WC into WC -7 0", "WC into X32 -7 0.5", "WC into SD8 -7 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 19 dBu input and 0 dB gain\nOutput from Wing Compact",
        "path": "Combined input FR by output",
        "filename": "All_frequency_19_from_WC",
        "files": [
            "WC into WC -1 0", "WC into X32 -1 0.5", "WC into SD8 -1 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 19 dBu input and 3 dB gain\nOutput from Wing Compact",
        "path": "Combined input FR by output",
        "filename": "All_frequency_19-3_from_WC",
        "files": [
            "WC into WC -1 2.5", "WC into X32 -1 3", "WC into SD8 -1 3"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at -32 dBu input and 45 dB gain\nOutput from X32",
        "path": "Combined input FR by output",
        "filename": "All_frequency_-32_from_X32",
        "files": [
            "X32 into WC -52 45", "X32 into X32 -52 45.5", "X32 into SD8 -52 45.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at -2 dBu input and 15 dB gain\nOutput from X32",
        "path": "Combined input FR by output",
        "filename": "All_frequency_-2_from_X32",
        "files": [
            "X32 into WC -22 15", "X32 into X32 -22 15.5", "X32 into SD8 -22 15.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 13 dBu input and 0 dB gain\nOutput from X32",
        "path": "Combined input FR by output",
        "filename": "All_frequency_13_from_X32",
        "files": [
            "X32 into WC -7 0", "X32 into X32 -7 0.5", "X32 into SD8 -7 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 19 dBu input and 0 dB gain\nOutput from X32",
        "path": "Combined input FR by output",
        "filename": "All_frequency_19_from_X32",
        "files": [
            "X32 into WC -1 0", "X32 into X32 -1 0.5", "X32 into SD8 -1 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 19 dBu input and 3 dB gain\nOutput from X32",
        "path": "Combined input FR by output",
        "filename": "All_frequency_19-3_from_X32",
        "files": [
            "X32 into WC -1 2.5", "X32 into X32 -1 3", "X32 into SD8 -1 3"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at -32 dBu input and 45 dB gain\nOutput from SD8",
        "path": "Combined input FR by output",
        "filename": "All_frequency_-32_from_SD8",
        "files": [
            "SD8 into WC -52 45", "SD8 into X32 -52 45.5", "SD8 into SD8 -52 45.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at -2 dBu input and 15 dB gain\nOutput from SD8",
        "path": "Combined input FR by output",
        "filename": "All_frequency_-2_from_SD8",
        "files": [
            "SD8 into WC -22 15", "SD8 into X32 -22 15.5", "SD8 into SD8 -22 15.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 13 dBu input and 0 dB gain\nOutput from SD8",
        "path": "Combined input FR by output",
        "filename": "All_frequency_13_from_SD8",
        "files": [
            "SD8 into WC -7 0", "SD8 into X32 -7 0.5", "SD8 into SD8 -7 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 19 dBu input and 0 dB gain\nOutput from SD8",
        "path": "Combined input FR by output",
        "filename": "All_frequency_19_from_SD8",
        "files": [
            "SD8 into WC -1 0", "SD8 into X32 -1 0.5", "SD8 into SD8 -1 0.5"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
    {
        "title": "Wing Compact, X32, SD8 input frequency responses at 19 dBu input and 3 dB gain\nOutput from SD8",
        "path": "Combined input FR by output",
        "filename": "All_frequency_19-3_from_SD8",
        "files": [
            "SD8 into WC -1 2.5", "SD8 into X32 -1 3", "SD8 into SD8 -1 3"
        ],
        "add_col": "Input device",
        "add_entries": [
            "Wing Compact", "X32", "SD8"
        ],
        "x": "Frequency",
        "y": "Gain",
        "sortby": "Input device"
    },
]

def make_plots(plot_data):
    plot_files = [f"REW_Data/{name}.txt" for name in plot_data["files"]]
    plot_dfs = [pd.read_csv(filename,  names=["Frequency", "Gain", "Phase"]) for filename in plot_files]
    if plot_data["add_col"] != "":
        for index, entry in enumerate(plot_data["add_entries"]):
            plot_dfs[index][plot_data["add_col"]] = entry

    master_df = combine_dataframes(plot_dfs)

    print(f"Working on {plot_data["title"]}")

    plot_width = 20
    plot_height = 10
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
        "legend.loc": "lower right",
        "figure.figsize": (plot_width, plot_height),
        "figure.dpi": 600,
    }
    sns.set_theme(rc=plot_style_gpt)
    sns.set_context("poster")
    freq_range = [20, 40, 60, 100, 200, 300, 400, 600, 1000, 2000, 4000, 6000, 10000, 20000]
    db_range = np.arange(2.5, -15.1, -2.5).tolist()

    frequency_plot = sns.lineplot(
        data=master_df, x=plot_data["x"], y=plot_data["y"], hue=plot_data["sortby"], palette="bright"
    )
    frequency_plot.set_title(plot_data["title"], pad=30)
    frequency_plot.set_xscale("log")
    plt.xlabel(xlabel="Frequency (Hz)", labelpad=20)
    plt.ylabel(ylabel="Gain (dBFS)", labelpad=20)
    plt.tick_params(axis="both", pad=10)

    frequency_plot.set_yticks(db_range)
    frequency_plot.set_xlim(19, 21000)
    frequency_plot.set_xticks(freq_range)
    frequency_plot.set_ylim(-17, 4)
    frequency_plot.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    plot_dpi = plt.gcf().get_dpi()

    image_width_px = hp_logo.shape[1]
    image_height_px = hp_logo.shape[0]

    xpos = (plot_width * plot_dpi - image_width_px) / 4
    ypos = (plot_height * plot_dpi - image_height_px) / 5

    plt.figimage(X=hp_logo, xo=xpos, yo=ypos, origin="upper", zorder=1, alpha=0.6)
    plt.savefig(f"Plots/{plot_data["path"]}/{plot_data["filename"]}")
    plt.clf()

for plot_set in plot_instructions_FR:
    make_plots(plot_set)