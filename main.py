import os

TEXT = 'The kettle takes its time. Rain does not hurry. The road home will still be there in one more breath. You have carried heavier things than this — and set every one of them down.'


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
