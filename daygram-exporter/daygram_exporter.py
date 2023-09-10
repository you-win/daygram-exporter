import sqlite3
import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser("daygram-exporter")
    parser.add_argument("db", help="Path to the sqlite db")
    parser.add_argument("--output", default="./daygram_exported.txt",
                        help="Path to the output file")

    args = parser.parse_args()

    input_path = Path(args.db)
    output_path = Path(args.output)

    print(f"Reading db from {input_path} and writing to {output_path}")

    con = sqlite3.connect(input_path)

    cur = con.cursor()
    res = cur.execute("select * from diary")

    file = open(output_path, "w")

    # Only handle 1 row at a time, otherwise large tables might crash the program
    entry = res.fetchone()
    while entry != None:
        date, _year, _month, _day, content, created, updated = entry
        content = content.strip()

        line = f"---\nDate: {date}\nCreated: {created}\nUpdated: {updated}\n{content}\n"

        print(line)

        file.write(line)

        entry = res.fetchone()

    # Write final line to make it look nice :)
    file.write("---\n")

    print("Finished! Closing file and connection.")

    file.close()
    con.close()

    print("Complete!")


if __name__ == "__main__":
    main()
