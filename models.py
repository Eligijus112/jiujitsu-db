from sqlalchemy import Column, DateTime, Integer, func, ForeignKey, Float  
from sqlalchemy.ext.declarative import declarative_base

# PSQL specific types
from sqlalchemy.dialects.postgresql import VARCHAR, BOOLEAN

# Create a base class for the models
Base = declarative_base()

class Users(Base):  
    # Setting the table name 
    __tablename__ = 'users'

    # The autoincremented primaty key 
    id = Column(Integer, primary_key=True, autoincrement=True)

    # User related information 
    name = Column(VARCHAR, nullable=False)
    surname = Column(VARCHAR, nullable=False)
    email = Column(VARCHAR, nullable=False)

    # Password field
    password = Column(VARCHAR, nullable=False)

    # Boolean for beeing an admin
    is_admin = Column(BOOLEAN, nullable=False, default=False)

    # Boolean for activity
    is_active = Column(BOOLEAN, nullable=False, default=True)

    # Image path of the user 
    image_path = Column(VARCHAR, nullable=True)

    # Creation an update times 
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"""
            User id: {self.id}, 
            name: {self.name}, 
            surname: {self.surname}, 
            email: {self.email}, 
            is_admin: {self.is_admin}, 
            is_active: {self.is_active}, 
            image_path: {self.image_path},
            created_at: {self.created_at}, 
            updated_at: {self.updated_at}
        """

class UserRanks(Base):
    # Setting up the tablename 
    __tablename__ = 'user_ranks'

    # The autoincremented primary key
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Foreign key for the user id
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # The rankname (belt color)
    rank_name = Column(VARCHAR, nullable=False)

    # Stripe count 
    stripe_count = Column(Integer, nullable=False)

    # Creation an update times 
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())