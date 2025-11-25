from typing import Dict, List
class Worker:
    def __init__(self):
        pass

    def generate_summary(self, chapter_text: str) -> str:
        # naive summarizer: first sentence or first 120 chars
        s = chapter_text.strip().split('\n')[0]
        return (s[:200] + '...') if len(s) > 200 else s

    def generate_objectives(self, chapter_text: str) -> List[str]:
        # return 4 sample action-oriented objectives derived from title/text
        base = chapter_text.strip().split('\n')[0][:80]
        return [
            f'Explain the concept of {base}.',
            f'Identify key subtopics related to {base}.',
            f'Solve basic problems involving {base}.',
            f'Compare and evaluate methods related to {base}.',
        ]

    def generate_subtopics(self, chapter_text: str) -> List[str]:
        lines = [l.strip() for l in chapter_text.split('\n') if l.strip()]
        subs = lines[1:6] if len(lines) > 1 else ['Overview', 'Examples', 'Practice']
        return subs

    def generate_mcqs(self, chapter_text: str, n:int=5) -> List[Dict]:
        mcqs = []
        for i in range(n):
            mcqs.append({
                'q': f'Sample question {i+1} about the chapter',
                'options': ['A','B','C','D'],
                'answer': 'A',
                'difficulty': 'medium'
            })
        return mcqs

    def find_resources(self, chapter_text: str) -> List[Dict]:
        return [{'title':'Standard Textbook', 'type':'book', 'citation':'Author - Intro Textbook'}]
