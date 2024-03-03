def main():
    # Define a dictionary to store batsmen and their runs
    batsmen_runs = {
        'Kohli': 12169,
        'Root': 8713,
        'Smith': 7540,
        'Williamson': 7115,
        'Rohit': 9115,
        'Warner': 8742,
        'Babar': 3890,
        'Labuschagne': 2065
    }

    # (a) Sort the dictionary in descending order of runs
    sorted_batsmen = dict(sorted(batsmen_runs.items(), key=lambda item: item[1], reverse=True))

    # (b) Display name of the batsman with maximum runs
    max_runs_batsman = max(batsmen_runs, key=batsmen_runs.get)

    # (c) Display only the names of batsmen
    batsmen_names = list(batsmen_runs.keys())

    # (d) Add a new batsman
    batsmen_runs['Pujara'] = 6157

    # (e) Remove the batsman having lowest runs
    min_runs_batsman = min(batsmen_runs, key=batsmen_runs.get)
    del batsmen_runs[min_runs_batsman]

    # Display results
    print("(a) Sorted batsmen with runs:", sorted_batsmen)
    print("(b) Batsman with maximum runs:", max_runs_batsman)
    print("(c) Names of batsmen:", batsmen_names)
    print("(d) Added new batsman 'Pujara' with runs:", batsmen_runs['Pujara'])
    print("(e) Removed batsman with lowest runs:", min_runs_batsman)

if __name__ == "__main__":
    main()
