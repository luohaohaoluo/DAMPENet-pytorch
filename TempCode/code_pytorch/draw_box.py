import matplotlib.pyplot as plt
import numpy as np


def draw_box_bar(data_et, data_wt, data_tc, box_labels, bar_labels, data_bar):
    # Random test data
    size = 15
    x = np.arange(len(bar_labels))  # the label locations
    width = 0.15  # the width of the bars
    multiplier = 0

    fig, ax1 = plt.subplots(nrows=2, ncols=2, figsize=(20, 13))

    # rectangular box plot
    bplot1 = ax1[0][0].boxplot(data_et,
                         vert=True,  # vertical box alignment
                         patch_artist=True)  # will be used to label x-ticks
    # ax1.set_xlabel('Three separate samples')
    ax1[0][0].set_xticklabels(box_labels, fontsize=size, weight='bold')
    ax1[0][0].set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=size, weight='bold')
    ax1[0][0].set_ylabel('Dice(ET)', fontsize=size, weight='bold')
    ax1[0][0].set_ylim(0, 1.0)

    # notch shape box plot
    bplot2 = ax1[0][1].boxplot(data_wt,
                         vert=True,  # vertical box alignment
                         patch_artist=True)  # will be used to label x-ticks
    ax1[0][1].set_ylabel('Dice(WT)', fontsize=size, weight='bold')
    ax1[0][1].set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=size, weight='bold')
    ax1[0][1].set_xticklabels(box_labels, fontsize=size, weight='bold')
    ax1[0][1].set_ylim(0, 1.0)

    bplot3 = ax1[1][0].boxplot(data_tc,
                         vert=True,  # vertical box alignment
                         patch_artist=True)  # will be used to label x-ticks
    ax1[1][0].set_ylabel('Dice(TC)', fontsize=size, weight='bold')
    ax1[1][0].set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=size, weight='bold')
    ax1[1][0].set_xticklabels(box_labels, fontsize=size, weight='bold')
    ax1[1][0].set_ylim(0, 1.0)

    # fill with colors
    # colors = ['#e484d9', '#a2e470', '#dae47d', '#02a0e4']
    colors = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2']
    for bplot in (bplot1, bplot2, bplot3):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    for i, (attribute, measurement) in enumerate(data_bar.items()):
        offset = width * multiplier
        ax1[1][1].bar(x + offset, measurement, width, label=attribute, color=colors[i], edgecolor='black')
        multiplier += 1

    ax1[1][1].set_ylabel('Dice score', fontsize=size, weight='bold')
    ax1[1][1].set_yticklabels([0, 20, 40, 60, 80, 100, 120, 140], fontsize=size, weight='bold')
    ax1[1][1].set_xticks(x + width, bar_labels, weight='bold', fontsize=size)
    ax1[1][1].legend(loc='upper right', fontsize=size, ncol=2)
    ax1[1][1].set_ylim(0, 120)

    plt.show()


