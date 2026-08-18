# Function Q10 — **kwargs

# New concept, but simpler than it looks.

# Suppose we call:

# create_profile(
#     name="Pratyush",
#     branch="CSE",
#     semester=7
# )

# Here we're passing named arguments.

# Create:

# def create_profile(**details):

# Inside the function:

# Print the entire details.

# Print the student's name using:

# details["name"]

# Print the branch using:

# details["branch"]

# Then call:

# create_profile(
#     name="Pratyush",
#     branch="CSE",
#     semester=7
# )
# What **kwargs does

# Just like:

# *args

# collects multiple positional arguments,

# **kwargs

# collects multiple keyword/named arguments into a dictionary.

# So inside the function, details will basically be:

# {
#     "name": "Pratyush",
#     "branch": "CSE",
#     "semester": 7
# }

# Try it. No need for a loop yet.

def create_profile(**details):
    print(details["name"])
    print(details["branch"])


create_profile(
    name="Pratyush",
    branch="CSE",
    semester=7
)