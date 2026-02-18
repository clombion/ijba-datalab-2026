This is the final structural piece. The **Spiral Pattern** perfectly integrates the "System Design" approach with the need for repetition. Instead of treating the pipeline as a linear list where we "leave behind" Step 1 to do Step 2, we treat it as a widening loop.

Every day, the students run the pipeline from the start (`Define`), moving quickly through the steps they have already mastered, until they hit the **New Topic** of the day, where they slow down and deepen their practice.

Here is the **Spiral Curriculum**:

### **The "Spiral" Model**

* **The Daily Rhythm:** Every morning starts with **Define** (The Horizon Table).
* **The Acceleration:** On Day 1, "Find & Get" takes all afternoon. By Day 4, "Find & Get" takes 10 minutes (because we use AI/CLI), leaving the rest of the day for Analysis.

---

### **Day 1: The First Loop (Define  Find  GET)**

*Focus: Structure & Acquisition. The loop stops at "Get."*

* **Morning: The Launch (Define)**
* **Spiral Step 1 (Define):** **Tabular Thinking.** We don't just look at data; we design it.
* **Exercise:** Deconstruct a published chart (e.g., "Car Accidents") back into its spreadsheet rows and columns.
* **The Friction:** Manually typing 20 rows of "Class Demographics" to feel the structure.


* **Afternoon: The "Wow" (Find  Get)**
* **Spiral Step 2 (Find):** Locating a structured table on Wikipedia (e.g., "French Presidents").
* **Spiral Step 3 (Get):** **The Topic of the Day.**
* **Tool:** `IMPORTHTML` in Google Sheets.
* **Activity:** Pulling the data live.
* **The Skill:** Documenting the **"Web-Import Skill"**.



---

### **Day 2: The Second Loop (Define  ...  VERIFY)**

*Focus: Ontology & Truth. The loop moves quickly past Get and stops at "Verify."*

* **Morning: The "Maternity" Loop (Define  Find)**
* **Spiral Step 1 (Define):** Rapidly design the **Horizon Table** for the **"Maternity Ward Medicalization"** hypothesis.
* **Spiral Step 2 (Find):** Use **NotebookLM** as a "Scout" to locate the C-section tables in 10 PDF reports.
* **Spiral Step 3 (Get):** (Skipped/Simulated) We acknowledge we *could* scrape this, but today we focus on the data's meaning.


* **Afternoon: The Audit (Verify)**
* **Spiral Step 4 (Verify):** **The Topic of the Day.**
* **Concept:** Data as "Structured Representation".
* **Activity:** Manually audit the NotebookLM findings against the PDF.
* **The Trap:** Identify "ambiguous nulls" (empty vs. 0) and missing medical codes.
* **Artifact:** A **"Verification Log"** comparing the Source to the Dataset.



---

### **Day 3: The Third Loop (Define  ...  CLEAN)**

*Focus: Hygiene & The Wall. The loop runs fully until it hits the "Clean" obstacle.*

* **Morning: The "Rurbanization" Loop (Define  Get)**
* **Spiral Step 1 (Define):** Design the Horizon Table for **"Digital Divide in Rural Areas"**.
* **Spiral Step 2 (Find):** Locate the raw "Addresses of Public Services" file.
* **Spiral Step 3 (Get):** Import the messy CSV into Sheets.
* **Spiral Step 4 (Verify):** Quick spot-check. "Wait, 'St. Martin' and 'Saint-Martin' are listed as different cities."


* **Afternoon: The Wall (Clean)**
* **Spiral Step 5 (Clean):** **The Topic of the Day.**
* **Activity:** Attempt to clean 1,000 rows of inconsistent addresses using standard Sheets filters.
* **The Lesson:** It is slow and fragile. The spiral is blocked by manual tools.
* **The Setup:** "We need a faster engine for this loop."



---

### **Day 4: The Fourth Loop (Define  ...  ANALYZE)**

*Focus: Automation & Insight. We accelerate through the early steps using AI/CLI to reach Analysis.*

* **Morning: The Turbo Loop (Get  Clean)**
* **Spiral Steps 3 & 5 (Get/Clean):** **Automation.**
* **Tool:** **Command Line Agents** (Terminal + `uv`).
* **Activity:** Run the AI script to clean the "Rurbanization" data from Day 3 instantly.
* **Result:** The spiral that took hours yesterday now takes seconds.


* **Afternoon: The Insight (Analyze I)**
* **Spiral Step 6 (Analyze):** **The Topic of the Day.**
* **Tool:** Google Sheets (Pivot Tables).
* **Activity:** Calculate the distribution of digital centers by region.
* **Artifact:** First descriptive charts.



---

### **Day 5: The Full Loop (Define  ...  PRESENT)**

*Focus: The Story. The spiral completes the full journey.*

* **Morning: The Deep Dive (Analyze II)**
* **Recap:** Rapidly review the verified, cleaned "Rurbanization" dataset.
* **Spiral Step 6 (Analyze):** **Cross-Analysis.**
* **Activity:** Merge with "Population Density" data to test the hypothesis: "Do rural areas have fewer services per capita?"


* **Afternoon: The Final Station (Present)**
* **Spiral Step 7 (Present):** **The Topic of the Day.**
* **Concept:** The Triad (Data, Form, Message).
* **Output:** The Portfolio.
1. The **Story** (Datawrapper).
2. The **Horizon Table** (Final Dataset).
3. The **Skill Library** (The Scripts/Prompts used to accelerate the loops).
