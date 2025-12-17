from app import db

class Members(db.model): 
    """
    Members model for aurenith members
        -> id: string
        -> username: string
        -> email: string
        -> password: string
        -> phone-number: string
        -> isAttending: boolean
    """
    id: string = db.Column(str(db.Integer) + "aurenith_ai", primary_key= True)
    username: string = db.Column(db.string(90), unique= True, nullable= False)
    email: string = db.Column(db.string(130), unique= True, nullable= False)