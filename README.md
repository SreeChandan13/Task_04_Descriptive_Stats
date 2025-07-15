# Task_04_Descriptive_Stats


Reflection: Comparing Pure Python, Pandas, and Polars
This project analyzes datasets using three approaches: Pure Python, Pandas, and Polars. Below is a summary of the performance and trade-offs of each method using the Netflix dataset.

Runtime Comparison
Method	Time (seconds)
Pure Python	0.214
Polars	0.120 (fastest)
Pandas	1.621

Datasets Used
To demonstrate that the system can handle arbitrary datasets beyond the original election-related files, we applied our analysis scripts to two well-known public datasets:

Netflix Dataset: Contains metadata on thousands of Netflix titles, including type, country, rating, release year, and duration.

Titanic Dataset: Contains passenger information such as age, fare, sex, class, and survival status.

Both datasets were analyzed using pure Python, Pandas, and Polars, with the analyses driven by metadata configuration files (in JSON format). These metadata files specify:

Which columns are numeric or categorical

Which fields to group by

The filename of the dataset

This modular design ensures that the statistics system is dataset-agnostic and can easily be extended to new datasets by simply updating the metadata, without rewriting the analysis code.

🔍 Key Insights
Polars was the fastest due to its Rust backend and support for multi-threading. It’s ideal for high-performance data analysis.

Pandas is slower but extremely versatile, beginner-friendly, and has widespread community support.

Pure Python is efficient for small datasets and learning purposes but lacks high-level features like grouping or null handling.

💡 Recommendations
Use Pandas for quick prototyping, teaching, or when working in a team.

Use Polars when speed matters (e.g., large datasets or batch processing).

Use Pure Python to understand how data operations work under the hood.

🤖 On Using AI Tools
When prompted to perform descriptive statistics, tools like ChatGPT often default to Pandas due to its popularity and rich syntax. While this is a good starting point, knowing when to switch to Polars can provide significant performance gains
