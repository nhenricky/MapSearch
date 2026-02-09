from nicegui import ui
import requests

def search_location():
    query = search_input.value.strip()
    if not query:
        ui.notify('Digite um local', color='warning')
        return

    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': query,
        'format': 'json',
        'limit': 1
    }
    headers = {
        # OBRIGATÓRIO pelo Nominatim
        'User-Agent': 'MapSearchApp/1.0 (henrique@example.com)',
        'Accept-Language': 'pt-BR'
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        ui.notify(f'Erro na busca: {e}', color='negative')
        return

    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])

        map.center = (lat, lon)
        map.zoom = 10

        ui.notify(f'📍 {data[0]["display_name"]}')
    else:
        ui.notify('❌ Local não encontrado', color='negative')


map = ui.leaflet(center=(0, 0), zoom=2).style(
    'position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0;'
)

ui.dark_mode().enable()

with ui.card().style(
    'position: fixed; top: 16px; right: 16px; z-index: 10; width: 100%; max-width: 300px;'
):
    ui.markdown('**MapSearch**').classes('text-2xl')

    search_input = ui.input(
        placeholder='Pesquisar cidade ou país...'
    ).props('outlined dense').classes('w-full') \
     .on('keydown.enter', lambda _: search_location())

    ui.button('Search', on_click=search_location).classes('w-full mt-2')

ui.run()