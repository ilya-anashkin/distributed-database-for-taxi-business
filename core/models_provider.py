from models import *
from enum import Enum


class ReplicationType(Enum):
    WITH_MAIN_COPY = (1,)
    WITHOUT_MAIN_COPY = (2,)
    COSOLIDATION = (3,)


all_models = [
    (CarClassesModel, ReplicationType.WITH_MAIN_COPY),
    (CarColorsModel, ReplicationType.WITH_MAIN_COPY),
    (CarModelsModel, ReplicationType.WITH_MAIN_COPY),
    (CarModelsRBIModel, ReplicationType.WITH_MAIN_COPY),
    (RegionsModel, ReplicationType.WITH_MAIN_COPY),
    (TaxiPoolsModel, ReplicationType.WITH_MAIN_COPY),
    (EmploymentStatusesModel, ReplicationType.WITH_MAIN_COPY),
    (DriversStatusesModel, ReplicationType.WITH_MAIN_COPY),
    (DriversModel, ReplicationType.WITHOUT_MAIN_COPY),
    (DriversStatesModel, ReplicationType.WITHOUT_MAIN_COPY),
    (CarsModel, ReplicationType.WITH_MAIN_COPY),
    (ClientsModel, ReplicationType.WITHOUT_MAIN_COPY),
    (CarRentsModel, ReplicationType.COSOLIDATION),
    (RidesModel, ReplicationType.COSOLIDATION),
    (UnsatisfactoryRidesModel, ReplicationType.WITHOUT_MAIN_COPY),
]
