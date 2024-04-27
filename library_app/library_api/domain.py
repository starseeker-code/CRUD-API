from dataclass import dataclass
import library_api.repository as repository
from library_api.schemas.domain import b

@dataclass
class test:
    models = repository.ModelRepo()
    
    def fetch(self):
        test = "test"
        test_2 = self.models.do_fetch(test)
        return test_2