<table align="center">
<tr>
<td align="center">

<img src="figures/10_final_CVOSc.png" width="400"><br>
Refined diffraction pattern

</td>
<td align="center">

<img src="figures/unit cell in perspective 1.png" width="400"><br>
Crystal structure with nearest bonds

</td>
</tr>
</table>


# Rietveld Refinement of a Calcium Vanadate (CVO) Diffraction Pattern

This repository contains the data, scripts, and figures used for a Rietveld refinement project performed with the **FullProf Suite** as part of a Solid State Physics course.

The goal of the project was to refine the crystal structure of a CVO sample starting from an experimental powder diffraction pattern and an initial crystallographic model provided in CIF format. The refinement was carried out step by step by progressively activating relevant parameters such as the scale factor, background polynomial, lattice parameters, and peak-profile parameters.

The repository also includes Python scripts used to generate quality plots of the diffraction pattern and zoomed views of the main peaks.

---

# Repository Structure

```
CVO_Rietveld_Refinement
│
├── data/
│   ├── CVOSc.CIF
│   └── CVOSc.DAT
│
├── evolution/
│   ├── *_refinement_step_CVOSc.XYN
│   └── *_refinement_step_CVOSc.PCR
│
├── figures/
│   ├── *_refinement_step_CVOSc.png
│   ├── Ca with O bonds.png
│   ├── V with O bonds.png
│   ├── atoms in unit cell.png
│   ├── unit cell in perspective 1.png
│   ├── unit cell in perspective 2.png
│   ├── unit cell upper view.png
│   └── zoom_peaks/
│       └── zoom_peak_near_*.png
│
├── refinement/
│   ├── CVOSc.out
│   ├── CVOSc.pcr
│   ├── CVOSc.prf
│   ├── CVOSc.sum
│   └── CVOSc.fst
│
├── report/
│   └── _(CVO)_Rietvelt_Refinement_with_FullProf.pdf
│
├── scripts/
│   ├── plot.py
│   └── plot_peaks.py
│
└── README.md
```

---

# Refinement Procedure

The refinement was performed using **FullProf** following a sequential strategy to ensure stability and convergence:

1. Scale factor refinement  
2. First background refinement
3. Second background refinement
4. Zero shift correction  
5. Cell parameters refinement  
6. U peak-profile parameter refinement
7. V peak-profile parameter refinement
8. W peak-profile parameter refinement
9. atomic positions correction
10. Final refinement  

The final agreement factors obtained were:

| Parameter | Value |
|-----------|-------|
| Rp | 6.61 % |
| Rwp | 8.73 % |
| Rexp | 3.22 % |
| χ² | 7.32 |

The refined lattice parameters were:

- a = 10.6754 Å  
- b = 9.2087 Å  
- c = 3.0086 Å  

---

# Generating Diffraction Plots

The Python scripts read the `.XYN` files and generate normalized diffraction plots.

### Run the main plotting script

From the repository root:

```bash
python scripts/plot.py
```

This generates normalized diffraction plots and saves them in the `figures/` directory.

### Generate zoomed views of the main peaks

```bash
python scripts/plot_peaks.py
```

This script automatically detects the strongest peaks and generates zoomed figures.

---

# Crystal Structure Visualization

The crystal structure was visualized on FullProf using the refined model. The nearest bonds were identified between:

- **V – O atoms**
- **Ca – O atoms**

---

# Requirements

The plotting scripts require the following Python packages:

- numpy  
- matplotlib  
- scipy  

Install them with:

```bash
pip install numpy matplotlib scipy
```

---

# Author

Juan Ignacio Nina 
Physics Student  
Universidad San Francisco de Quito
