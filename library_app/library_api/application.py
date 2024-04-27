import logging
import formatter
from pythonjsonlogger import jsonlogger
import ninja
import library_api.domain as domain
import library_api.repository as repository
from library_api.schemas.application import a

logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

router = ninja.Router()

def handler():
    test = "Test"
    return domain.test(
        models=test
    )

@router.get("/get", response={
    200: GetResponse,
    404: Error
})
def get_endpoint(request, body: GetResponse) -> GetResponse | Error:
    try:
        test = "test"
        test_2 = handler().fetch(test)
    except Exception as error:
        logger.exception(error)
        return 404, Error()
    return GetResponse(test_2)