import random
import json
import os

WRITE_MODE = "w"
READ_MODE = "r"
DATA_FOLDER = "data"
NUMBER_OF_DRONES = 1500  # Increased from 50 to 1000

def generate_drone_data(number_of_drones=NUMBER_OF_DRONES):
    """Generate enemy counts and radiation levels for drone swarm."""
    
    enemy_counts = [random.randint(0, 8) for _ in range(number_of_drones)]
    radiation_levels = [round(random.uniform(0.5, 150.0), 2) for _ in range(number_of_drones)]
    
    return enemy_counts, radiation_levels

def calculate_expected_values(enemy_counts, radiation_levels):
    """Calculate expected sum and average for verification."""
    
    expected_sum = sum(enemy_counts)
    expected_average = sum(radiation_levels) / len(radiation_levels)
    
    return expected_sum, expected_average

def save_to_json(data, filepath):
    """Save data to JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode=WRITE_MODE) as file_handle:
        json.dump(data, file_handle, indent=2)

def load_from_json(filepath):
    """Load data from JSON file."""
    with open(filepath, mode=READ_MODE) as file_handle:
        return json.load(file_handle)

if __name__ == "__main__":
    # Generate mission data
    enemy_counts, radiation_levels = generate_drone_data()
    
    # Calculate expected values for verification
    expected_sum, expected_average = calculate_expected_values(enemy_counts, radiation_levels)
    
    # Save datasets
    save_to_json(enemy_counts, f"{DATA_FOLDER}/raw_data_bfv.json")
    save_to_json(radiation_levels, f"{DATA_FOLDER}/raw_data_ckks.json")
    
    # Save expected values for verification
    verification_data = {
        "expected_sum_bfv": expected_sum,
        "expected_average_ckks": round(expected_average, 4),
        "number_of_measurements": len(radiation_levels)
    }
    save_to_json(verification_data, f"{DATA_FOLDER}/expected_values.json")
    
    print(f"[BFV Dataset] {len(enemy_counts)} enemy counts saved")
    print(f"  Expected sum: {expected_sum}")
    print(f"\n[CKKS Dataset] {len(radiation_levels)} radiation values saved")
    print(f"  Expected average: {expected_average:.4f}")
    print(f"\n[Verification] Expected values saved to expected_values.json")