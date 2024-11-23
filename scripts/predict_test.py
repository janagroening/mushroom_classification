import requests

url = 'http://localhost:9696/predict'

mushroom = {"cap_shape": "b", 
            "cap_surface": "s", 
            "cap_color": "y", 
            "bruises": "t", 
            "odor": "a", 
            "gill_attachment": "a", 
            "gill_spacing": "c", 
            "gill_size": "b", 
            "gill_color": "y", 
            "stalk_shape": "e", 
            "stalk_root": "b", 
            "stalk_surface_above_ring": "s", 
            "stalk_surface_below_ring": "s", 
            "stalk_color_above_ring": "w", 
            "stalk_color_below_ring": "w", 
            "veil_type": "p", 
            "veil_color": "w", 
            "ring_number": "o", 
            "ring_type": "p", 
            "spore_print_color": "w", 
            "population": "s", 
            "habitat": "g"}

response = requests.post(url, json=mushroom).json()
print(response)


if response['class'] == True:
    print('The mushroom is poisonous')
else:
    print('The mushroom is edible')