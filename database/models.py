# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 24, 2025 22:16:30
# Database: sqlite:////tmp/tmp.YR6OlMcEMc-01JJD65AE00RDCE3NW9RJ40AST/DiaCareManagementSuite/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Medication(Base):  # type: ignore
    """
    description: Model representing typical diabetes medications.
    """
    __tablename__ = 'medications'
    _s_collection_name = 'Medication'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    typical_dosage = Column(String)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PatientMedicationList : Mapped[List["PatientMedication"]] = relationship(back_populates="medication")



class Patient(Base):  # type: ignore
    """
    description: Model representing patient details.
    """
    __tablename__ = 'patients'
    _s_collection_name = 'Patient'  # type: ignore

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    weight = Column(Float)
    height = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    BloodGlucoseReadingList : Mapped[List["BloodGlucoseReading"]] = relationship(back_populates="patient")
    ComorbidityList : Mapped[List["Comorbidity"]] = relationship(back_populates="patient")
    LabResultList : Mapped[List["LabResult"]] = relationship(back_populates="patient")
    LifestyleActivityList : Mapped[List["LifestyleActivity"]] = relationship(back_populates="patient")
    PatientMedicationList : Mapped[List["PatientMedication"]] = relationship(back_populates="patient")
    TreatmentPlanList : Mapped[List["TreatmentPlan"]] = relationship(back_populates="patient")



class BloodGlucoseReading(Base):  # type: ignore
    """
    description: Model representing daily blood glucose readings for patients.
    """
    __tablename__ = 'blood_glucose_readings'
    _s_collection_name = 'BloodGlucoseReading'  # type: ignore

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'))
    reading_date = Column(Date)
    glucose_value = Column(Float)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("BloodGlucoseReadingList"))

    # child relationships (access children)



class Comorbidity(Base):  # type: ignore
    """
    description: Model representing comorbidities associated with the patient.
    """
    __tablename__ = 'comorbidities'
    _s_collection_name = 'Comorbidity'  # type: ignore

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'))
    disease_name = Column(String)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("ComorbidityList"))

    # child relationships (access children)



class LabResult(Base):  # type: ignore
    """
    description: Model representing lab test results for patients.
    """
    __tablename__ = 'lab_results'
    _s_collection_name = 'LabResult'  # type: ignore

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'))
    test_date = Column(Date)
    test_name = Column(String)
    result_value = Column(Float)
    unit = Column(String)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("LabResultList"))

    # child relationships (access children)



class LifestyleActivity(Base):  # type: ignore
    """
    description: Model representing lifestyle activities of a patient.
    """
    __tablename__ = 'lifestyle_activities'
    _s_collection_name = 'LifestyleActivity'  # type: ignore

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'))
    activity = Column(String)
    duration_minutes = Column(Integer)
    date_logged = Column(Date)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("LifestyleActivityList"))

    # child relationships (access children)



class PatientMedication(Base):  # type: ignore
    """
    description: Link table to map patients to their prescribed medications.
    """
    __tablename__ = 'patient_medications'
    _s_collection_name = 'PatientMedication'  # type: ignore

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'))
    medication_id = Column(ForeignKey('medications.id'))
    taken_dosage = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    # parent relationships (access parent)
    medication : Mapped["Medication"] = relationship(back_populates=("PatientMedicationList"))
    patient : Mapped["Patient"] = relationship(back_populates=("PatientMedicationList"))

    # child relationships (access children)



class TreatmentPlan(Base):  # type: ignore
    """
    description: Model representing the treatment plan outlined for the patient.
    """
    __tablename__ = 'treatment_plans'
    _s_collection_name = 'TreatmentPlan'  # type: ignore

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'))
    plan_details = Column(String)
    created_at = Column(DateTime)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("TreatmentPlanList"))

    # child relationships (access children)
