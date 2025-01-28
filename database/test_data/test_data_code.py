import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 2653379950667880176 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient1 = Patient(first_name="John", last_name="Doe", date_of_birth=date(1970, 1, 1), gender="Male", weight=85.5, height=175.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2653379950667880176)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3404242749264705219 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient2 = Patient(first_name="Jane", last_name="Smith", date_of_birth=date(1980, 5, 15), gender="Female", weight=65.2, height=160.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3404242749264705219)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1568285711940846377 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient3 = Patient(first_name="Alice", last_name="Tan", date_of_birth=date(1990, 10, 20), gender="Female", weight=75.4, height=165.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1568285711940846377)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7770265319362481202 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient4 = Patient(first_name="Bob", last_name="Brown", date_of_birth=date(1965, 12, 30), gender="Male", weight=90.0, height=180.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7770265319362481202)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2398441617393713611 in succeeded_hashes:  # avoid duplicate inserts
            instance = medication1 = Medication(name="Ozempic", typical_dosage="0.5 mg once weekly", description="Medication to improve blood sugar control.")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2398441617393713611)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1869848518336920399 in succeeded_hashes:  # avoid duplicate inserts
            instance = medication2 = Medication(name="Glargine", typical_dosage="Long-acting insulin, dose based on blood sugar readings and doctor's recommendation.", description="Used to lower blood glucose levels in adults with diabetes.")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1869848518336920399)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8831899471038958918 in succeeded_hashes:  # avoid duplicate inserts
            instance = medication3 = Medication(name="Metformin", typical_dosage="500 mg twice daily", description="Lowers glucose production in the liver.")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8831899471038958918)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2723900971756614736 in succeeded_hashes:  # avoid duplicate inserts
            instance = medication4 = Medication(name="Januvia", typical_dosage="100 mg daily", description="Dipeptidyl peptidase-4 (DPP-4) inhibitor that helps increase insulin levels.")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2723900971756614736)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1074164409157187095 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient_med1 = PatientMedication(patient_id=1, medication_id=1, taken_dosage="0.5 mg", start_date=date(2023, 1, 10), end_date=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1074164409157187095)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7963274622627479852 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient_med2 = PatientMedication(patient_id=2, medication_id=2, taken_dosage="10 units", start_date=date(2023, 2, 5), end_date=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7963274622627479852)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 12346222198180344 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient_med3 = PatientMedication(patient_id=3, medication_id=3, taken_dosage="500 mg", start_date=date(2023, 3, 15), end_date=date(2023, 4, 15))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(12346222198180344)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2068697085658635915 in succeeded_hashes:  # avoid duplicate inserts
            instance = patient_med4 = PatientMedication(patient_id=4, medication_id=4, taken_dosage="100 mg", start_date=date(2023, 4, 20), end_date=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2068697085658635915)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5063866879180806400 in succeeded_hashes:  # avoid duplicate inserts
            instance = activity1 = LifestyleActivity(patient_id=1, activity="Walking", duration_minutes=30, date_logged=date(2023, 5, 10))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5063866879180806400)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7300910236520111847 in succeeded_hashes:  # avoid duplicate inserts
            instance = activity2 = LifestyleActivity(patient_id=2, activity="Cycling", duration_minutes=45, date_logged=date(2023, 5, 12))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7300910236520111847)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4283682315503119087 in succeeded_hashes:  # avoid duplicate inserts
            instance = activity3 = LifestyleActivity(patient_id=3, activity="Swimming", duration_minutes=60, date_logged=date(2023, 5, 14))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4283682315503119087)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7137422416154035873 in succeeded_hashes:  # avoid duplicate inserts
            instance = activity4 = LifestyleActivity(patient_id=4, activity="Yoga", duration_minutes=40, date_logged=date(2023, 5, 16))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7137422416154035873)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5842886590742376124 in succeeded_hashes:  # avoid duplicate inserts
            instance = lab_result1 = LabResult(patient_id=1, test_date=date(2023, 6, 1), test_name="HbA1c", result_value=7.1, unit="%")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5842886590742376124)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6909144312013803933 in succeeded_hashes:  # avoid duplicate inserts
            instance = lab_result2 = LabResult(patient_id=2, test_date=date(2023, 6, 2), test_name="Fasting Glucose", result_value=120.0, unit="mg/dL")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6909144312013803933)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 9054271469171334984 in succeeded_hashes:  # avoid duplicate inserts
            instance = lab_result3 = LabResult(patient_id=3, test_date=date(2023, 6, 3), test_name="Lipid Panel", result_value=200.0, unit="mg/dL")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(9054271469171334984)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6243379651563318446 in succeeded_hashes:  # avoid duplicate inserts
            instance = lab_result4 = LabResult(patient_id=4, test_date=date(2023, 6, 4), test_name="Blood Pressure", result_value=130.0, unit="mmHg")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6243379651563318446)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4647895497341952234 in succeeded_hashes:  # avoid duplicate inserts
            instance = glucose_reading1 = BloodGlucoseReading(patient_id=1, reading_date=date(2023, 7, 1), glucose_value=150.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4647895497341952234)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1239523917926098413 in succeeded_hashes:  # avoid duplicate inserts
            instance = glucose_reading2 = BloodGlucoseReading(patient_id=2, reading_date=date(2023, 7, 2), glucose_value=155.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1239523917926098413)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8453385459540166938 in succeeded_hashes:  # avoid duplicate inserts
            instance = glucose_reading3 = BloodGlucoseReading(patient_id=3, reading_date=date(2023, 7, 3), glucose_value=160.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8453385459540166938)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8730615025799814821 in succeeded_hashes:  # avoid duplicate inserts
            instance = glucose_reading4 = BloodGlucoseReading(patient_id=4, reading_date=date(2023, 7, 4), glucose_value=165.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8730615025799814821)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7992556235906087120 in succeeded_hashes:  # avoid duplicate inserts
            instance = comorbidity1 = Comorbidity(patient_id=1, disease_name="Hypertension")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7992556235906087120)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8777041954150495719 in succeeded_hashes:  # avoid duplicate inserts
            instance = comorbidity2 = Comorbidity(patient_id=2, disease_name="Dyslipidemia")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8777041954150495719)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2672938429493008427 in succeeded_hashes:  # avoid duplicate inserts
            instance = comorbidity3 = Comorbidity(patient_id=3, disease_name="Obesity")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2672938429493008427)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3416611409502695563 in succeeded_hashes:  # avoid duplicate inserts
            instance = comorbidity4 = Comorbidity(patient_id=4, disease_name="Sleep Apnea")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3416611409502695563)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8831242863235742602 in succeeded_hashes:  # avoid duplicate inserts
            instance = treatment_plan1 = TreatmentPlan(patient_id=1, plan_details="Increase Metformin dosage.", created_at=datetime.utcnow())
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8831242863235742602)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2980972472095389943 in succeeded_hashes:  # avoid duplicate inserts
            instance = treatment_plan2 = TreatmentPlan(patient_id=2, plan_details="Include Glargine in regimen.", created_at=datetime.utcnow())
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2980972472095389943)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5366241982038356073 in succeeded_hashes:  # avoid duplicate inserts
            instance = treatment_plan3 = TreatmentPlan(patient_id=3, plan_details="Add exercise and lifestyle changes.", created_at=datetime.utcnow())
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5366241982038356073)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5843181826763091611 in succeeded_hashes:  # avoid duplicate inserts
            instance = treatment_plan4 = TreatmentPlan(patient_id=4, plan_details="Start insulin therapy.", created_at=datetime.utcnow())
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5843181826763091611)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
