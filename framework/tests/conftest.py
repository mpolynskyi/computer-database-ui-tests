import pytest
from dataclasses import dataclass
from typing import Optional


@dataclass
class ComputerItem:
    id: int
    computer_name: str
    introduced: Optional[str] = None
    discontinued: Optional[str] = None
    company: Optional[str] = None


@pytest.fixture(scope="session")
def computer_505_with_new_data():
    computer_505 = ComputerItem(id=505,
                                computer_name="new 505 name",
                                introduced="1955-02-03",
                                discontinued="1999-02-04",
                                company="Nokia")
    return computer_505


@pytest.fixture(scope="session")
def computer_506_to_delete():
    computer_506 = ComputerItem(id=506, computer_name="IBM 305")
    return computer_506


@pytest.fixture(scope="session", autouse=True)
def asci_white_filter_computer():
    asci_white_computer = ComputerItem(id=311,
                                       computer_name="ASCI White",
                                       introduced="01 Jan 2001",
                                       discontinued="01 Jan 2006",
                                       company="IBM")
    return asci_white_computer


@pytest.fixture(scope="session", autouse=True)
def spectrum_2a_filter_computer():
    spectrum_2a = ComputerItem(id=328,
                               computer_name="ZX Spectrum +2A",
                               introduced="01 Jan 1987",
                               company="Amstrad")
    return spectrum_2a
