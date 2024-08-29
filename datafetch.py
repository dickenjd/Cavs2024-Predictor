from nba_api.stats.endpoints import leaguegamefinder, playercareerstats, teamyearbyyearstats
import pandas as pd

def fetch_team_data(seasons):
    all_team_data = []
    for season in seasons:

        print(f"Fetching data for season: {season}")
        team_stats = teamyearbyyearstats.TeamYearByYearStats(season=season)
        team_data = team_stats.get_data_frames()[0]
        all_team_data.append(team_data)
        
    return pd.concat(all_team_data, ignore_index=True)

def fetch_player_data(player_ids):
    all_players_data = []

    for player_id in player_ids:

        print(f"Fetching career stats for player ID: {player_id}")
        player_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        player_data = player_stats.get_data_frames()[0]
        all_players_data.append(player_data)

    return pd.concat(all_players_data, ignore_index=True)

def get_player_ids(seasons):
    
    player_ids = []  
    return player_ids

if __name__ == "__main__":
    seasons = ['2022-23', '2021-22'] 
    player_ids = get_player_ids(seasons) 

    team_data = fetch_team_data(seasons)
    player_data = fetch_player_data(player_ids)

    team_data.to_csv('nba_team_data.csv', index=False)
    player_data.to_csv('nba_player_data.csv', index=False)

    print("Data fetching complete. Files saved as 'nba_team_data.csv' and 'nba_player_data.csv'.")