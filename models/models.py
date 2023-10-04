# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

# create out db engibne
engine = create_engine("sqlite:///salesmanagement.db")

Base = declarative_base()
session=sessionmaker(bind=engine)()


# Association Table for Branches and Suppliers Many-to-Many Relationship
branch_supplier_association = Table(
    "branch_supplier_association",
    Base.metadata,
    Column("branch_id", Integer, ForeignKey("branches.id")),
    Column("supplier_id", Integer, ForeignKey("suppliers.id")),
)



class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    manager = Column(String)

    # Relationship to Supplier through association table
    suppliers = relationship("Supplier", secondary=branch_supplier_association, back_populates="branches")
   
    # Relationship to Customer
    customers = relationship("Customer", back_populates="branch")

    # crud methods
    # Create a new branch
    @classmethod
    def create(cls, name, location, manager):
        branch = cls(name=name, location=location, manager=manager)
        session.add(branch)
        session.commit()
        return branch

    # Retrieve a branch by ID
    @classmethod
    def get_by_id(cls, branch_id):
        return session.query(cls).filter_by(id=branch_id).first()

    # Update a branch's information
    def update(self, name=None, location=None, manager=None):
        if name:
            self.name = name
        if location:
            self.location = location
        if manager:
            self.manager = manager
        session.commit()

    # Delete a branch
    def delete(self):
        session.delete(self)
        session.commit()
     # Fetch suppliers associated with this branch
    def get_suppliers(self):
        return self.suppliers

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    contact_person = Column(String)

    # Relationship to Branch through association table
    branches = relationship("Branch", secondary=branch_supplier_association, back_populates="suppliers")

    # Create a new supplier
    @classmethod
    def create(cls, name, address, contact_person):
        supplier = cls(name=name, address=address, contact_person=contact_person)
        session.add(supplier)
        session.commit()
        return supplier

    # Retrieve a supplier by ID
    @classmethod
    def get_by_id(cls, supplier_id):
        return session.query(cls).filter_by(id=supplier_id).first()

    # Update a supplier's information
    def update(self, name=None, address=None, contact_person=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if contact_person:
            self.contact_person = contact_person
        session.commit()

    # Delete a supplier
    def delete(self):
        session.delete(self)
        session.commit()

    # Fetch branches associated with this supplier
    def get_branches(self):
        return self.branches

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    phone_number = Column(String)
    branch_id = Column(Integer, ForeignKey("branches.id"))

    # Relationship to Branch
    branch = relationship("Branch", back_populates="customers")

    # Create a new customer
    @classmethod
    def create(cls, name, email, phone_number, branch_id):
        customer = cls(name=name, email=email, phone_number=phone_number, branch_id=branch_id)
        session.add(customer)
        session.commit()
        return customer

    # Retrieve a customer by ID
    @classmethod
    def get_by_id(cls, customer_id):
        return session.query(cls).filter_by(id=customer_id).first()

    # Update a customer's information
    def update(self, name=None, email=None, phone_number=None, branch_id=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone_number:
            self.phone_number = phone_number
        if branch_id:
            self.branch_id = branch_id
        session.commit()

    # Delete a customer
    def delete(self):
        session.delete(self)
        session.commit()

    # Fetch branch information for this customer
    def get_branch_info(self):
        return self.branch
    


Base.metadata.create_all(engine)