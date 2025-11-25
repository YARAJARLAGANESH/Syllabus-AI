from typing import List, Dict
class Planner:
    def __init__(self):
        pass

    def detect_chapters(self, cleaned_text: str) -> List[Dict]:
        """
        Very small heuristic: split by two newlines paragraphs and treat top lines as chapter titles.
        Returns a list of chapter dicts: {chapter_id, title, text}
        """
        chunks = [c.strip() for c in cleaned_text.split('\n\n') if c.strip()]
        chapters = []
        for i, ch in enumerate(chunks):
            title = ch.split('\n')[0][:60]
            chapters.append({
                'chapter_id': f'ch_{i+1}',
                'title': title,
                'text': ch,
            })
        return chapters

    def create_plan(self, chapters: List[Dict]) -> Dict:
        plan = {'chapters': []}
        for ch in chapters:
            plan['chapters'].append({
                'chapter_id': ch['chapter_id'],
                'title': ch['title'],
                'tasks': ['summary','objectives','subtopics','mcqs','resources']
            })
        return plan