if __name__ == "__main__":

    # box
    data_et = [[0.950, 0.868, 0.917, 0.945, 0.862, 0.661, 0.872, 0.877, 0.177, 0.870, 0.952, 0.915, 0.732, 0.835, 0.848, 0.920, 0.959, 0.950, 0.903, 0.784,
0.975, 0.948, 0.932, 0.832, 0.879, 0.905, 0.899, 0.812, 0.845, 0.906, 0.837, 0.781, 0.931, 0.868, 0.855, 0.920, 0.911, 0.916, 0.896, 0.616,
0.918, 0.956, 0.470, 0.735, 0.468, 0.767, 0.950, 0.915, 0.873, 0.909, 0.938, 0.938, 0.718, 0.955, 0.955, 0.000, 0.888, 0.921, 0.929, 0.787,
0.000, 0.906, 0.942, 0.532, 0.919, 0.000, 0.953, 0.911, 0.785, 0.808, 0.667, 0.753, 0.919, 0.647, 0.626, 0.799, 0.716, 0.862, 0.652, 0.856,
0.883, 0.810, 0.835, 0.829, 0.879, 0.786, 0.786, 0.795, 0.818, 0.531, 0.786, 0.959, 0.467, 0.869, 0.977, 0.954, 0.953, 0.935, 0.844, 0.911,
0.000, 0.864, 0.859, 0.908, 0.791, 0.953, 0.738, 0.000, 0.872, 0.048, 0.908, 0.896, 0.942, 0.840, 0.820, 0.964, 0.000, 0.455, 0.850, 0.920,
0.000, 0.927, 0.965, 0.942, 0.944],
               [0.950, 0.873, 0.922, 0.938, 0.813, 0.690, 0.812, 0.878, 0.464, 0.749, 0.947, 0.914, 0.692, 0.827, 0.748, 0.913, 0.937, 0.927, 0.882, 0.848,
0.932, 0.944, 0.878, 0.692, 0.838, 0.872, 0.856, 0.832, 0.858, 0.892, 0.893, 0.754, 0.925, 0.874, 0.920, 0.924, 0.918, 0.890, 0.922, 0.613,
0.913, 0.928, 0.388, 0.823, 0.582, 0.842, 0.949, 0.912, 0.907, 0.886, 0.912, 0.917, 0.648, 0.950, 0.925, 0.000, 0.923, 0.923, 0.940, 0.757,
0.184, 0.900, 0.928, 0.493, 0.889, 0.000, 0.933, 0.930, 0.634, 0.780, 0.427, 0.747, 0.901, 0.727, 0.679, 0.783, 0.686, 0.809, 0.712, 0.822,
0.856, 0.778, 0.817, 0.828, 0.838, 0.780, 0.780, 0.764, 0.748, 0.550, 0.703, 0.940, 0.026, 0.842, 0.966, 0.942, 0.937, 0.917, 0.800, 0.930,
0.000, 0.903, 0.866, 0.867, 0.784, 0.957, 0.637, 0.000, 0.806, 0.016, 0.919, 0.952, 0.911, 0.831, 0.812, 0.943, 0.000, 0.602, 0.903, 0.886,
0.000, 0.907, 0.954, 0.933, 0.960],
               [0.952, 0.890, 0.911, 0.954, 0.903, 0.795, 0.844, 0.892, 0.336, 0.908, 0.973, 0.935, 0.816, 0.850, 0.907, 0.955, 0.965, 0.967, 0.913, 0.806,
0.972, 0.960, 0.964, 0.839, 0.899, 0.944, 0.908, 0.865, 0.868, 0.937, 0.934, 0.804, 0.923, 0.889, 0.963, 0.948, 0.967, 0.942, 0.926, 0.644,
0.927, 0.948, 0.551, 0.888, 0.836, 0.897, 0.928, 0.927, 0.941, 0.931, 0.954, 0.934, 0.764, 0.966, 0.964, 0.000, 0.933, 0.930, 0.947, 0.798,
0.432, 0.909, 0.944, 0.473, 0.902, 0.000, 0.953, 0.940, 0.826, 0.815, 0.671, 0.825, 0.964, 0.807, 0.723, 0.847, 0.716, 0.862, 0.645, 0.860,
0.883, 0.818, 0.844, 0.827, 0.894, 0.846, 0.781, 0.822, 0.867, 0.957, 0.808, 0.957, 0.646, 0.854, 0.981, 0.953, 0.962, 0.937, 0.860, 0.926,
0.000, 0.919, 0.876, 0.908, 0.762, 0.927, 0.709, 0.004, 0.858, 0.020, 0.939, 0.978, 0.954, 0.783, 0.891, 0.967, 0.000, 0.644, 0.912, 0.913,
0.641, 0.902, 0.978, 0.958, 0.969],
               [0.952, 0.909, 0.932, 0.955, 0.884, 0.794, 0.861, 0.911, 0.338, 0.909, 0.973, 0.931, 0.769, 0.612, 0.889, 0.962, 0.960, 0.973, 0.917, 0.764,
0.967, 0.966, 0.969, 0.782, 0.896, 0.943, 0.880, 0.892, 0.872, 0.923, 0.939, 0.814, 0.942, 0.888, 0.959, 0.947, 0.960, 0.941, 0.919, 0.620,
0.934, 0.961, 0.485, 0.830, 0.875, 0.902, 0.946, 0.925, 0.935, 0.941, 0.925, 0.934, 0.786, 0.969, 0.957, 0.000, 0.933, 0.932, 0.943, 0.780,
0.354, 0.897, 0.951, 0.613, 0.896, 0.000, 0.964, 0.929, 0.840, 0.804, 0.661, 0.875, 0.958, 0.775, 0.739, 0.848, 0.719, 0.873, 0.630, 0.860,
0.874, 0.815, 0.848, 0.843, 0.883, 0.844, 0.788, 0.788, 0.848, 0.944, 0.819, 0.961, 0.604, 0.878, 0.976, 0.962, 0.960, 0.923, 0.862, 0.919,
0.000, 0.916, 0.869, 0.905, 0.760, 0.910, 0.649, 0.001, 0.884, 0.037, 0.931, 0.965, 0.926, 0.789, 0.808, 0.972, 0.000, 0.891, 0.916, 0.920,
0.683, 0.925, 0.971, 0.946, 0.948]]

    data_wt = [[0.951, 0.900, 0.947, 0.892, 0.940, 0.979, 0.910, 0.868, 0.532, 0.944, 0.953, 0.960, 0.852, 0.692, 0.958, 0.936, 0.980, 0.959, 0.807, 0.896,
0.973, 0.964, 0.902, 0.908, 0.951, 0.974, 0.946, 0.952, 0.919, 0.952, 0.688, 0.975, 0.960, 0.947, 0.823, 0.937, 0.961, 0.836, 0.948, 0.902,
0.959, 0.906, 0.940, 0.851, 0.676, 0.881, 0.838, 0.953, 0.923, 0.960, 0.899, 0.977, 0.966, 0.977, 0.952, 0.251, 0.848, 0.975, 0.961, 0.877,
0.722, 0.879, 0.950, 0.580, 0.943, 0.560, 0.953, 0.956, 0.949, 0.916, 0.840, 0.937, 0.912, 0.957, 0.826, 0.896, 0.902, 0.947, 0.770, 0.867,
0.919, 0.913, 0.936, 0.767, 0.917, 0.924, 0.949, 0.746, 0.957, 0.401, 0.875, 0.977, 0.470, 0.973, 0.980, 0.977, 0.962, 0.976, 0.885, 0.919,
0.814, 0.931, 0.939, 0.962, 0.774, 0.969, 0.974, 0.771, 0.945, 0.940, 0.953, 0.964, 0.975, 0.848, 0.895, 0.972, 0.782, 0.482, 0.882, 0.981,
0.000, 0.978, 0.852, 0.820, 0.970],
               [0.936, 0.885, 0.935, 0.905, 0.933, 0.977, 0.899, 0.899, 0.544, 0.900, 0.955, 0.966, 0.857, 0.715, 0.937, 0.933, 0.978, 0.963, 0.790, 0.908,
0.967, 0.961, 0.918, 0.871, 0.927, 0.977, 0.945, 0.961, 0.907, 0.950, 0.725, 0.976, 0.944, 0.955, 0.893, 0.927, 0.966, 0.736, 0.944, 0.901,
0.930, 0.900, 0.931, 0.901, 0.735, 0.932, 0.815, 0.941, 0.950, 0.963, 0.903, 0.972, 0.961, 0.974, 0.970, 0.694, 0.829, 0.977, 0.963, 0.863,
0.801, 0.915, 0.943, 0.633, 0.938, 0.000, 0.959, 0.959, 0.928, 0.909, 0.548, 0.948, 0.902, 0.963, 0.880, 0.894, 0.907, 0.943, 0.754, 0.874,
0.921, 0.875, 0.931, 0.821, 0.912, 0.915, 0.942, 0.727, 0.936, 0.192, 0.825, 0.960, 0.013, 0.972, 0.976, 0.978, 0.960, 0.972, 0.859, 0.935,
0.754, 0.940, 0.925, 0.954, 0.803, 0.962, 0.958, 0.826, 0.938, 0.909, 0.939, 0.934, 0.976, 0.807, 0.907, 0.968, 0.835, 0.594, 0.870, 0.977,
0.000, 0.974, 0.881, 0.744, 0.959],
               [0.950, 0.930, 0.955, 0.923, 0.941, 0.979, 0.929, 0.931, 0.883, 0.896, 0.962, 0.971, 0.906, 0.795, 0.966, 0.951, 0.985, 0.970, 0.806, 0.918,
0.977, 0.970, 0.944, 0.877, 0.953, 0.973, 0.956, 0.968, 0.955, 0.967, 0.786, 0.978, 0.957, 0.969, 0.932, 0.949, 0.980, 0.953, 0.951, 0.911,
0.970, 0.922, 0.983, 0.937, 0.881, 0.946, 0.883, 0.958, 0.966, 0.972, 0.928, 0.975, 0.968, 0.984, 0.978, 0.891, 0.953, 0.979, 0.967, 0.889,
0.933, 0.899, 0.967, 0.409, 0.941, 0.823, 0.960, 0.968, 0.952, 0.928, 0.812, 0.944, 0.938, 0.962, 0.936, 0.893, 0.912, 0.950, 0.800, 0.888,
0.933, 0.939, 0.940, 0.780, 0.920, 0.933, 0.950, 0.803, 0.963, 0.903, 0.921, 0.981, 0.312, 0.969, 0.987, 0.983, 0.961, 0.981, 0.936, 0.925,
0.861, 0.947, 0.947, 0.961, 0.793, 0.962, 0.979, 0.938, 0.948, 0.946, 0.959, 0.969, 0.984, 0.879, 0.938, 0.982, 0.922, 0.626, 0.945, 0.983,
0.690, 0.987, 0.865, 0.857, 0.981],
               [0.945, 0.939, 0.962, 0.953, 0.939, 0.976, 0.926, 0.936, 0.887, 0.961, 0.960, 0.968, 0.893, 0.818, 0.970, 0.953, 0.984, 0.969, 0.808, 0.924,
0.979, 0.977, 0.956, 0.911, 0.965, 0.968, 0.957, 0.944, 0.961, 0.963, 0.765, 0.981, 0.976, 0.970, 0.940, 0.957, 0.982, 0.974, 0.950, 0.925,
0.957, 0.913, 0.975, 0.910, 0.904, 0.946, 0.863, 0.961, 0.967, 0.973, 0.945, 0.979, 0.968, 0.988, 0.985, 0.950, 0.969, 0.976, 0.973, 0.891,
0.943, 0.929, 0.972, 0.527, 0.952, 0.781, 0.960, 0.971, 0.958, 0.931, 0.936, 0.959, 0.939, 0.965, 0.937, 0.891, 0.902, 0.952, 0.794, 0.906,
0.923, 0.941, 0.943, 0.736, 0.922, 0.935, 0.958, 0.776, 0.945, 0.910, 0.951, 0.983, 0.592, 0.979, 0.988, 0.986, 0.968, 0.981, 0.942, 0.948,
0.877, 0.947, 0.952, 0.963, 0.785, 0.970, 0.973, 0.929, 0.953, 0.955, 0.964, 0.973, 0.973, 0.960, 0.937, 0.985, 0.904, 0.934, 0.941, 0.984,
0.683, 0.986, 0.879, 0.868, 0.980]]

    data_tc = [[0.976, 0.902, 0.955, 0.957, 0.898, 0.928, 0.857, 0.937, 0.142, 0.877, 0.946, 0.957, 0.572, 0.930, 0.877, 0.915, 0.981, 0.974, 0.893, 0.858,
0.982, 0.958, 0.939, 0.864, 0.909, 0.960, 0.899, 0.927, 0.948, 0.928, 0.923, 0.784, 0.980, 0.960, 0.862, 0.944, 0.929, 0.946, 0.919, 0.511,
0.928, 0.955, 0.877, 0.785, 0.623, 0.894, 0.973, 0.951, 0.917, 0.918, 0.944, 0.976, 0.811, 0.941, 0.969, 0.000, 0.940, 0.923, 0.962, 0.809,
0.000, 0.917, 0.966, 0.522, 0.933, 0.000, 0.954, 0.934, 0.805, 0.861, 0.794, 0.835, 0.961, 0.825, 0.321, 0.895, 0.915, 0.776, 0.872, 0.942,
0.924, 0.922, 0.902, 0.934, 0.899, 0.612, 0.952, 0.887, 0.846, 0.504, 0.796, 0.974, 0.418, 0.917, 0.945, 0.963, 0.948, 0.980, 0.850, 0.925,
0.228, 0.906, 0.927, 0.947, 0.633, 0.938, 0.625, 0.686, 0.691, 0.748, 0.947, 0.877, 0.946, 0.684, 0.789, 0.979, 0.000, 0.455, 0.897, 0.964,
0.000, 0.974, 0.967, 0.939, 0.922],
               [0.978, 0.932, 0.958, 0.967, 0.855, 0.943, 0.804, 0.907, 0.367, 0.766, 0.948, 0.961, 0.463, 0.932, 0.628, 0.807, 0.969, 0.964, 0.760, 0.943,
0.944, 0.958, 0.915, 0.641, 0.872, 0.940, 0.856, 0.951, 0.872, 0.942, 0.956, 0.755, 0.983, 0.973, 0.938, 0.963, 0.943, 0.925, 0.943, 0.522,
0.612, 0.925, 0.873, 0.610, 0.829, 0.890, 0.972, 0.953, 0.877, 0.895, 0.915, 0.955, 0.766, 0.938, 0.938, 0.000, 0.957, 0.869, 0.978, 0.851,
0.184, 0.915, 0.941, 0.485, 0.888, 0.000, 0.928, 0.938, 0.626, 0.860, 0.503, 0.827, 0.818, 0.823, 0.219, 0.889, 0.899, 0.713, 0.829, 0.909,
0.885, 0.887, 0.887, 0.915, 0.843, 0.301, 0.910, 0.875, 0.798, 0.570, 0.694, 0.958, 0.018, 0.845, 0.882, 0.956, 0.920, 0.979, 0.840, 0.945,
0.290, 0.899, 0.916, 0.930, 0.725, 0.930, 0.827, 0.878, 0.597, 0.914, 0.961, 0.916, 0.619, 0.679, 0.776, 0.960, 0.000, 0.602, 0.959, 0.935,
0.000, 0.954, 0.956, 0.572, 0.871],
               [0.978, 0.940, 0.949, 0.978, 0.924, 0.931, 0.838, 0.950, 0.283, 0.929, 0.971, 0.976, 0.791, 0.946, 0.949, 0.964, 0.988, 0.982, 0.911, 0.919,
0.983, 0.972, 0.969, 0.872, 0.934, 0.976, 0.908, 0.957, 0.966, 0.974, 0.980, 0.783, 0.976, 0.980, 0.980, 0.989, 0.978, 0.963, 0.948, 0.536,
0.917, 0.944, 0.916, 0.939, 0.914, 0.962, 0.958, 0.961, 0.961, 0.919, 0.961, 0.974, 0.831, 0.970, 0.975, 0.000, 0.966, 0.939, 0.978, 0.911,
0.432, 0.924, 0.974, 0.413, 0.925, 0.000, 0.942, 0.961, 0.848, 0.848, 0.706, 0.846, 0.983, 0.862, 0.340, 0.926, 0.917, 0.770, 0.917, 0.945,
0.926, 0.921, 0.904, 0.942, 0.936, 0.687, 0.957, 0.886, 0.906, 0.968, 0.754, 0.972, 0.837, 0.925, 0.977, 0.985, 0.950, 0.971, 0.864, 0.945,
0.368, 0.947, 0.943, 0.962, 0.625, 0.897, 0.873, 0.919, 0.728, 0.876, 0.976, 0.978, 0.963, 0.706, 0.768, 0.979, 0.000, 0.679, 0.974, 0.956,
0.652, 0.954, 0.979, 0.956, 0.976],
               [0.975, 0.951, 0.968, 0.978, 0.908, 0.960, 0.874, 0.964, 0.337, 0.931, 0.972, 0.969, 0.711, 0.696, 0.937, 0.960, 0.981, 0.985, 0.918, 0.905,
0.974, 0.977, 0.972, 0.803, 0.933, 0.972, 0.880, 0.949, 0.968, 0.964, 0.980, 0.795, 0.985, 0.982, 0.959, 0.987, 0.978, 0.972, 0.942, 0.670,
0.931, 0.962, 0.881, 0.884, 0.950, 0.958, 0.966, 0.957, 0.973, 0.946, 0.923, 0.974, 0.853, 0.973, 0.963, 0.000, 0.968, 0.935, 0.975, 0.905,
0.354, 0.914, 0.976, 0.532, 0.922, 0.000, 0.976, 0.947, 0.855, 0.867, 0.873, 0.925, 0.980, 0.901, 0.388, 0.927, 0.921, 0.792, 0.914, 0.952,
0.914, 0.918, 0.909, 0.944, 0.930, 0.788, 0.958, 0.876, 0.882, 0.953, 0.815, 0.980, 0.799, 0.950, 0.970, 0.987, 0.963, 0.973, 0.830, 0.941,
0.592, 0.946, 0.939, 0.960, 0.581, 0.905, 0.819, 0.885, 0.786, 0.900, 0.967, 0.971, 0.915, 0.836, 0.627, 0.985, 0.000, 0.891, 0.977, 0.966,
0.706, 0.969, 0.973, 0.948, 0.951]]

    # I: baseline
    # II: baseline+RSA
    # III: baseline+MRF
    # IV: SAMRNet
    labels_box = ['(I)', '(II)', '(III)', '(IV)']

    # bar
    labels_bar = ("ET", "WT", "TC")
    data_bar = {
        'baseline': (78.82, 87.91, 82.64),
        'baseline+DA': (80.63, 90.06, 83.01),
        'baseline+MPE': (82.08, 92.05, 85.16),
        'MPEDA-Net': (82.23, 92.23, 86.68),
    }

    draw_box_bar(data_et, data_wt, data_tc, labels_box, labels_bar, data_bar)



