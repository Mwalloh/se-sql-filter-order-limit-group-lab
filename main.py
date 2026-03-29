import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1
# Replace None with your code
df_no_moons = """
    SELECT * 
    FROM planets
    WHERE num_of_moons = 0;
"""

# STEP 2
# Replace None with your code
df_name_seven = """
    SELECT name, mass 
    FROM planets 
    WHERE length(name) = 7;
"""


##### Part 2: Advanced Filtering #####

# STEP 3
# Replace None with your code
df_mass = """
    SELECT name, mass
    FROM planets 
    WHERE mass <= 1.00;
"""


# STEP 4
# Replace None with your code
df_mass_moon = """
    SELECT * 
    FROM planets 
    WHERE num_of_moons >= 1 AND mass < 1.00;
"""

# STEP 5
# Replace None with your code
df_blue = """
    SELECT name, color 
    FROM planets 
    WHERE color = "blue";
"""



##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6
# Replace None with your code
df_hungry = """
    SELECT name, age, breed
    FROM dogs 
    WHERE hungry = 1
    ORDER BY age ASC;
"""

# STEP 7
# Replace None with your code
df_hungry_ages = """
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1 
    AND age BETWEEN 2 AND 7
    ORDER BY name;
"""

# STEP 8
# Replace None with your code
df_4_oldest = """
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC, breed
    LIMIT 4;
"""



##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
# Replace None with your code
df_ruth_years = """
    SELECT COUNT(DISTINCT year) 
    FROM babe_ruth_stats
"""


# STEP 10
# Replace None with your code
df_hr_total = """
    SELECT SUM(HR)
    FROM babe_ruth_stats
"""



##### Part 5: Grouping and Aggregation #####

# STEP 11
# Replace None with your code
df_teams_years = """
    SELECT team, COUNT(DISTINCT years) AS number_years
    FROM babe_ruth_stats
    GROUP BY team;
"""


# STEP 12
# Replace None with your code
df_at_bats = """
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    WHERE at_bats > 200
    GROUP BY team;
"""



conn1.close()
conn2.close()
conn3.close()