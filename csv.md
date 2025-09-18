Who would know that harmless looking csv file could cause so much trouble? Attention all fellow new Data Engineers. This is a nice checklist that help me save the hassel of hours of debugging. BRAT

## Level1 : sep/delimiter

Always choose '|' this guy over ','

## Level2: encoding charset
default: UTF-8

Types of csv file:


Escape characters:
Backslash escape (\")
This is common in programming libraries (Python csv, Java, etc.). A backslash is used to say “the next character is literal, not special.”

Double-quote escape ("")
This is the RFC 4180 standard used by Excel, Access, SQL Server, and many enterprise tools. If a field contains a quote, it doubles it inside:

Annoying thing: one file mix both stype so need to mormalize it first.

Example:
# Step 1: Read raw file as plain text
raw = spark.read.text(FILE_PATH)

# Step 2: Normalize backslash escapes to doubled quotes
normalized = raw.withColumn(
    "value",
    F.regexp_replace("value", r'\\"', '""')
)
opts = {"sep": ",", "quote": '"', "escape": "\"", "multiLine": "true"}

ddl = """
`BI_CUST_NBR` BIGINT, `BI_ACCT` BIGINT """
header = raw.first()[0] 
raw_no_header = raw.filter(F.col("value") != header) # remove the header as header is defined in ddl

df = (
    raw_no_header
    .select(F.from_csv("value", ddl, opts).alias("parsed"))
    .select("parsed.*")
)


Helper Functions:
Databricks for read raw files to check where went wrong:
raw = spark.read.text(FILE_PATH)
display(raw.filter(raw.value.contains("ROBERT")).limit(20))
