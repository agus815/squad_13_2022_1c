class BDD_Context:

    def __init__(self):
        self.response_code = None
        self.error_message = None
        self.proyect_code = None

    def save_proyect_code(self, project):
        self.proyect_code = project["codigo"]

    def save_response_code(self, response):
        self.response_code = response.status_code

    def save_response_message(self, message):
        self.error_message = message
