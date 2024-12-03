# %%
import pandas as pd

# --------------------------------------------------------------------
# ------------------------------ PART 1 ------------------------------
# --------------------------------------------------------------------

# %%
df = pd.read_csv("day01/day01_input.csv")
df.head(2)

# %%
df.describe()

# %%
left = df["left"].sort_values().reset_index(drop=True)
right = df["right"].sort_values().reset_index(drop=True)

# %%
ordered_df = pd.DataFrame({"left": left, "right": right})

# %%
ordered_df["diff"] = abs(ordered_df["left"] - ordered_df["right"])
ordered_df.head(2)

# %%
total_diff = sum(ordered_df["diff"])
print("Part 1 solution is", total_diff)

# %%

# --------------------------------------------------------------------
# ------------------------------ PART 2 ------------------------------
# --------------------------------------------------------------------

# %%
total_sim = 0

for i in left:
    if i in right.unique():
        n = right.to_list().count(i) * i
    else:
        n = 0 * i

    total_sim += n

print("Part 2 solution is", total_sim)
# %%
