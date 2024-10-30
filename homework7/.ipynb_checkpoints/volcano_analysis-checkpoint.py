# File: volcano_analysis.py

import numpy as np

def calculate_eruption_volume(height, radius):
    """
    Calculate the volume of material erupted during a volcanic eruption.
    
    Inputs:
    height (float): Height of the eruption column in meters.
    radius (float): Radius of the base of the eruption column in meters.
    
    Outputs:
    float: The volume of erupted material in cubic meters.
    """
    volume = (1 / 3) * np.pi * radius**2 * height
    return volume

# Function to classify the eruption based on its Volcanic Explosivity Index (VEI)
def classify_eruption(vei):
    """
    Classify the volcanic eruption based on the Volcanic Explosivity Index (VEI).
    
    Inputs:
    vei (int): The Volcanic Explosivity Index of the eruption.
    
    Outputs:
    str: The classification of the eruption.
    """
    if vei == 0:
        return "Non-explosive"
    elif 1 <= vei <= 2:
        return "Small"
    elif 3 <= vei <= 4:
        return "Moderate"
    elif 5 <= vei <= 6:
        return "Large"
    else:
        return "Very Large"

# Function to analyze a list of volcanic eruptions and their VEI values
def analyze_eruptions(eruptions):
    """
    Analyze a list of volcanic eruptions and classify each one.
    
    Inputs:
    eruptions (list): A list of dictionaries, each containing 'height', 'radius', and 'vei' keys.
    
    Outputs:
    list: A list of containing the volume of erupted material and its classification.
    """
    results = []
    
    for eruption in eruptions:
        volume = calculate_eruption_volume(eruption['height'], eruption['radius'])
        classification = classify_eruption(eruption['vei'])
        results.append((volume, classification))
        
    return results

if __name__ == "__main__":
    # Multi-dimensional array representing eruptions (rows: eruptions, columns: [height, radius, vei])
    eruption_data = np.array([
        [1000, 300, 5],
        [500, 150, 3],
        [200, 50, 1]
    ])

    eruptions = []
    for row in eruption_data:
        eruptions.append({'height': row[0], 'radius': row[1], 'vei': row[2]})
    
    analysis_results = analyze_eruptions(eruptions)

    for i, (volume, classification) in enumerate(analysis_results):
        print(f"Eruption {i + 1}: Volume = {volume:.2f} cubic meters, Classification = {classification}")