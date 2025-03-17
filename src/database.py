from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class BitcoinPreco(Base):
    __tablename__ = 'bitcoin_precos'
    
    id = Column(Integer, primary_key=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(10), nullable=False)
    moeda = Column(String(10), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"<BitcoinPreco(valor={self.valor}, criptomoeda='{self.criptomoeda}', moeda='{self.moeda}')>"


    
