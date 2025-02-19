from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class VentureCreate(BaseModel):
    id: Optional[int] = None
    venture_name: Optional[str] = ""
    email: Optional[str] = ""
    phone: Optional[str] = ""
    venture_type: Optional[str] = ""
    venture_status: Optional[int]
    venture_facing: Optional[str] = ""
    corner_facing: Optional[str] = ""
    venture_length: Optional[int] = 0
    venture_breadth: Optional[int] = 0
    plot_area: Optional[str] = ""
    plot_area_unit: Optional[str] = ""
    total_venture_area: Optional[str] = ""
    least_plot_price: Optional[str] = ""
    plot_price_sq_ft: Optional[str] = ""
    road_width: Optional[str] = ""
    no_of_plots: Optional[int] = 0
    no_of_gates: Optional[int] = 0
    distance_info: Optional[str] = ""
    venture_address: Optional[str] = ""
    venture_state: Optional[str] = ""
    venture_district: Optional[str] = ""
    venture_city: Optional[str] = ""
    venture_locality: Optional[str] = ""
    venture_description: Optional[str] = ""
    company_id: Optional[int] = None
    land_status: Optional[int] = 0
    status: int
    created_by_id: int
    updated_by_id: Optional[int]


class VentureResponse(VentureCreate):
    id: int

    class Config:
        from_attributes = True

