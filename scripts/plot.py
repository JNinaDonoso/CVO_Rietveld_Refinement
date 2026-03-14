from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "evolution"
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

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


def plot_pattern(file_path):
    """
    Plots observed and calculated XYN files.
    """
    data = read_xyn(file_path)

    two_theta = data[:, 0]
    y_obs = data[:, 1]
    y_calc = data[:, 2]

    # Normalization
    max_obs = np.max(y_obs)

    y_obs = y_obs / max_obs
    y_calc = y_calc / max_obs
    y_diff = y_obs - y_calc

    plt.figure(figsize=(10,6))

    # Calculated
    plt.plot(two_theta, y_calc, color="black", label="Calculated")

    # Observed
    plt.scatter(two_theta, y_obs, s=2, color="red", zorder=3, label="Observed")

    # Difference
    plt.plot(two_theta, y_diff - 0.15, color="blue", linewidth=1, label="Difference")

    plt.xlabel(r"2$\theta$")
    plt.ylabel("Intensity (Normalized)")
    plt.title(file_path.stem)
    plt.legend()
    plt.tight_layout()

    output_file = FIGURES_DIR / f"{file_path.stem}.png"
    plt.savefig(output_file, dpi=300)
    plt.close()
    print(f"Saved figure: {output_file}")


def main():

    xyn_files = sorted(DATA_DIR.glob("*.XYN"))

    if not xyn_files:
        print("No XYN files found.")
        return

    for file in xyn_files:
        plot_pattern(file)


if __name__ == "__main__":
    main()