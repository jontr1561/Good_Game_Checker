import requests
import datetime


api_key = # your api
base_url = "https://api.balldontlie.io/v1"
headers = {"Authorization": #your api}

url = f"{base_url}/games"


# function to get today's date
def today_date():
    """This function gets today's date and turns it into a string"""
    today = datetime.date.today()
    str_today = str(today)
    return str_today


team_dict = {
    1: "Atlanta Hawks",
    2: "Boston Celtics",
    3: "Brooklyn Nets",
    4: "Charlotte Hornets",
    5: "Chicago Bulls",
    6: "Cleveland Cavaliers",
    7: "Dallas Mavericks",
    8: "Denver Nuggets",
    9: "Detroit Pistons",
    10: "Golden State Warriors",
    11: "Houston Rockets",
    12: "Indiana Pacers",
    13: "LA Clippers",
    14: "Los Angeles Lakers",
    15: "Memphis Grizzlies",
    16: "Miami Heat",
    17: "Milwaukee Bucks",
    18: "Minnesota Timberwolves",
    19: "New Orleans Pelicans",
    20: "New York Knicks",
    21: "Oklahoma City Thunder",
    22: "Orlando Magic",
    23: "Philadelphia 76ers",
    24: "Phoenix Suns",
    25: "Portland Trail Blazers",
    26: "Sacramento Kings",
    27: "San Antonio Spurs",
    28: "Toronto Raptors",
    29: "Utah Jazz",
    30: "Washington Wizards",
    37: "Chicago Stags",
    38: "St. Louis Bombers",
    39: "Cleveland Rebels",
    40: "Detroit Falcons",
    41: "Toronto Huskies",
    42: "Washington Capitols",
    43: "Providence Steamrollers",
    44: "Pittsburgh Ironmen",
    45: "Baltimore Bullets",
    46: "Indianapolis Jets",
    47: "Anderson Packers",
    48: "Waterloo Hawks",
    49: "Indianapolis Olympians",
    50: "Denver Nuggets",
    51: "Sheboygan Redskins"
}

def game_checker():
    """Gets game statistics for specified team for today's date. Tells the user to watch the game if their team wins.
    Also tells the user to watch the game if the point differential is less than 15. Tells user to not watch the
    game if their team lost by more than 15 points."""
    if response.status_code == 200:  # 200 is the successful status code if access to API was successful
        data = response.json()
        games = data["data"]  # game data is put into a list of dictionaries
        print(f"Found {len(games)} {team_dict[my_team]} game today\n")
        for game in games:
            home_team = game["home_team"]["full_name"]  # gets home team name
            visitor_team = game["visitor_team"]["full_name"]  # gets away team name
            home_score = game["home_team_score"]  # gets home team score
            visitor_score = game["visitor_team_score"]  # gets away team score
            print(f'{visitor_team} @ {home_team}', end='\n')
            if game["status"] == "Final":  # checks if the game has finished
                if home_team == team_dict[my_team]:  # code that is run if the specified team are the home team
                    if home_score > visitor_score:
                        print("You should watch the game!")
                    elif abs(home_score - visitor_score) <= 15:
                        print("You should watch the game!")
                    else:
                        print("Your team got blown out, don't watch it.")
                else:  # code that runs if the specified team are the away team
                    if visitor_score > home_score:
                        print("You should watch the game!")
                    elif abs(visitor_score - home_score) <= 15:
                        print("You should watch the game!")
                    else:
                        print("Your team got blown out, don't watch it.")
            else:
                print("The game is still going on, watch it!")



# main function that runs the program
if __name__ == '__main__':
    date_today = today_date()   # get today's date
    for key, value in team_dict.items():     # display all the teams with their team codes to the user
        print(f'{key} : {value}', end='\n')
    my_team = int(input("Enter team ID: "))   # Asks the user to enter the team ID they are interested in
    params = {    # Get specified team's games from a specific date range
        "team_ids[]": my_team,
        "start_date": date_today,
        "end_date": date_today,
        "per_page": 50
    }
    response = requests.get(url, headers=headers, params=params)
    game_checker()



