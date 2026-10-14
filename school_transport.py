"""School bus transport register: enrol riders, print rosters, send alerts."""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE riders (id INTEGER PRIMARY KEY, student TEXT, "
    "route TEXT, stop TEXT, fee INTEGER)"
)


def enroll_rider(student, route, stop, fee):
    """Add a rider to a route."""
    conn.execute(
        "INSERT INTO riders (student, route, stop, fee) VALUES (?, ?, ?, ?)",
        (student, route, stop, fee),
    )
    conn.commit()


def route_roster(route):
    """Return the names of the students on a route."""
    rows = conn.execute(
        "SELECT student FROM riders WHERE route = ?", (route,)
    )
    return [r[0] for r in rows]


def export_roster(path, route):
    """Write a route's student names to a text file, one per line."""
    with open(path, "w", encoding="utf-8") as out:
        for name in route_roster(route):
            out.write(name + "\n")


def dispatch_alert(route):
    """Announce that the bus for a route is being dispatched."""
    print("dispatching bus " + route)


def fee_collected(route):
    """Return the total fees collected on a route (0 if there are none)."""
    try:
        row = conn.execute(
            "SELECT COALESCE(SUM(fee), 0) FROM riders WHERE route = ?",
            (route,),
        ).fetchone()
    except sqlite3.Error:
        return 0
    return row[0]


def main():
    """Run a short demonstration of the register."""
    enroll_rider("Tara", "R1", "Lake Road", 1800)
    enroll_rider("Kabir", "R1", "Mill Street", 1800)
    enroll_rider("Zoya", "R2", "Fort Gate", 2100)
    if fee_collected("R1") != 3600:
        raise ValueError("unexpected fee total for route R1")
    export_roster("route_r1.txt", "R1")
    dispatch_alert("R1")
    print(route_roster("R2"))


if __name__ == "__main__":
    main()
