from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.memory.session_memory import SessionMemory
from project.core.observability import log_info, log_error
import uuid
class MainAgent:
    def __init__(self):
        self.planner = Planner()
        self.worker = Worker()
        self.evaluator = Evaluator()

    def handle_message(self, user_input: str) -> dict:
        # Treat user_input as raw syllabus text for this demo
        session = SessionMemory(session_id=str(uuid.uuid4()))
        session.set('raw_text', user_input)
        try:
            chapters = self.planner.detect_chapters(user_input)
            plan = self.planner.create_plan(chapters)
            results = []
            for ch in chapters:
                summary = self.worker.generate_summary(ch['text'])
                objectives = self.worker.generate_objectives(ch['text'])
                subtopics = self.worker.generate_subtopics(ch['text'])
                mcqs = self.worker.generate_mcqs(ch['text'])
                resources = self.worker.find_resources(ch['text'])
                generated = {
                    'chapter_id': ch['chapter_id'],
                    'chapter_title': ch['title'],
                    'summary': summary,
                    'objectives': objectives,
                    'subtopics': subtopics,
                    'mcqs': mcqs,
                    'resources': resources
                }
                eval_res = self.evaluator.validate(generated, ch['text'])
                generated['quality_score'] = eval_res['score']
                generated['issues'] = eval_res['issues']
                results.append(generated)
            output = {'response': {'plan': plan, 'chapters': results}}
            return output
        except Exception as e:
            log_error('Processing failed', {'error': str(e)})
            return {'response': {'error': str(e)}}

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result['response']
