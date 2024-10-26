# db_module.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///rules.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Rule(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    rule_string = Column(String)

def save_rule_to_db(rule_string):
    new_rule = Rule(rule_string=rule_string)
    session.add(new_rule)
    session.commit()

def get_rule_from_db(rule_id):
    rule = session.query(Rule).filter_by(id=rule_id).first()
    return rule.rule_string

# Initialize DB
Base.metadata.create_all(engine)
