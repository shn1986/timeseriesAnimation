# Timeseries Animation

This project visualizes population trends over time by creating an animated bar chart of the top 15 countries with the highest population for each month in the dataset. The project is organized with Python scripts for data cleaning and visualization.

---

## Project Structure

```plaintext
timeseriesAnimation/
├── cleaning.py                  # Python script for data preprocessing and monthly granularity creation
├── data/
│   ├── un-country-data.csv      # Raw population dataset from the UN
│   ├── cleaned-data.csv         # Processed data with yearly granularity
│   ├── cleaned-data-monthly.csv # Processed data with monthly granularity (output of cleaning.py)
│   ├── population_animation.py  # Python script to generate population animations
```

---

## Getting Started

### Prerequisites
- Python 3.8 or above
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`

Install dependencies:
```bash
pip install pandas numpy matplotlib
```

---

### Usage

#### 1. Data Cleaning
The `cleaning.py` script processes the raw data:
- Reads the `un-country-data.csv` file.
- Filters and cleans the data for relevant columns and countries.
- Interpolates population values to create monthly granularity.
- Outputs the cleaned dataset to `cleaned-data-monthly.csv`.

Run the cleaning script:
```bash
python cleaning.py
```

#### 2. Population Animation
The `population_animation.py` script generates an animated bar chart:
- Reads the `cleaned-data-monthly.csv` file.
- Creates an animation showing the top 15 countries with the highest population month by month.

Run the animation script:
```bash
python population_animation.py
```

---

### Output
- **Data Cleaning**: `cleaned-data-monthly.csv` is saved in the `data/` folder.
- **Visualization**: Displays an animated bar chart in a separate window.

---

## Sample Data

The dataset used in this project is sourced from the United Nations and includes:
- `ISO3_code`: Country code
- `Location`: Country name
- `Time`: Year
- `TPopulation1Jan` and `TPopulation1July`: Population figures (in thousands) for January and July.

---

## Customization

To adapt this project for other datasets:
1. Modify the `cleaning.py` script to preprocess your data.
2. Update `population_animation.py` to reflect new column names or visualization preferences.

---

## License
This project is open source and available under the [MIT License](LICENSE).

---

## Authors

- **Shahid Hassan Nasir**
