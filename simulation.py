import pandas as pd
import random
import argparse


class MonteCarloSimulation:
    """
    Monte Carlo Simulation of Monty Hall Problem
    
    You stand in front of the N number of doors.
    Behind one of those doors is a brand new car that you can win. 
    Behind other rest of the doors is a goat.
    
    First, you randomly choose the one door and,
    host open the rest of doors which must contain a goat.
    
    Host gives you second a chance to decide or switch the door.
    At the end prize is revealed.
    Most of the time, the chance of wining the game is by switching
    the door in second chance and not by sticking to door you selected in
    first chance.
    
    This class simulates the same with n number of doors.
    
    """
    def __init__(self, n_doors, n_samples):
        self.number_of_doors = n_doors
        self.n_samples = n_samples
        self.doors = set(range(1, self.number_of_doors + 1))

    def simulate(self):        
        data = []
        
        for i in range(self.n_samples):
            prize = random.randint(1, self.number_of_doors)
            candidate = random.randint(1, self.number_of_doors)

            # Host leaves 1 door
            remanining_doors = {prize, candidate} if prize != candidate else {random.choice(list(self.doors - {candidate})), candidate}

            switch_no = candidate
            switch_yes = (remanining_doors - {candidate}).pop()

            switch_no_win = switch_no == prize
            switch_yes_win = switch_yes == prize

            data.append([prize, candidate, self.doors - remanining_doors, switch_no, switch_yes, "WON" if switch_yes_win else "LOST"])

        table_df = pd.DataFrame(data, columns=["Prize", "Candidate", "Host", "Switch No", "Switch Yes", "Result"])
        print(table_df)
        table_df.to_csv(f"{self.number_of_doors}_doors_{self.n_samples}_samples.csv", index=False)
        print(table_df['Result'].value_counts(normalize=True))
     
 
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="MonteCarloSimulation")
    parser.add_argument("--doors", type=int, default=3, help="Number of doors")
    parser.add_argument("--samples", type=int, default=100, help="Number of samples")
    args = parser.parse_args()
    MonteCarloSimulation(args.doors, args.samples).simulate()

