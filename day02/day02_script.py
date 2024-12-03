# %%
import pandas as pd

# --------------------------------------------------------------------
# ------------------------------ PART 1 ------------------------------
# --------------------------------------------------------------------

# %% import the input
df = pd.read_csv("day02_input.csv")
df.head(2)

# %% make it a usable list
df["list"] = df["input"].apply(lambda x: list(map(int, x.split())))
df.head()

# %% create a col with max difference between levels
max_diff = 3
min_diff = 1

test = [85, 87, 89, 92, 93, 96, 98, 98]

for i in range(len(test) - 1):
    diff = abs((test[i] - test[i + 1]))
    if diff < min_diff or diff > max_diff:
        print("unsafe")


# %% if loop

for i in range(len(df)):

    diff = abs((test[i] - test[i + 1]))

    if df.loc[i, "list"] == sorted(df.loc[i, "list"]):
        df.loc[i, "safe"] = "yes"

    elif df.loc[i, "list"] == sorted(df.loc[i, "list"], reverse=True):
        df.loc[i, "safe"] = "yes"

    else:
        df.loc[i, "safe"] = "no"

df.head()

# %% sum of safe reports
total_safe = df["safe"].count("yes")
print("Part 1 solution is", total_safe)

# %%
