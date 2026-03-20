import pandas as pd

df = pd.read_csv("Customer.csv")

print("Initial Data:\n")
print(df.head())
print(df.info())

df = df.drop_duplicates()

print("\nDuplicates:", df.duplicated().sum())


df = df.drop(columns=["Index"])


df["Subscription Date"] = pd.to_datetime(df["Subscription Date"], errors="coerce")

print("\nAfter Date Conversion:\n")
print(df.info())


df["First Name"] = df["First Name"].str.lower().str.strip()
df["Last Name"] = df["Last Name"].str.lower().str.strip()
df["Country"] = df["Country"].str.lower().str.strip()
df["City"] = df["City"].str.lower().str.strip()
df["Company"] = df["Company"].str.lower().str.strip()
df["Email"] = df["Email"].str.lower().str.strip()

print("\nAfter Text Cleaning:\n")
print(df.head())

df.to_csv("cleaned_customer.csv", index=False)

print("\nFile saved successfully!")