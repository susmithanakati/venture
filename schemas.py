from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime



class VentureCreate(BaseModel):
    id: Optional[int] = None
    venture_name: Optional[str] = ""
    email: Optional[EmailStr] = None
    phone: Optional[str] = ""
    venture_type: Optional[str] = ""
    venture_status: Optional[int] = None
    venture_facing: Optional[str] = ""
    venture_length: Optional[int] = 0
    venture_breadth: Optional[int] = 0
    plot_area: Optional[str] = ""
    no_of_plots: Optional[int] = 0
    no_of_gates: Optional[int] = 0
    distance_info: Optional[str] = ""
    venture_address: Optional[str] = ""
    venture_state_id: Optional[int] = None
    venture_district_id: Optional[int] = None
    venture_city_id: Optional[int] = None
    is_rera_approved: Optional[bool] = False
    is_rera_registered: Optional[bool] = False
    is_featured: Optional[bool] = False
    status: int = 0
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None


class VentureResponse(BaseModel):
    id: Optional[int]

    class Config:
        from_attributes = True
