import json
from firebase_functions import https_fn
from firebase_admin import initialize_app

# Inicializar Firebase Admin SDK
initialize_app()

# Constante para el tipo de contenido
APPLICATION_JSON = 'application/json'

@https_fn.on_request()
def get_movie_recommendations(req: https_fn.Request) -> https_fn.Response:
    """
    Firebase Function que devuelve recomendaciones de películas en formato JSON.
    Acepta POST requests con las preferencias del usuario.
    """
    
    # Configurar CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    # Manejar preflight OPTIONS request
    if req.method == 'OPTIONS':
        return https_fn.Response(status=204, headers=headers)
    
    if req.method != 'POST':
        return https_fn.Response(
            json.dumps({'error': 'Only POST method is allowed'}),
            status=405,
            headers=headers,
            mimetype=APPLICATION_JSON
        )
    
    try:
        # Obtener datos del POST request
        request_json = req.get_json(silent=True)
        user_preferences = ""
        
        if request_json and 'user_preferences' in request_json:
            user_preferences = request_json['user_preferences']
        
        # Generar recomendaciones basadas en las preferencias del usuario
        recommendations = generate_recommendations(user_preferences)
        
        # Devolver solo el array de recomendaciones
        return https_fn.Response(
            json.dumps(recommendations, ensure_ascii=False, indent=2),
            status=200,
            headers=headers,
            mimetype=APPLICATION_JSON
        )
    
    except Exception:
        return https_fn.Response(
            json.dumps([]),
            status=500,
            headers=headers,
            mimetype=APPLICATION_JSON
        )

def generate_recommendations(user_preferences: str):
    """
    Genera recomendaciones de películas basadas en las preferencias del usuario.
    Devuelve un array JSON con 3 películas.
    """
    
    # Convertir a lowercase para análisis simple
    preferences_lower = user_preferences.lower() if user_preferences else ""
    
    # Recomendaciones por defecto para casos generales
    default_recommendations = [
        {
            "title": "The Grand Budapest Hotel",
            "genre": "Comedy-Drama",
            "recommendation_reason": "Based on your interest in discovering something new, I've chosen this Wes Anderson masterpiece that combines visual artistry with whimsical storytelling. Its meticulous cinematography and charming narrative offer both entertainment and aesthetic pleasure, making it perfect for expanding your cinematic horizons."
        },
        {
            "title": "Parasite",
            "genre": "Thriller",
            "recommendation_reason": "Given your openness to recommendations, I've selected this critically acclaimed film that masterfully blends genres. Bong Joon-ho's direction creates a gripping social commentary wrapped in suspenseful storytelling, offering both intellectual engagement and thrilling entertainment."
        },
        {
            "title": "Spider-Man: Into the Spider-Verse",
            "genre": "Animation",
            "recommendation_reason": "To provide variety in your viewing experience, I've included this innovative animated film that revolutionizes the superhero genre. Its groundbreaking visual style and heartfelt coming-of-age story demonstrate how animation can tell sophisticated, emotionally resonant narratives."
        }
    ]
    
    # Recomendaciones específicas basadas en palabras clave
    if any(word in preferences_lower for word in ['tired', 'exhausted', 'don\'t know']):
        return [
            {
                "title": "Amélie",
                "genre": "Romantic Comedy",
                "recommendation_reason": "Since you mentioned feeling tired and uncertain about what you want to watch, I've assumed you'd appreciate something light yet emotionally uplifting. 'Amélie' offers a whimsical, feel-good narrative with charming visual inventiveness and gentle humor, making it a soothing choice without demanding too much emotional or cognitive energy."
            },
            {
                "title": "Lost in Translation",
                "genre": "Drama",
                "recommendation_reason": "Your current state of tiredness suggests that a slower, contemplative film might resonate. 'Lost in Translation' provides a quiet, atmospheric experience where mood and subtle emotion carry the story. Its introspective tone allows you to sink into the ambiance without the pressure of a dense plot, aligning with your need for something gentle and absorbing."
            },
            {
                "title": "Paddington 2",
                "genre": "Family/Comedy",
                "recommendation_reason": "Given your low-energy mood, I've assumed you might enjoy an uncomplicated but heartwarming film that brings instant comfort. 'Paddington 2' is universally praised for its warmth, humor, and kindness, offering a delightful, restorative watch that is both entertaining and soothing after a tiring day."
            }
        ]
    
    elif any(word in preferences_lower for word in ['angry', 'betrayed', 'left me', 'classic']):
        return [
            {
                "title": "North by Northwest",
                "genre": "Thriller",
                "recommendation_reason": "Since you enjoy classic cinema and are dealing with difficult emotions, 'North by Northwest' is an ideal choice. Hitchcock's masterpiece blends suspense, wit, and adventure, showcasing Cary Grant at his most charismatic while avoiding sentimental romance. Its brisk pacing and iconic set pieces channel tension and excitement that may help redirect your anger into pure cinematic thrill."
            },
            {
                "title": "The Night of the Hunter",
                "genre": "Film Noir",
                "recommendation_reason": "Given your current emotional state, I assumed you might connect with a darker, more unsettling classic. 'The Night of the Hunter' offers an intense, haunting narrative with striking expressionist visuals. It avoids romantic clichés and instead explores themes of betrayal and survival, which could resonate with your emotional state while immersing you in bold classic cinema."
            },
            {
                "title": "12 Angry Men",
                "genre": "Drama",
                "recommendation_reason": "Your frustration may find a cathartic outlet in '12 Angry Men.' This tightly crafted courtroom drama channels raw human conflict into gripping dialogue and moral tension. I've assumed you might find solace in watching characters wrestle with anger, prejudice, and fairness—turning personal turmoil into collective reflection on justice and truth."
            }
        ]
    
    elif any(word in preferences_lower for word in ['horror', 'scary', 'thriller']):
        return [
            {
                "title": "Hereditary",
                "genre": "Horror",
                "recommendation_reason": "Based on your interest in horror, I've selected this modern masterpiece that elevates the genre through psychological depth and artistic cinematography. Ari Aster's direction creates genuine dread through family trauma and supernatural elements, offering both scares and sophisticated filmmaking."
            },
            {
                "title": "The Wailing",
                "genre": "Horror-Mystery",
                "recommendation_reason": "Given your taste for thrilling content, this Korean horror film provides an intricate mystery wrapped in supernatural terror. Its slow-burn approach and cultural richness create a uniquely unsettling experience that rewards patient viewers with both scares and narrative complexity."
            },
            {
                "title": "Midsommar",
                "genre": "Folk Horror",
                "recommendation_reason": "To complement your horror preferences, I've chosen this daylight horror that subverts traditional genre expectations. Its beautiful yet disturbing imagery creates a unique viewing experience that lingers long after viewing, perfect for horror enthusiasts seeking something artistically ambitious."
            }
        ]
    
    elif any(word in preferences_lower for word in ['comedy', 'funny', 'laugh']):
        return [
            {
                "title": "The Grand Budapest Hotel",
                "genre": "Comedy",
                "recommendation_reason": "Based on your desire for comedy, I've selected this Wes Anderson film that combines sophisticated humor with visual artistry. Its witty dialogue and absurdist situations create consistent laughs while maintaining emotional depth, perfect for viewers who appreciate both comedy and craftsmanship."
            },
            {
                "title": "What We Do in the Shadows",
                "genre": "Comedy-Horror",
                "recommendation_reason": "Given your interest in humor, this mockumentary brilliantly parodies vampire films while creating genuine laughs through deadpan delivery and absurd situations. Its clever writing and committed performances make it ideal for comedy lovers who enjoy genre-bending humor."
            },
            {
                "title": "Hunt for the Wilderpeople",
                "genre": "Adventure-Comedy",
                "recommendation_reason": "To provide heartwarming comedy, I've chosen this New Zealand film that balances humor with genuine emotion. Its quirky characters and beautiful scenery create a feel-good experience that delivers both laughs and touching moments, perfect for viewers seeking uplifting entertainment."
            }
        ]
    
    else:
        return default_recommendations

