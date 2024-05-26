# -*- coding: utf-8 -*-
"""Book models."""
from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database import Model


class Book(Model):
    """Book model."""

    __tablename__ = "book_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("author_table.id"), nullable=False
    )
    author: Mapped["Author"] = relationship(back_populates="books")
    genre: Mapped[str] = mapped_column(String(255))
    published_year: Mapped[str] = mapped_column(String(255))

    def __init__(self, title, author_id=None, genre=None, published_year=None):
        """
        Initialize a Book instance.

        :param title: The title of the book.
        :param author_id: The ID of the author (optional).
        :param genre: The genre of the book (optional).
        :param published_year: The year the book was published (optional).
        """
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.published_year = published_year

    def __repr__(self):
        """
        Return a string representation of the Book instance.

        :return: A string representation of the book.
        """
        return f"<Book {self.title}>"
