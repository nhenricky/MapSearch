from nicegui import ui
import requests


def search_location(e):
    query = search_input.value
    if not query:
        return

    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': query,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'MapSearchApp/1.0 (your@email.com)'
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])

        map.center = (lat, lon)
        map.zoom = 10

        ui.notify(f'📍 Location found: {data[0]["display_name"]}')
    else:
        ui.notify('❌ Location not found', color='negative')

with ui.row().classes('w-full items-center justify-between px-6 mt-4 flex-wrap gap-4'):
    ui.label('MapSearch').classes(
        'text-4xl font-extrabold '
        'bg-gradient-to-r from-purple-600 via-green-500 to-black '
        'text-transparent bg-clip-text'
    )

    with ui.row().classes('items-center gap-2'):
        search_input = ui.input(
            placeholder='Search city or country...'
        ).props('outlined dense').classes('w-64')

        ui.button(icon='search', on_click=search_location).props('flat round')

ui.separator()

CONTINENT_CENTERS = {
    'North America': ((54.5260, -105.2551), 3),
    'South America': ((-8.7832, -55.4915), 3),
    'Europe': ((54.5260, 15.2551), 4),
    'Africa': ((-8.7832, 34.5085), 3), 
    'Asia': ((34.0479, 100.6197), 3),
    'Oceania': ((-22.7359, 140.0188), 4),
    'Antarctica': ((-82.8628, 135.0000), 2),
}

def move_map(e):
    continent = e.value
    if not continent or continent not in CONTINENT_CENTERS:
        return
    
    center, zoom = CONTINENT_CENTERS[continent]
    map.center = center
    map.zoom = zoom 
    
    # 'justify-center items-center gap-8 mt-6'

with ui.row().classes('w-screen max-w-none flex-col lg:flex-row justify-center items-center gap-8 mt-4'):
    map = ui.leaflet(
        center=(20, 0),
        # center=(51.505, -0.09),
        # zoom=5).classes('w-[300px] h-[300px] rounded-xl shadow-lg')
        zoom=2).classes(
            'w-[98vw] h-[65vh] '            # celular
            'md:w-[95vw] md:h-[75vh] '      # tablet
            'lg:w-[95vw] lg:h-[88vh] '      # notebook
            'xl:w-[97vw] xl:h-[92vh] '      # monitor grande
            '2xl:w-[97vw] 2xl:h-[95vh] '    # monitor gigante
            'rounded-xl shadow-2xl'
        )
                
        
    with ui.column().classes('gap-4'):
        
        ui.label('Select a Continent').classes(
            'text-lg font-semibold text-gray-800'
        )
        ui.select(
            options=list(CONTINENT_CENTERS.keys()),
            label='Continent',
            on_change=move_map
        ).classes(
            'w-56 text-base font-medium '
            'border-2 border-purple-600 '
            'rounded-lg shadow-md bg-white'
        )

ui.run()