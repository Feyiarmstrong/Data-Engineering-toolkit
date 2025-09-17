# Data-Engineering-toolkit


## Purpose

This repository is a collection of scripts and resources that demonstrate common data engineering tasks.
It is designed as a learning toolkit to practice:
 • Data cleaning
 • Data transformation
 • Data loading

The goal is to build reusable components that can serve as building blocks for larger data engineering projects.

⸻

## Documentation

Each script in this toolkit focuses on a specific task:
 • data_cleaning.py → functions for handling missing values, duplicates, and basic data quality fixes.
 • data_transformation.py → functions to reshape, aggregate, or enrich datasets.
 • data_loading.py → functions to write data into files (CSV, Parquet).

Additional documentation will be added as new features are developed.

## Code example 

import pandas as pd

### Sample dataframe
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice"],
    "age": [25, None, 25]
})

#### Clean
df = clean_data(df)

#### Transform
df = transform_data(df)

#### Load
save_to_csv(df, "output.csv")


## Contribution Guide

Contributions are welcomed : 
• Follow the Gitflow branching strategy: 
• main : stable production code 
• develop : integration branch 
• feature/<branch-name> : feature development 

 
 ### Steps to contribute:
 
 1. Fork the repository
 2. Create a feature branch (feature/new-script)
 3. Commit changes and push
 4. Open a Pull Request against develop
