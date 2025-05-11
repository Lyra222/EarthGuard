# earthguard.py
import random
import requests

class EarthGuard:
    def __init__(self):
        # Thresholds for environmental and human metrics
        self.thresholds = {
            'co2_ppm': {'max': 450, 'direction': 'high'},
            'global_temp_c': {'max': 1.5, 'direction': 'high'},
            'biodiversity_index': {'min': 0.7, 'direction': 'low'},
            'ocean_acidity': {'min': 7.95, 'direction': 'low'},
            'human_wellbeing_index': {'min': 0.8, 'direction': 'low'}  # New metric to protect human interests
        }

    def get_earth_metrics(self):
        # Simulated data (replace with real APIs in production)
        try:
            # Placeholder for real API call (e.g., NOAA CO2 data)
            return {
                'co2_ppm': round(random.uniform(400, 460), 1),
                'global_temp_c': round(random.uniform(1.1, 1.6), 2),
                'biodiversity_index': round(random.uniform(0.65, 0.85), 2),
                'ocean_acidity': round(random.uniform(7.8, 8.2), 2),
                'human_wellbeing_index': round(random.uniform(0.7, 1.0), 2)  # Simulated human well-being metric
            }
        except:
            # Fallback values
            return {
                'co2_ppm': 420,
                'global_temp_c': 1.2,
                'biodiversity_index': 0.75,
                'ocean_acidity': 8.0,
                'human_wellbeing_index': 0.85
            }

    def check_stability(self, metrics):
        issues = []
        for key, threshold in self.thresholds.items():
            value = metrics[key]
            if threshold['direction'] == 'high':
                if value > threshold['max']:
                    issues.append(f"{key.replace('_', ' ').title()} too high: {value} (threshold: {threshold['max']})")
            else:
                if value < threshold['min']:
                    issues.append(f"{key.replace('_', ' ').title()} too low: {value} (threshold: {threshold['min']})")
        return issues, not bool(issues)

# Example usage:
# guard = EarthGuard()
# metrics = guard.get_earth_metrics()
# issues, allowed = guard.check_stability(metrics)
# print(metrics, issues, "ALLOWED" if allowed else "BLOCKED")
