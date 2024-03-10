import re
import unittest
from Infra.api_wrapper import APIWrapper
from Logic.pokemon_page import PokemonPage


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = PokemonPage(self.my_api)

    def test_random_pokemon_card_by_id(self):
        card_info = self.api_logic.get_random_pokemon_card()
        card_id = card_info["data"]["id"]
        self.assertIsNotNone(card_id, "Card not found")

    def test_random_pokemon_url_card(self):
        card_url = self.api_logic.open_random_pokemon_card_url()
        url_pattern = re.compile(r'https://images.pokemontcg.io/(?:[-\w.]|(?:%[\da-fA-F]{2}))+/(?:[-\w.]|(?:%[\da-fA-F]{2}))+.png')
        self.assertRegex(card_url, url_pattern, f"Invalid URL format: {card_url}")

    def test_random_pokemon_card(self):
        card_pokemon_text = self.api_logic.get_random_pokemon_card_text()
        self.assertIsNotNone(card_pokemon_text, "Card text not included")
