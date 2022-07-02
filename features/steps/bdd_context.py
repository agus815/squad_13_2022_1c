class BDD_Context:

    def __init__(self):
        self.response_code = None
        self.error_message = None
        self.proyect_code = None
        self.task_code = None

    def save_proyect_code(self, code):
        self.proyect_code = code

    def save_task_code(self, code):
        self.task_code = code

    def save_response_code(self, response):
        self.response_code = response.status_code

    def save_response_message(self, message):
        self.error_message = message
