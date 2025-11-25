from typing import Dict
class Evaluator:
    def __init__(self):
        pass

    def validate(self, generated: Dict, chapter_text: str) -> Dict:
        # Very small validator: checks presence of fields and simple heuristics
        score = 100
        issues = []
        if not generated.get('summary'):
            score -= 25
            issues.append('missing summary')
        if not generated.get('objectives'):
            score -= 25
            issues.append('missing objectives')
        if not generated.get('mcqs'):
            score -= 25
            issues.append('missing mcqs')
        return {'score': score, 'issues': issues}
