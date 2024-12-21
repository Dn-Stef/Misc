from dataclasses import dataclass
from typing import List
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel('C:\\...\\NASAPS201224.xlsx',
                   sheet_name='main')


@dataclass
class Planet:
    name: str
    radius: float
    mass: float
    eql_temp: float
    spec_type: str
    distance: float


def df_to_planets(df: pd.DataFrame) -> List[Planet]:
    names = df['pl_name'].tolist()
    radii = df['pl_rade'].tolist()
    masses = df['pl_bmasse'].tolist()
    eql_temps = df['pl_eqt'].tolist()
    spec_types = df['st_spectype'].tolist()
    distances = df['sy_dist'].tolist()
    return [
        Planet(name=name, radius=radius, mass=mass, eql_temp=eql_temp,
               spec_type=spec_type, distance=distance) for name,
        radius, mass, eql_temp, spec_type, distance in zip(names, radii,
                                                           masses, eql_temps, spec_types, distances)
    ]


planets = df_to_planets(df)

data = {
    "Mass": [planet.mass for planet in planets],
    "Radius": [planet.radius for planet in planets],
    "Equilibrium Temperature": [planet.eql_temp for planet in planets],

}

analysis_df = pd.DataFrame(data)

corr = analysis_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Planetary Properties", fontsize=16)
plt.tight_layout()
plt.show()

radius = analysis_df['Radius'].dropna().values.reshape(-1, 1)
mass = analysis_df['Mass'].dropna().values
eql_temp = analysis_df['Equilibrium Temperature'].dropna().values.reshape(-1, 1)

model_radius = LinearRegression()
model_radius.fit(radius, mass)
predicted_mass_radius = model_radius.predict(radius)
r2_radius = model_radius.score(radius, mass)
print(f"Mass vs. Radius: Slope = {model_radius.coef_[0]}, Intercept = {model_radius.intercept_}, R^2 = {r2_radius:.2f}")

model_temp = LinearRegression()
model_temp.fit(eql_temp, mass)
predicted_mass_temp = model_temp.predict(eql_temp)
r2_temp = model_temp.score(eql_temp, mass)
print(
    f"Mass vs. Equilibrium Temperature: Slope = {model_temp.coef_[0]}, Intercept = {model_temp.intercept_}, R^2 = {r2_temp:.2f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(radius, mass, color="blue", label="Data")
axes[0].plot(radius, predicted_mass_radius, color="red", label="Fit")
axes[0].set_title("Mass vs. Radius")
axes[0].set_xlabel("Radius (Earth radius)")
axes[0].set_ylabel("Mass (Earth mass)")
axes[0].legend()

axes[1].scatter(eql_temp, mass, color="blue", label="Data")
axes[1].plot(eql_temp, predicted_mass_temp, color="red", label="Fit")
axes[1].set_title("Mass vs. Equilibrium Temperature")
axes[1].set_xlabel("Equilibrium Temperature (K)")
axes[1].set_ylabel("Mass (Earth mass)")
axes[1].legend()

plt.tight_layout()
plt.show()
