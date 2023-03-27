from ipywidgets import Dropdown
from IPython.display import display

def car_dropdown():
    dropdown = Dropdown(
        options=list(car_name.keys()),
        value=None,
        description='Select car:',
        disabled=False,
    )
    display(dropdown)
    return dropdown

car_dropdown.get = lambda: car_dropdown().value
