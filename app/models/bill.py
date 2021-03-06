from app import db
from datetime import datetime
import pytz
timezone = pytz.timezone("Asia/Kolkata")

class Bill(db.Model):
    """
        A class to represent a bill
        ....

        Attributes
        ----------
        amount: int
            amount to be paid

        paymentID: string
            paymentID of the payment made by the customer

        Member Functions:
        ----------------
        __repr__(): str
            returns the string representation of an object of the class

    """
    ################################# ORM #################################
    __tablename__ = "bill"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, index=True, nullable=False)
    invoice = db.Column(db.String(256))
    branchID = db.Column(db.Integer, db.ForeignKey('office.id'), index=True)
    time = db.Column(db.DateTime, index=True)
    #######################################################################

    def __init__(self, **kwargs) -> None:
        """
            The constructor of the Bill class
            ....

            Parameters:
                amount: int
                    amount to be paid
                paymentID: string
                    paymentID of the payment made by the customer

        """
        super().__init__(**kwargs)
        self.time = timezone.localize(datetime.now())

    def __repr__(self) -> str:
        """
            The function to get the string representation of the bill
            ....

            Returns:
                str
        """
        return f'<Bill: {self.amount}, Invoice: {self.invoice}>'
