from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base



class Venture(Base):
    __tablename__ = "ventures"

    id = Column(Integer, primary_key=True, index=True)
    venture_name = Column(String, nullable=True, default="")
    email = Column(String, nullable=True, default="")
    phone = Column(String, nullable=True, default="")
    venture_type = Column(String, nullable=True, default="", comment="All, Residential, Commercial, Gated Community")
    venture_status = Column(Integer, nullable=True, comment="Ready To Move, Under Construction")
    venture_facing = Column(String, nullable=True, default="")
    venture_length = Column(Integer, nullable=True, default=0)
    venture_breadth = Column(Integer, nullable=True, default=0)
    plot_area = Column(String, nullable=True, default="")
    no_of_plots = Column(Integer, nullable=True, default=0)
    no_of_gates = Column(Integer, nullable=True, default=0)
    distance_info = Column(String, nullable=True, default="")
    venture_address = Column(String, nullable=True, default="")
    venture_state_id = Column(Integer,  nullable=True)
    venture_district_id = Column(Integer, nullable=True)
    venture_city_id = Column(Integer,  nullable=True)
    is_rera_approved = Column(Boolean, default=False)
    is_rera_registered = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)
    status = Column(Integer, default=0, comment="0=active;1=inactive;2=delete")
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column( Integer,default="")
    updated_by = Column(Integer, default="")



