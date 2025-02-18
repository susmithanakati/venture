from sqlalchemy.orm import Session
from models import Venture
from schemas import VentureCreate,VentureResponse
import models
import schemas

def create_venture(db:Session, venture:VentureCreate):
    new_venture = Venture(**venture.dict())
    db.add(new_venture)
    db.commit()
    db.refresh(new_venture)
    return new_venture

def get_ventures(db:Session):
    return db.query(Venture).all()

def get_venture(db:Session,venture_id:int):
    return db.query(Venture).filter(Venture.id == venture_id).first()

def update_venture(db:Session,venture_id:int,update_venture:VentureCreate):
    venture = db.query(Venture).filter(Venture.id == venture_id).first()
    if not venture:
        return None
    venture.venture_name = update_venture.venture_name
    venture.email = update_venture.email
    venture.phone = update_venture.phone
    venture.venture_type = update_venture.venture_type
    venture.venture_status = update_venture.venture_status
    venture.venture_facing = update_venture.venture_facing
    venture.corner_facing = update_venture.corner_facing
    venture.venture_length = update_venture.venture_length
    venture.venture_breadth = update_venture.venture_breadth
    venture.plot_area = update_venture.plot_area
    venture.plot_area_unit = update_venture.plot_area_unit
    venture.total_venture_area = update_venture.total_venture_area
    venture.least_plot_price = update_venture.least_plot_price
    venture.plot_price_sq_ft = update_venture.plot_price_sq_ft
    venture.road_width = update_venture.road_width
    venture.no_of_plots = update_venture.no_of_plots
    venture.no_of_gates = update_venture.no_of_gates
    venture.distance_info = update_venture.distance_info
    venture.venture_address = update_venture.venture_address
    venture.venture_state = update_venture.venture_state
    venture.venture_district = update_venture.venture_district
    venture.venture_city = update_venture.venture_city
    venture.venture_locality = update_venture.venture_locality
    venture.venture_description = update_venture.venture_description
    venture.venture_brochure = update_venture.venture_brochure
    venture.venture_layout = update_venture.venture_layout
    venture.venture_3d_layout = update_venture.venture_3d_layout
    venture.venture_video = update_venture.venture_video
    venture.venture_latitude = update_venture.venture_latitude
    venture.venture_longitude = update_venture.venture_longitude
    venture.is_rera_approved = update_venture.is_rera_approved
    venture.is_rera_registered = update_venture.is_rera_registered
    venture.approved_by = update_venture.approved_by
    venture.rero_no = update_venture.rero_no
    venture.tlp_no = update_venture.tlp_no
    venture.tsl_no = update_venture.tsl_no
    venture.is_blocked = update_venture.is_blocked
    venture.is_gated_community = update_venture.is_gated_community
    venture.is_popular = update_venture.is_popular
    venture.is_featured = update_venture.is_featured
    venture.featured_text = update_venture.featured_text
    venture.is_low_cost_land = update_venture.is_low_cost_land
    venture.venture_featured = update_venture.venture_featured
    venture.company = update_venture.company
    venture.land_status = update_venture.land_status
    venture.drone_approach_videos = update_venture.drone_approach_videos
    venture.drone_aerial_view = update_venture.drone_aerial_view
    venture.close_up = update_venture.close_up
    venture.status = update_venture.status
    venture.created_date = update_venture.created_date
    venture.created_by = update_venture.created_by

    db.commit()
    db.refresh(venture)
    return venture


def delete_venture(db:Session,venture_id:int):
    venture = db.query(Venture).filter(Venture.id == venture_id).first()
    if not venture:
        return None
    db.delete(venture)
    db.commit()
    return{"message":"Venture Successfully Deleted"}


