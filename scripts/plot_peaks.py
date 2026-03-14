from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "evolution"
FIG_DIR = BASE_DIR / "figures" / "zoom_peaks"

FIG_DIR.mkdir(parents=True, exist_ok=True)

# final XYN file
XYN_FILE = DATA_DIR / "10_final_CVOSc.XYN"

def read_xyn(file_path):
    """
    Reads XYN files.
    """
    rows = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("!"):
                continue
            parts = line.split()
            if len(parts) < 3:
                continue
            try:
                rows.append([
                    float(parts[0]),
                    float(parts[1]),
                    float(parts[2])
                ])
            except ValueError:
                continue
    return np.array(rows)


def main():

    data = read_xyn(XYN_FILE)

    two_theta = data[:, 0]
    y_obs = data[:, 1]
    y_calc = data[:, 2]

    # normalization
    max_obs = np.max(y_obs)

    y_obs = y_obs / max_obs
    y_calc = y_calc / max_obs
    y_diff = y_obs - y_calc

    # detect peaks
    peaks, _ = find_peaks(y_obs, height=0.2, distance=50)

    # take 5 highest peaks
    peak_heights = y_obs[peaks]
    strongest = peaks[np.argsort(peak_heights)[-5:]]

    strongest = sorted(strongest)

    window = 0.4

    for i, p in enumerate(strongest):

        center = two_theta[p]

        mask = (two_theta > center - window) & (two_theta < center + window)

        plt.figure(figsize=(10,6))

        plt.plot(two_theta[mask], y_calc[mask], color="black", label="Calculated")
        plt.scatter(two_theta[mask], y_obs[mask], s=4, color="red", zorder=3, label="Observed")
        plt.plot(two_theta[mask], y_diff[mask] - 0.15, linestyle=":", color="blue", linewidth=1, label="Difference")

        plt.xlabel(r"2$\theta$")
        plt.ylabel("Intensity (Normalized)")
        plt.title(f"Peak near {center:.2f}°")
        plt.legend()
        plt.tight_layout()

        out = FIG_DIR / f"zoom_peak_near_{center:.2f}.png"

        plt.savefig(out, dpi=300)
        plt.close()

        print(f"Saved {out}")


if __name__ == "__main__":
    main()