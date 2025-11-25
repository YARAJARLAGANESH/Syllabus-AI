PROMPTS = {
    'summary': 'Write a 2-3 line student-friendly summary for the given chapter text.',
    'objectives': 'Write 4-6 actionable learning objectives, each starting with a verb.',
}
OUTPUT_SCHEMA = {
    'chapter_id': 'str',
    'chapter_title': 'str',
    'summary': 'str',
    'objectives': 'list',
    'subtopics': 'list',
    'mcqs': 'list',
    'resources': 'list',
}
