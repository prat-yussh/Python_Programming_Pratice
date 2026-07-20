# Q10: Report File Validator

# Ask the user to enter a file name.

# Valid example:

# report_july.pdf

# Exact requirements
# Remove spaces from both ends.
# Convert the file name to lowercase.
# The file is valid only when:
# it starts with report_;
# it ends with .pdf;
# it contains no spaces;
# something exists between report_ and .pdf.
# When invalid, print:
# Invalid report file

# When valid, extract the report name.

# Example:

# File: report_july.pdf
# Report name: july
# Valid report file


# Useful slicing:

# file_name[7:-4]


# Use:

# startswith()
# endswith()
# in / not in
# slicing


# Do not use a loop. This covers the remaining starting/ending checks from the String chapter.

file_name = input("Enter filename:").strip().lower()

if file_name.startswith("report_") and file_name.endswith(".pdf") and not file_name.isspace():
    print("File:",file_name)
    print("Report name:",file_name[7:-4])
    print("Valid report file")
else:
    print("Invalid report file")