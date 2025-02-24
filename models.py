from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base


class Venture(Base):
    __tablename__ = "ventures"

    id = Column(Integer, primary_key=True, index=True)
    venture_name = Column(String, nullable=True, default="")
    email = Column(String, nullable=True, default="")
    phone = Column(String, nullable=True, default="")
    venture_type = Column(String, nullable=True, default="")
    venture_status = Column(Integer, nullable=True)
    venture_facing = Column(String, nullable=True, default="")
    corner_facing = Column(String, nullable=True, default="")
    venture_length = Column(Integer, nullable=True, default=0)
    venture_breadth = Column(Integer, nullable=True, default=0)
    plot_area = Column(String, nullable=True, default="")
    plot_area_unit = Column(String, nullable=True, default="")
    total_venture_area = Column(String, nullable=True, default="")
    least_plot_price = Column(String, nullable=True, default="")
    plot_price_sq_ft = Column(String, nullable=True, default="")
    road_width = Column(String, nullable=True, default="")
    no_of_plots = Column(Integer, nullable=True, default=0)
    no_of_gates = Column(Integer, nullable=True, default=0)
    distance_info = Column(String, nullable=True, default="")
    venture_address = Column(String, nullable=True, default="")
    venture_state = Column(String, nullable=True)
    venture_district = Column(String, nullable=True)
    venture_city = Column(String,  nullable=True)
    venture_locality = Column(String, nullable=True)
    venture_description = Column(String, nullable=True, default="")
    venture_brochure = Column(String, nullable=True, default="")
    venture_layout = Column(String, nullable=True, default="")
    venture_3d_layout = Column(String, nullable=True, default="")
    venture_video = Column(String, nullable=True, default="")
    venture_latitude = Column(String, nullable=True, default="")
    venture_longitude = Column(String, nullable=True, default="")
    is_rera_approved = Column(Boolean, nullable=True, default=False)
    is_rera_registered = Column(Boolean, nullable=True, default=False)
    approved_by = Column(String, nullable=True, default="")
    rera_no = Column(String, nullable=True, default="")
    tlp_no = Column(String, nullable=True, default="")
    tsl_no = Column(String, nullable=True)
    is_blocked = Column(Boolean, default=False)
    is_gated_community = Column(Boolean, default=False)
    is_popular = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)
    featured_text = Column(String, nullable=True, default="")
    is_low_cost_land = Column(Boolean, default=False)
    venture_featured = Column(Boolean, default=False)
    company_id = Column(Integer,  nullable=True)
    land_status = Column(Integer, default=0)
    drone_approach_videos = Column(String, nullable=True)
    drone_aerial_view = Column(String, nullable=True)
    drone_close_up = Column(String, nullable=True)
    status = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_id = Column(Integer, )
    updated_by_id = Column(Integer,  nullable=True)
