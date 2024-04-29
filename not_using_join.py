import sqlite3

conn = sqlite3.connect('without_join.db')

conn.execute('''CREATE TABLE locations (
                location_id INT,
                street_address TEXT,
                postal_code INT,
                city TEXT,
                state_province TEXT,
                country_id TEXT
                )''')

conn.execute('''CREATE TABLE countries (
                country_id TEXT,
                region_id INT,
                country_name TEXT
                )''')

conn.executemany('''INSERT INTO locations VALUES (?, ?, ?, ?, ?, ?)''', [
    (1000, '1297 Via Cola di Rie', 989, 'Roma', None, 'IT'),
    (1100, '93091 Calle della Te', 10934, 'Venice', None, 'IT'),
    (1200, '2017 9450 Shinjuku-ku', 1689, 'Tokyo', 'Tokyo Prefecture', 'US'),
    (1300, '9450 Kamiya-cho', 6623,'Hiroshima', None,'JP'),
    (1400, '2014 Jabberwocky Rd Interiors Blvd', 26192, 'Southlake', 'Texas', 'US'),
    (1500, '2011 Interiors Blvd', 99326,'South San Francisco','California', 'US'),
    (1600, '2007 2004 Zagora St Charade Rd', 50090, 'South Brun New Jersey', 'Ontario', 'CA'),
    (1700, '147 Spadina Ave', 98199, 'Seattle', 'Washington', 'US')
    ])

conn.executemany('''INSERT INTO countries VALUES (?, ?, ?)''', [
    ('AR', 2, 'Argentina'),
    ('AU', 3, 'Australia'),
    ('BE', 1, 'Belgium'),
    ('BR',2,'Brazil'),
    ('CA',2,'Canada'),
    ('CH',1,'Switzerland'),
    ('CN',3,'China'),
    ('DE',1,'Germany')
    ])

query = '''
    SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
    FROM locations l, countries c
    WHERE l.country_id = c.country_id
    AND c.country_name = 'Canada'
'''

results = conn.execute(query).fetchall()

for result in results:
    print(result)

conn.close()