world-universities
======================
This is a forked copy of two CSV files with universities in the US and around the world.

## Usage

This package assumes that you already have a table called `universities` in your DB connection. If you don't, please create the table with the following columns: `id`. `name`, `country`, and `website`. Thanks

```bash
git clone github.com/geziwen/world-universities.git
cd world-universities
```

Plase open the file mysql.py and enter your database configuration. Then:

```bash
./mysql.py
```
