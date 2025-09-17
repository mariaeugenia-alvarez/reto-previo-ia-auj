import json

import os
from dotenv import load_dotenv


def llm_call(prompt_text):
    """
    Función ficticia para interactuar con un modelo de lenguaje.
    En la práctica, esto haría una llamada real a una API.
    """
    # En un proyecto real, el código para llamar a la API se vería así:
    # from openai import OpenAI
    # client = OpenAI(api_key="TU_CLAVE_AQUI")
    # response = client.chat.completions.create(
    #   model="gpt-3.5-turbo",
    #   messages=[{"role": "user", "content": prompt_text}]
    # )
    # return response.choices[0].message.content

    # Para este ejemplo de proyecto junior, simplemente devolvemos un JSON de prueba
    # para demostrar que el prompt funciona.
    return json.dumps(
        [
            {
                "titulo": "Arrival",
                "genero": "Ciencia ficción, drama",
                "motivo_recomendacion": "Al igual que las películas de Christopher Nolan que te gustan, 'Arrival' te ofrecerá una trama de ciencia ficción compleja que se desarrolla de manera no lineal. Se centra en el poder del lenguaje y el tiempo, elementos que te harán pensar y que tienen un final sorprendente, en línea con tu gusto por los giros argumentales.",
            },
            {
                "titulo": "Primer",
                "genero": "Ciencia ficción, thriller",
                "motivo_recomendacion": "Esta película de bajo presupuesto es una de las más complejas sobre viajes en el tiempo. Si te gusta que una película te 'vuele la cabeza' y no temes a una trama que requiere atención, 'Primer' te retará y te hará reflexionar sobre cada detalle, de forma similar a los desafíos narrativos de 'Inception'.",
            },
            {
                "titulo": "Memento",
                "genero": "Thriller psicológico",
                "motivo_recomendacion": "Dirigida por Christopher Nolan, es una elección obvia. La narrativa se construye en reversa, lo que encaja perfectamente con tu gusto por los 'giros de trama sorprendentes' y las historias no lineales. Explora temas de memoria y percepción de una forma que te fascinará.",
            },
        ],
        indent=2,
    )


def recomendar_peliculas_personalizadas():
    """
    Función principal para guiar al usuario y obtener recomendaciones.
    """
    print(
        "🎬 ¡Hola! Soy tu asistente de cine. Para darte las mejores recomendaciones, necesito conocer tus gustos."
    )
    print("-" * 50)

    # 1. Recolección de datos del usuario
    generos = input(
        "1. ¿Qué géneros de películas te gustan y cuáles evitas? (ej: Me gusta la ciencia ficción, pero no el terror)\n> "
    )
    peliculas_favoritas = input(
        "2. Menciona 2-3 de tus películas, directores o actores favoritos. (ej: Inception, Christopher Nolan)\n> "
    )
    elementos_clave = input(
        "3. ¿Qué es lo que más valoras en una película? (ej: historia, giros, acción, humor, personajes)\n> "
    )
    estado_animo = input(
        "4. ¿Qué tipo de película te apetece ver en este momento? (ej: algo para pensar, algo relajante)\n> "
    )

    # 2. Construcción del prompt con los datos del usuario
    prompt_completo = f"""
    Eres un experto en cine y un curador de películas personalizadas. Tu tarea es recomendar 3 películas en formato JSON basándote en los gustos detallados que te proporciono.

    **Respuestas del usuario:**
    1. Géneros: {generos}
    2. Películas Favoritas: {peliculas_favoritas}
    3. Elementos Clave: {elementos_clave}
    4. Estado de Ánimo: {estado_animo}

    **Instrucción Final:**
    Basado en las respuestas del usuario, genera una respuesta en **formato JSON**, que contenga un array de 3 objetos, cada uno representando una película. Cada objeto debe tener los siguientes campos: `titulo` (string), `genero` (string) y `motivo_recomendacion` (string). El `motivo_recomendacion` debe explicar de forma convincente por qué la película es una buena opción para el usuario, conectándola directamente con sus respuestas anteriores. No incluyas nada más en la respuesta, solo el JSON.
    """

    # 3. Llamada al modelo de lenguaje
    print("\n🧐 Analizando tus gustos...")
    try:
        json_recomendaciones = llm_call(prompt_completo)
        recomendaciones = json.loads(json_recomendaciones)

        # 4. Presentación de resultados
        print("\n🎉 ¡Aquí están tus recomendaciones personalizadas! 🎉")
        print("-" * 50)
        for peli in recomendaciones:
            print(f"🎬 **Título:** {peli['titulo']}")
            print(f"   **Género:** {peli['genero']}")
            print(f"   **Motivo:** {peli['motivo_recomendacion']}")
            print("-" * 50)

    except json.JSONDecodeError:
        print(
            "❌ Lo siento, no pude procesar la respuesta del modelo. Por favor, intenta de nuevo."
        )
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")


# Ejecutar el script
if __name__ == "__main__":
    recomendar_peliculas_personalizadas()
