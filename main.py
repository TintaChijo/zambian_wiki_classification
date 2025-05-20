import wikipediaapi
import pandas as pd

# List of Zambian Wikipedia page titles (you can add more)
zambian_titles = [
    "Zambia",
    "Lusaka",
    "Hakainde Hichilema",
    "Kenneth Kaunda",
    "Zambian cuisine",
    "Economy of Zambia",
    "Education in Zambia",
    "Zambian kwacha",
    "Victoria Falls",
    "Zambian music",
    "Zambia national football team",
    "Lake Kariba",
    "Zambian culture",
    "Politics of Zambia",
    "Zambian literature",
    "Zambian independence",
    "Zambia women's national football team",
    "Zambian traditional ceremonies",
    "Zambian wildlife",
    "Mining in Zambia"
]


wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='ZambianWikiProject/1.0 (mutintac@unza.zm)'
)

# Function to get sections of a page
def get_sections(page):
    sections = []
    for section in page.sections:
        text = section.text
        word_count = len(text.split())
        sections.append({
            'title': page.title,
            'section_title': section.title,
            'word_count': word_count,
            'text': text
        })
    return sections

# Collect all sections from the pages
all_sections = []

for title in zambian_titles:
    page = wiki.page(title)
    if page.exists():
        print(f"Processing: {title}")
        sections = get_sections(page)
        all_sections.extend(sections)
    else:
        print(f"Page not found: {title}")

# Convert to DataFrame
df = pd.DataFrame(all_sections)

# Optional: Add labels based on word count
def label_completeness(wc):
    if wc >= 300:
        return 'Complete'
    elif wc >= 50:
        return 'Incomplete'
    else:
        return 'Stub'

df['completeness_label'] = df['word_count'].apply(label_completeness)

# Save to CSV
df.to_csv("zambian_wiki_sections.csv", index=False)
print("Data saved to zambian_wiki_sections.csv")

