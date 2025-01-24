# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Patient(Base):
    """description: Model representing patient details."""
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    weight = Column(Float)
    height = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=
        datetime.utcnow)

class Medication(Base):
    """description: Model representing typical diabetes medications."""
    __tablename__ = 'medications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    typical_dosage = Column(String)
    description = Column(String)

class PatientMedication(Base):
    """description: Link table to map patients to their prescribed medications."""
    __tablename__ = 'patient_medications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    medication_id = Column(Integer, ForeignKey('medications.id'))
    taken_dosage = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

class LifestyleActivity(Base):
    """description: Model representing lifestyle activities of a patient."""
    __tablename__ = 'lifestyle_activities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    activity = Column(String)
    duration_minutes = Column(Integer)
    date_logged = Column(Date)

class LabResult(Base):
    """description: Model representing lab test results for patients."""
    __tablename__ = 'lab_results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    test_date = Column(Date)
    test_name = Column(String)
    result_value = Column(Float)
    unit = Column(String)

class BloodGlucoseReading(Base):
    """description: Model representing daily blood glucose readings for patients."""
    __tablename__ = 'blood_glucose_readings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    reading_date = Column(Date)
    glucose_value = Column(Float)

class Comorbidity(Base):
    """description: Model representing comorbidities associated with the patient."""
    __tablename__ = 'comorbidities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    disease_name = Column(String)

class TreatmentPlan(Base):
    """description: Model representing the treatment plan outlined for the patient."""
    __tablename__ = 'treatment_plans'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    plan_details = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    patient1 = Patient(first_name="John", last_name="Doe", date_of_birth=date(1970, 1, 1), gender="Male", weight=85.5, height=175.0)
    patient2 = Patient(first_name="Jane", last_name="Smith", date_of_birth=date(1980, 5, 15), gender="Female", weight=65.2, height=160.0)
    patient3 = Patient(first_name="Alice", last_name="Tan", date_of_birth=date(1990, 10, 20), gender="Female", weight=75.4, height=165.0)
    patient4 = Patient(first_name="Bob", last_name="Brown", date_of_birth=date(1965, 12, 30), gender="Male", weight=90.0, height=180.0)
    medication1 = Medication(name="Ozempic", typical_dosage="0.5 mg once weekly", description="Medication to improve blood sugar control.")
    medication2 = Medication(name="Glargine", typical_dosage="Long-acting insulin, dose based on blood sugar readings and doctor's recommendation.", description="Used to lower blood glucose levels in adults with diabetes.")
    medication3 = Medication(name="Metformin", typical_dosage="500 mg twice daily", description="Lowers glucose production in the liver.")
    medication4 = Medication(name="Januvia", typical_dosage="100 mg daily", description="Dipeptidyl peptidase-4 (DPP-4) inhibitor that helps increase insulin levels.")
    patient_med1 = PatientMedication(patient_id=1, medication_id=1, taken_dosage="0.5 mg", start_date=date(2023, 1, 10), end_date=None)
    patient_med2 = PatientMedication(patient_id=2, medication_id=2, taken_dosage="10 units", start_date=date(2023, 2, 5), end_date=None)
    patient_med3 = PatientMedication(patient_id=3, medication_id=3, taken_dosage="500 mg", start_date=date(2023, 3, 15), end_date=date(2023, 4, 15))
    patient_med4 = PatientMedication(patient_id=4, medication_id=4, taken_dosage="100 mg", start_date=date(2023, 4, 20), end_date=None)
    activity1 = LifestyleActivity(patient_id=1, activity="Walking", duration_minutes=30, date_logged=date(2023, 5, 10))
    activity2 = LifestyleActivity(patient_id=2, activity="Cycling", duration_minutes=45, date_logged=date(2023, 5, 12))
    activity3 = LifestyleActivity(patient_id=3, activity="Swimming", duration_minutes=60, date_logged=date(2023, 5, 14))
    activity4 = LifestyleActivity(patient_id=4, activity="Yoga", duration_minutes=40, date_logged=date(2023, 5, 16))
    lab_result1 = LabResult(patient_id=1, test_date=date(2023, 6, 1), test_name="HbA1c", result_value=7.1, unit="%")
    lab_result2 = LabResult(patient_id=2, test_date=date(2023, 6, 2), test_name="Fasting Glucose", result_value=120.0, unit="mg/dL")
    lab_result3 = LabResult(patient_id=3, test_date=date(2023, 6, 3), test_name="Lipid Panel", result_value=200.0, unit="mg/dL")
    lab_result4 = LabResult(patient_id=4, test_date=date(2023, 6, 4), test_name="Blood Pressure", result_value=130.0, unit="mmHg")
    glucose_reading1 = BloodGlucoseReading(patient_id=1, reading_date=date(2023, 7, 1), glucose_value=150.0)
    glucose_reading2 = BloodGlucoseReading(patient_id=2, reading_date=date(2023, 7, 2), glucose_value=155.0)
    glucose_reading3 = BloodGlucoseReading(patient_id=3, reading_date=date(2023, 7, 3), glucose_value=160.0)
    glucose_reading4 = BloodGlucoseReading(patient_id=4, reading_date=date(2023, 7, 4), glucose_value=165.0)
    comorbidity1 = Comorbidity(patient_id=1, disease_name="Hypertension")
    comorbidity2 = Comorbidity(patient_id=2, disease_name="Dyslipidemia")
    comorbidity3 = Comorbidity(patient_id=3, disease_name="Obesity")
    comorbidity4 = Comorbidity(patient_id=4, disease_name="Sleep Apnea")
    treatment_plan1 = TreatmentPlan(patient_id=1, plan_details="Increase Metformin dosage.", created_at=datetime.utcnow())
    treatment_plan2 = TreatmentPlan(patient_id=2, plan_details="Include Glargine in regimen.", created_at=datetime.utcnow())
    treatment_plan3 = TreatmentPlan(patient_id=3, plan_details="Add exercise and lifestyle changes.", created_at=datetime.utcnow())
    treatment_plan4 = TreatmentPlan(patient_id=4, plan_details="Start insulin therapy.", created_at=datetime.utcnow())
    
    
    
    session.add_all([patient1, patient2, patient3, patient4, medication1, medication2, medication3, medication4, patient_med1, patient_med2, patient_med3, patient_med4, activity1, activity2, activity3, activity4, lab_result1, lab_result2, lab_result3, lab_result4, glucose_reading1, glucose_reading2, glucose_reading3, glucose_reading4, comorbidity1, comorbidity2, comorbidity3, comorbidity4, treatment_plan1, treatment_plan2, treatment_plan3, treatment_plan4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
