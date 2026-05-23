import random

# --- Simulated "Scientific Process" ---
# This function represents a complex natural phenomenon or experiment
# whose optimal conditions are unknown to the AI. The AI's goal is to
# maximize the 'yield' by finding the best 'temperature' and 'pressure'.
def simulate_reaction_yield(temperature: float, pressure: float) -> float:
    """
    Simulates the yield of a hypothetical chemical reaction based on temperature and pressure.
    This is the 'black box' that the autonomous AI is trying to understand and optimize.
    The optimal yield is at temperature=75.0 and pressure=150.0.
    """
    # Introduce some noise to simulate real-world experimental variability
    noise = random.uniform(-0.5, 0.5)

    # A quadratic function to simulate a peak yield
    # Optimal point: temp = 75, pressure = 150
    temp_factor = -0.01 * (temperature - 75.0)**2
    pressure_factor = -0.005 * (pressure - 150.0)**2
    base_yield = 100.0 # Maximum possible yield without noise

    yield_value = base_yield + temp_factor + pressure_factor + noise
    return max(0.0, yield_value) # Yield cannot be negative

# --- Autonomous Scientific AI Agent ---
class AutonomousScientist:
    def __init__(self, initial_temp: float, initial_pressure: float, step_size: float = 5.0):
        self.current_temp = initial_temp
        self.current_pressure = initial_pressure
        self.best_temp = initial_temp
        self.best_pressure = initial_pressure
        self.best_yield = simulate_reaction_yield(initial_temp, initial_pressure)
        self.step_size = step_size
        print(f"Initial Experiment: Temp={self.current_temp:.2f}, Pressure={self.current_pressure:.2f}, Yield={self.best_yield:.2f}")

    def conduct_experiment(self, temp: float, pressure: float) -> float:
        """Simulates conducting an experiment and observing the yield."""
        yield_val = simulate_reaction_yield(temp, pressure)
        print(f"  Experiment: Temp={temp:.2f}, Pressure={pressure:.2f}, Yield={yield_val:.2f}")
        return yield_val

    def iterate_discovery(self, num_iterations: int):
        """
        The core 'autonomous discovery' loop.
        The AI iteratively designs, conducts, and analyzes experiments.
        """
        print("\n--- Autonomous Discovery Process Started ---")
        for i in range(num_iterations):
            print(f"\nIteration {i+1}: Current Best (T={self.best_temp:.2f}, P={self.best_pressure:.2f}, Y={self.best_yield:.2f})")

            # --- AI designs new experiments (explores parameter space) ---
            # It generates candidate parameters around the current best to find improvements.
            candidate_experiments = []
            for _ in range(5): # Try 5 different perturbations
                delta_temp = random.uniform(-self.step_size, self.step_size)
                delta_pressure = random.uniform(-self.step_size, self.step_size)
                new_temp = max(0.0, self.best_temp + delta_temp) # Ensure non-negative
                new_pressure = max(0.0, self.best_pressure + delta_pressure) # Ensure non-negative
                candidate_experiments.append((new_temp, new_pressure))

            # Add a random jump periodically to avoid local optima (simple exploration strategy)
            if i % 10 == 0 and i > 0:
                print("  Performing a wider exploration jump...")
                candidate_experiments.append((random.uniform(0, 150), random.uniform(0, 300)))

            best_candidate_yield = self.best_yield
            best_candidate_params = (self.best_temp, self.best_pressure)

            # --- AI conducts experiments and analyzes results ---
            # It executes each designed experiment and compares its outcome.
            for temp, pressure in candidate_experiments:
                current_yield = self.conduct_experiment(temp, pressure) # AI executes experiment
                if current_yield > best_candidate_yield:
                    best_candidate_yield = current_yield
                    best_candidate_params = (temp, pressure)

            # --- AI updates its 'understanding' and 'hypothesis' ---
            # Based on the analysis, it refines its knowledge of the optimal conditions.
            if best_candidate_yield > self.best_yield:
                self.best_yield = best_candidate_yield
                self.best_temp, self.best_pressure = best_candidate_params
                print(f"  New best found! Temp={self.best_temp:.2f}, Pressure={self.best_pressure:.2f}, Yield={self.best_yield:.2f}")
            else:
                print("  No significant improvement in this iteration. Sticking to current best.")

        print("\n--- Autonomous Discovery Process Finished ---")
        print(f"Final Optimal Conditions Found: Temperature={self.best_temp:.2f}, Pressure={self.best_pressure:.2f}")
        print(f"Maximum Yield Achieved: {self.best_yield:.2f}")

# --- Main execution ---
if __name__ == "__main__":
    # The autonomous scientist starts with some initial guess
    scientist = AutonomousScientist(initial_temp=20.0, initial_pressure=50.0, step_size=10.0)
    # The scientist then autonomously runs a series of experiments
    scientist.iterate_discovery(num_iterations=20) # Run 20 iterations of discovery