def generate_mock_recommendations(user_preferences: str):
    """
    Genera recomendaciones simuladas basadas en las preferencias del usuario.
    En una implementación real, esto llamaría a la API de OpenAI.
    """
    
    # Convertir a lowercase para análisis simple
    preferences_lower = user_preferences.lower()
    
    # Recomendaciones por defecto para casos generales
    default_recommendations = [
        {
            "title": "The Grand Budapest Hotel",
            "genre": "Comedy-Drama",
            "recommendation_reason": "Based on your interest in discovering something new, I've chosen this Wes Anderson masterpiece that combines visual artistry with whimsical storytelling. Its meticulous cinematography and charming narrative offer both entertainment and aesthetic pleasure, making it perfect for expanding your cinematic horizons."
        },
        {
            "title": "Parasite",
            "genre": "Thriller",
            "recommendation_reason": "Given your openness to recommendations, I've selected this critically acclaimed film that masterfully blends genres. Bong Joon-ho's direction creates a gripping social commentary wrapped in suspenseful storytelling, offering both intellectual engagement and thrilling entertainment."
        },
        {
            "title": "Spider-Man: Into the Spider-Verse",
            "genre": "Animation",
            "recommendation_reason": "To provide variety in your viewing experience, I've included this innovative animated film that revolutionizes the superhero genre. Its groundbreaking visual style and heartfelt coming-of-age story demonstrate how animation can tell sophisticated, emotionally resonant narratives."
        }
    ]
    
    # Recomendaciones específicas basadas en palabras clave
    if any(word in preferences_lower for word in ['tired', 'exhausted', 'don\'t know']):
        return [
            {
                "title": "Amélie",
                "genre": "Romantic Comedy",
                "recommendation_reason": "Since you mentioned feeling tired and uncertain about what you want to watch, I've assumed you'd appreciate something light yet emotionally uplifting. 'Amélie' offers a whimsical, feel-good narrative with charming visual inventiveness and gentle humor, making it a soothing choice without demanding too much emotional or cognitive energy."
            },
            {
                "title": "Lost in Translation",
                "genre": "Drama",
                "recommendation_reason": "Your current state of tiredness suggests that a slower, contemplative film might resonate. 'Lost in Translation' provides a quiet, atmospheric experience where mood and subtle emotion carry the story. Its introspective tone allows you to sink into the ambiance without the pressure of a dense plot, aligning with your need for something gentle and absorbing."
            },
            {
                "title": "Paddington 2",
                "genre": "Family/Comedy",
                "recommendation_reason": "Given your low-energy mood, I've assumed you might enjoy an uncomplicated but heartwarming film that brings instant comfort. 'Paddington 2' is universally praised for its warmth, humor, and kindness, offering a delightful, restorative watch that is both entertaining and soothing after a tiring day."
            }
        ]
    
    elif any(word in preferences_lower for word in ['angry', 'betrayed', 'left me', 'classic']):
        return [
            {
                "title": "North by Northwest",
                "genre": "Thriller",
                "recommendation_reason": "Since you enjoy classic cinema and are dealing with difficult emotions, 'North by Northwest' is an ideal choice. Hitchcock's masterpiece blends suspense, wit, and adventure, showcasing Cary Grant at his most charismatic while avoiding sentimental romance. Its brisk pacing and iconic set pieces channel tension and excitement that may help redirect your anger into pure cinematic thrill."
            },
            {
                "title": "The Night of the Hunter",
                "genre": "Film Noir",
                "recommendation_reason": "Given your current emotional state, I assumed you might connect with a darker, more unsettling classic. 'The Night of the Hunter' offers an intense, haunting narrative with striking expressionist visuals. It avoids romantic clichés and instead explores themes of betrayal and survival, which could resonate with your emotional state while immersing you in bold classic cinema."
            },
            {
                "title": "12 Angry Men",
                "genre": "Drama",
                "recommendation_reason": "Your frustration may find a cathartic outlet in '12 Angry Men.' This tightly crafted courtroom drama channels raw human conflict into gripping dialogue and moral tension. I've assumed you might find solace in watching characters wrestle with anger, prejudice, and fairness—turning personal turmoil into collective reflection on justice and truth."
            }
        ]
    
    elif any(word in preferences_lower for word in ['horror', 'scary', 'thriller']):
        return [
            {
                "title": "Hereditary",
                "genre": "Horror",
                "recommendation_reason": "Based on your interest in horror, I've selected this modern masterpiece that elevates the genre through psychological depth and artistic cinematography. Ari Aster's direction creates genuine dread through family trauma and supernatural elements, offering both scares and sophisticated filmmaking."
            },
            {
                "title": "The Wailing",
                "genre": "Horror-Mystery",
                "recommendation_reason": "Given your taste for thrilling content, this Korean horror film provides an intricate mystery wrapped in supernatural terror. Its slow-burn approach and cultural richness create a uniquely unsettling experience that rewards patient viewers with both scares and narrative complexity."
            },
            {
                "title": "Midsommar",
                "genre": "Folk Horror",
                "recommendation_reason": "To complement your horror preferences, I've chosen this daylight horror that subverts traditional genre expectations. Its beautiful yet disturbing imagery creates a unique viewing experience that lingers long after viewing, perfect for horror enthusiasts seeking something artistically ambitious."
            }
        ]
    
    elif any(word in preferences_lower for word in ['comedy', 'funny', 'laugh']):
        return [
            {
                "title": "The Grand Budapest Hotel",
                "genre": "Comedy",
                "recommendation_reason": "Based on your desire for comedy, I've selected this Wes Anderson film that combines sophisticated humor with visual artistry. Its witty dialogue and absurdist situations create consistent laughs while maintaining emotional depth, perfect for viewers who appreciate both comedy and craftsmanship."
            },
            {
                "title": "What We Do in the Shadows",
                "genre": "Comedy-Horror",
                "recommendation_reason": "Given your interest in humor, this mockumentary brilliantly parodies vampire films while creating genuine laughs through deadpan delivery and absurd situations. Its clever writing and committed performances make it ideal for comedy lovers who enjoy genre-bending humor."
            },
            {
                "title": "Hunt for the Wilderpeople",
                "genre": "Adventure-Comedy",
                "recommendation_reason": "To provide heartwarming comedy, I've chosen this New Zealand film that balances humor with genuine emotion. Its quirky characters and beautiful scenery create a feel-good experience that delivers both laughs and touching moments, perfect for viewers seeking uplifting entertainment."
            }
        ]
    
    else:
        return default_recommendations