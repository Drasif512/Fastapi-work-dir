from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.expression import text
# from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base




class Students(Base):
    __tablename__ = "Student"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)



    # content = Column(String, nullable=False)
    # published = Column(Boolean, server_default='TRUE', nullable=False)
    # created_at = Column(TIMESTAMP(timezone=True),
    #                     nullable=False, server_default=text('now()'))
    # owner_id = Column(Integer, ForeignKey(
    #     "users.id", ondelete="CASCADE"), nullable=False)

