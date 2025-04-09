# Report: Lead Generation Tool Using Gemini and Web Scraping

## Approach
After understanding the challenge I decide it to re create it but not in google sheets, I am using python and gemini for this challenge, the challenge itself is pretty simple, create good lead data from company urls that provided by the user.

## Model Selection
I selected the Gemini 2.0 Flash (Experimental) model from Google (`gemini-2.0-flash-exp`) because it is free, it is lightweight too compared with gpt I think.

## Data Preprocessing
The tool uses a excel or csv as its data source, with website URLs in the first column. :
- **Input**: first row of column is URLs are read directly from the sheet (csv or excek), assuming other column clean, valid entries.
- **Formulas**: Dynamic queries or prompt it depends on the header collumn (e.g., "B2C or B2B?"), it will ignore the first column since it is a URL.

No cleaning since the data input is URL, and the result is based on gpt or gemini prompt,
No extensive cleaning is performed, as the focus is on real-time extraction. Future iterations could validate URLs or handle malformed data.

## Performance Evaluation
Performance was assessed based on:
- **Accuracy**: The Gemini model reliably on good prompt from what I tested, even 1 sentences can change the result.
- **Speed**: Processing averages 5-7 seconds per row, the reason it's so slow because I limit the code so I don't get any limit from gemini.
- **Scalability**: the code itself can scale, but I don't think the UI is good for production.
- **Business Impact**: With this result I think it can be a good product, and it will gives value to user.

Limitations is on proccessing data per row, with premium/paid model I think I can get this program faster.

## Rationale
With good UI, and good model, I think this product can work, from the website example I don't think it's a good approach for program to input the data directly, sometimes we don't know what error can program produce, it is better approach to create a web for customers and let the program process it.
The streamlit (the UI) is not a good product/package for production, I read on their github and thread it has funny error/bug, like the page refresh when a user click on save button, but with their default download button from previewing the data it won't have this issues.
The gemini is a good model, it can scape or find usefull information as long the developer give the model good prompt.