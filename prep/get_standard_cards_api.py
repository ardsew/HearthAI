import requests
import json
from datetime import datetime


def get_hearthstone_standard_cards():
    api_url = "https://api.hearthstonejson.com/v1/latest/enUS/cards.collectible.json"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            all_cards = response.json()
            standard_sets = [
                "CORE",
                "BATTLE_OF_THE_BANDS", 
                "TITANS",
                "WILD_WEST",
                "EVENT",
                "WHIZBANGS_WORKSHOP",
                "ISLAND_VACATION", # PERILS
                "SPACE" # A GREAT DARK BEYOND
            ]
            
            standard_cards = []
            for card in all_cards:
                if card.get('set') in standard_sets:
                    standard_cards.append(card)
            
            return standard_cards
        
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    
    except requests.RequestException as e:
        print(f"Error fetching Hearthstone cards: {e}")
        return None


def save_cards_to_file(cards, filename=None):
    if not cards:
        print("No cards to save.")
        return
    
    # If no filename provided, create one with current timestamp
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'hearthstone_standard_cards_{timestamp}.json'
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(cards, f, ensure_ascii=False, indent=4)
        print(f"Cards saved to {filename}")
    except Exception as e:
        print(f"Error saving cards to file: {e}")


def main():
    standard_cards = get_hearthstone_standard_cards()
    
    if standard_cards:
        save_cards_to_file(standard_cards)
    print('Done!!')


if __name__ == "__main__":
    main()
