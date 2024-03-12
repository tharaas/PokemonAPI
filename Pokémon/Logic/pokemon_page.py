import random
import webbrowser


class PokemonPage:
    CARDS = []
    LEN_LIST_CARDS = 0
    URL = 'https://api.pokemontcg.io/v2/cards'

    def __init__(self, api_object):
        self.my_api = api_object

    def pokemon_cards(self):
        response = self.my_api.api_get_request(self.URL)
        data = response.json()
        cards = data.get("data")

        if cards:
            for card in cards:
                card_ids = card["id"]
                self.CARDS.append(card_ids)

        self.LEN_LIST_CARDS = len(self.CARDS)

    def get_random_pokemon_card(self):
        self.pokemon_cards()
        random_card = random.randint(0, self.LEN_LIST_CARDS - 1)
        card_id = self.CARDS[random_card]
        response = self.my_api.api_get_request(f'https://api.pokemontcg.io/v2/cards/{card_id}')

        return response.json()

    def open_random_pokemon_card_url(self):
        data = self.get_random_pokemon_card()
        symbol_url = data["data"]["images"]["small"]
        webbrowser.open(symbol_url)
        return symbol_url

    def get_random_pokemon_card_text(self):
        data = self.get_random_pokemon_card()
        attacks = data["data"]["attacks"]
        attack_texts = [attack.get("text", "No description available") for attack in attacks]

        print("Attack Texts:", attack_texts)
        return attack_texts
