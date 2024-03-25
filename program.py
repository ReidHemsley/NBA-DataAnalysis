import csv

def search_player_stats(file_path, player_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['player'] == player_name:
                return row
    return None

def compare_players(player1_stats, player2_stats, stats_type):
    if player1_stats is None or player2_stats is None:
        print("Player not found.")
        return

    if stats_type.lower() == "per 36 minutes":
        print(f"Comparing per 36 minutes stats for {player1_stats['player']} and {player2_stats['player']}:")
        print(f"Points: {player1_stats['pts_per_36_min']} vs {player2_stats['pts_per_36_min']}")
        print(f"Assists: {player1_stats['ast_per_36_min']} vs {player2_stats['ast_per_36_min']}")
        print(f"Rebounds: {player1_stats['trb_per_36_min']} vs {player2_stats['trb_per_36_min']}")
        print(f"Field goal percentage: {player1_stats['fg_percent']} vs {player2_stats['fg_percent']}")
    elif stats_type.lower() == "per game":
        print(f"Comparing per game stats for {player1_stats['player']} and {player2_stats['player']}:")
        print(f"Points: {player1_stats['pts_per_game']} vs {player2_stats['pts_per_game']}")
        print(f"Assists: {player1_stats['ast_per_game']} vs {player2_stats['ast_per_game']}")
        print(f"Rebounds: {player1_stats['trb_per_game']} vs {player2_stats['trb_per_game']}")
        print(f"Field goal percentage: {player1_stats['fg_percent']} vs {player2_stats['fg_percent']}")
    elif stats_type.lower() == "total":
        print(f"Comparing total stats for {player1_stats['player']} and {player2_stats['player']}:")
        print(f"Points: {player1_stats['pts']} vs {player2_stats['pts']}")
        print(f"Assists: {player1_stats['ast']} vs {player2_stats['ast']}")
        print(f"Rebounds: {player1_stats['trb']} vs {player2_stats['trb']}")
        print(f"Field goal percentage: {player1_stats['fg_percent']} vs {player2_stats['fg_percent']}")
    else:
        print("Invalid stats type.")

# File paths
per_36_minutes_file = 'Archive/Per 36 Minutes.csv'
player_totals_file = 'Archive/Player Totals.csv'
player_per_game_file = 'Archive/Player Per Game.csv'

# Get user input
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")

# Get stats type input
stats_type = input("Enter the type of stats to compare (per 36 minutes, per game, or total): ")

# Search and compare player stats based on stats type
if stats_type.lower() == "per 36 minutes":
    player1_stats = search_player_stats(per_36_minutes_file, player1)
    player2_stats = search_player_stats(per_36_minutes_file, player2)
elif stats_type.lower() == "per game":
    player1_stats = search_player_stats(player_per_game_file, player1)
    player2_stats = search_player_stats(player_per_game_file, player2)
elif stats_type.lower() == "total":
    player1_stats = search_player_stats(player_totals_file, player1)
    player2_stats = search_player_stats(player_totals_file, player2)
else:
    print("Invalid stats type.")
    player1_stats = None
    player2_stats = None

compare_players(player1_stats, player2_stats, stats_type)
