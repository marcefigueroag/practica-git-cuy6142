# cambio secundario
import requests

while True:
    nombre = input("Ingrese el nombre de un Pokémon (o 'salir' para terminar): ").strip().lower()
    if nombre == "salir" or nombre == "quit":
        print("¡Saliendo de la consulta de Pokémon!")
        break
    
    if not nombre:
        continue

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()

        print(f"\n--- Información de {datos['name'].title()} ---")
        print(f"Nombre: {datos['name'].title()}")
        print(f"Peso: {datos['weight']} hectogramos")
        print("Habilidades:")
        for habilidad in datos["abilities"]:
            print(f" - {habilidad['ability']['name']}")
        print("-" * 35 + "\n")
    except requests.exceptions.HTTPError:
        print(f"\nError: No se encontró el Pokémon '{nombre}'. Intente de nuevo.\n")
    except Exception as e:
        print(f"\nOcurrió un error en la consulta: {e}\n")
