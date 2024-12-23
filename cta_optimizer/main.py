from cta_optimizer.station_data_loader import StationDataLoader

def main():
    station_loader = StationDataLoader([
        "./data/trains/cta/yellow_line.json",
        "./data/trains/cta/red_line.json",
    ])


if __name__ == "__main__":
    main()