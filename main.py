#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:25:12 2023

@author: mehekdaga
"""
"""
Mehek Daga
DS 2000
October 10
Assignment: Tottenham 
"""

FILENAME = '/Users/atifagboatwala/Desktop/Projects/pythonProject/hotspur.txt'

# Initialize variables to keep track of statistics
total_matches = 0
total_wins = 0
total_draws = 0
total_losses = 0
wins_with_one_goal = 0
total_points = 0
goals = []
points = []
# Open the file for reading
with open(FILENAME, 'r') as file:
    while True:
        # Read two lines from the file
        goals_line = file.readline()
        result_line = file.readline().strip()

        goals = goals_line[9:len(goals_line)]
        for element in goals:
            if element == " " or element == "\n":
                continue
            points.append(int(element))
        print(points)

        print(goals.strip(""))

        # Check if we have reached the end of the file
        if not goals_line or not result_line:
            break

        # Convert goals to a list of integers


# Calculate the number of matches played this season
matches_played = len(goals)
total_matches += matches_played

# Count the number of wins, draws, and losses this season
wins = result_line.count('W')
draws = result_line.count('D')
losses = result_line.count('L')

total_wins += wins
total_draws += draws
total_losses += losses

# Count matches won with only one goal
wins_with_one_goal += sum(1 for i in range(matches_played) if goals[i] == 1 and result_line[i] == 'W')

# Calculate points for this season and add to total points
season_points = (wins * 3) + (draws * 1)
total_points += season_points

# Print season statistics
print("Season Stats:")
print(f"Total Matches: {matches_played}")
print(f"Wins: {wins}")
print(f"Draws: {draws}")
print(f"Losses: {losses}")
print(f"Matches won with one goal: {wins_with_one_goal}")
print(f"Points: {season_points}")
print("\n")

# Print overall statistics
print("Overall Stats:")
print(f"Total Matches Played: {total_matches}")
print(f"Total Wins: {total_wins}")
print(f"Total Draws: {total_draws}")
print(f"Total Losses: {total_losses}")
print(f"Total Matches won with one goal: {wins_with_one_goal}")
print(f"Total Points: {total_points}")
