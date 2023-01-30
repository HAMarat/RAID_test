from dao.framework import FrameworkDAO
from service.framework import FrameworkService
from setup_db import db

framework_dao = FrameworkDAO(session=db.session)
framework_service = FrameworkService(dao=framework_dao)
