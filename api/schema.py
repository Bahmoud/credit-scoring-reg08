from pydantic import BaseModel

class ClientData(BaseModel):
    
    # Scores externes
    EXT_SOURCE_1: float
    EXT_SOURCE_2: float
    EXT_SOURCE_3: float
    
    # Informations financières
    AMT_GOODS_PRICE: float
    AMT_ANNUITY: float
    AMT_CREDIT: float
    
    # Profil client
    DAYS_BIRTH: float
    DAYS_EMPLOYED: float
    DAYS_LAST_PHONE_CHANGE: float
    
    # Situation familiale
    NAME_FAMILY_STATUS_Married: int
    
    # Région
    REGION_RATING_CLIENT: float
    REGION_RATING_CLIENT_W_CITY: float
    
    # Documents
    FLAG_DOCUMENT_3: int
    DAYS_ID_PUBLISH: float
    
    # Profession
    OCCUPATION_TYPE_Laborers: int
