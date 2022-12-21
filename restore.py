import webbrowser
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-b', '--backup_path',  default='index.txt', type=str, help='Specificy the backup location.')

args = parser.parse_args()

with open(args.backup_path, "r") as backup:
    for tmp, beatmap_id in enumerate(backup):
        url = f'https://osu.ppy.sh/beatmapsets/{beatmap_id}'
        webbrowser.open(url)
        if tmp % 10 == 0:
            input("Press Enter to continue...")