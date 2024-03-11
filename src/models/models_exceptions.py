class TemplateNotFoundError(Exception):
    def __init__(self, message='Template not found!'):
        self.message = message
        super().__init__(self.message)


class ElementDefinitionNotFoundError(Exception):
    def __init__(self, message='Element not found'):
        self.message = message
        super().__init__(self.message)


class ElementTypeNotFound(Exception):
    def __init__(self, message='Element type is not valid'):
        self.message = message
        super().__init__(self.message)


class InvalidElementType(Exception):
    def __init__(self, message='Element type is not valid'):
        self.message = message
        super().__init__(self.message)


class InvalidInput(Exception):
    def __init__(self, message='Element type is not valid'):
        self.message = message
        super().__init__(self.message)
