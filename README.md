# Task_04_Descriptive_Stats


Reflection: Comparing Pure Python, Pandas, and Polars
This project analyzes datasets using three approaches: Pure Python, Pandas, and Polars. Below is a summary of the performance and trade-offs of each method using the Netflix dataset.

Runtime Comparison
Method	Time (seconds)
Pure Python	0.214
Polars	0.120 (fastest)
Pandas	1.621

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
