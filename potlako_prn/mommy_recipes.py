from faker import Faker
from model_mommy.recipe import Recipe

from edc_visit_tracking.constants import SCHEDULED

from .models import DeathReport, CoordinatorExit, SubjectOffStudy

fake = Faker()

deathreport = Recipe(
    DeathReport,)

coordinatorexit = Recipe(
    CoordinatorExit,)

subjectoffstudy = Recipe(
    SubjectOffStudy,)
