from nicegui import ui

ui.label('MapSearch').classes(
    'text-4xl font-extrabold text-center mt-6 '
    'bg-gradient-to-r from-purple-600 via-green-500 to-black-600 '
    'text-transparent bg-clip-text '
    'animate-pulse '
)

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
    if e.value is None:
        return
    center, zoom = CONTINENT_CENTERS[e.value]
    map.center = center
    map.zoom = zoom 

with ui.row().classes('justify-center items-center gap-8 mt-6'):
    map = ui.leaflet(
        center=(51.505, -0.09),
        zoom=5).classes('w-[300px] h-[300px] rounded-x1 shadow-lg')
        
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
