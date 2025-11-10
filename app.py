import requests
import sys

def get_programming_joke():
    """
    Interroge JokesAPI pour une blague de programmation "safe-mode"
    et l'affiche.
    """
    url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("error", False):
            print("Erreur: L'API a retourné une erreur.", file=sys.stderr)
            return

        if data["type"] == "single":
            print("Voici une blague :\n")
            print(data["joke"])
            
        elif data["type"] == "twopart":
            print("Question :", data["setup"])
            print("Réponse :", data["delivery"])

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion ou de l'API : {e}", file=sys.stderr)

if __name__ == "__main__":
    get_programming_joke()
