#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://charlesleifer.com/blog/querying-tree-structures-in-sqlite-using-python-and-the-transitive-closure-extension/
"""


import os
import sys

from peewee import (
    Model,
    CharField,
    ForeignKeyField,
)

from playhouse.sqlite_ext import (
    SqliteExtDatabase,
    ClosureTable,
)


src_root = os.path.realpath(os.path.dirname(__file__))
app_root = os.path.realpath(os.path.dirname(src_root))


db = SqliteExtDatabase(os.path.join(src_root, 'test_peewee_sqlite_closure.db'))
db.load_extension(os.path.join(app_root, 'bin/sqlite/closure'))  # Note we do not include the ".so".


class Category(Model):
    name = CharField()
    parent = ForeignKeyField('self', null=True, related_name='children')

    class Meta:
        database = db


CategoryClosure = ClosureTable(Category)


if __name__ == '__main__':
    # Create the tables if they do not exist already.
    Category.create_table(True)
    CategoryClosure.create_table(True)

    books = Category.create(name='Books')
    fiction = Category.create(name='Fiction', parent=books)
    Category.create(name='Sci-fi', parent=fiction)
    Category.create(name='Westerns', parent=fiction)
    Category.create(name='Non-fiction', parent=books)

    # afficher tout les enfants de books
    print("## Books all descendants 1:")
    # Using a join query :
    all_descendants = (Category
        .select()
        .join(
            CategoryClosure,
            on=(Category.id == CategoryClosure.id)
        )
        .where(CategoryClosure.root == books)
    )
    for d in all_descendants:
        print(d.name)

    # Using a subquery instead a join query :
    # "<<" translates to "IN".
    print("## Books all descendants 2:")
    subquery = (CategoryClosure
        .select(CategoryClosure.id)
        .where(CategoryClosure.root == books)
    )
    all_descendants = Category.select().where(
        Category.id << subquery
    )
    for d in all_descendants:
        print(d.name)

    # Using the helper method :
    print("## Books all descendants 3:")
    all_descendants = CategoryClosure.descendants(
        books, include_node=True
    )
    for d in all_descendants:
        print(d.name)

    # afficher uniquement les enfants de books
    # Using a join query :
    print("## Books descendants only 1:")
    descendants = (Category
        .select()
        .join(
            CategoryClosure,
            on=(Category.id == CategoryClosure.id)
        )
        .where(
            (CategoryClosure.root == books) &
            (CategoryClosure.depth > 0)
        )
    )
    for d in descendants:
        print(d.name)

    print("## Books descendants only 2:")
    descendants = CategoryClosure.descendants(books, include_node=False)
    for d in descendants:
        print(d.name)

    # afficher les descendants direct
    # We can use just the Category table in this case.
    print("## Books direct descendants 1:")
    direct_descendants = Category.select().where(
        Category.parent == books
    )
    for d in direct_descendants:
        print(d.name)

    # We can join on the closure table.
    print("## Books direct descendants 2:")
    direct_descendants = (Category
        .select()
        .join(
            CategoryClosure,
            on=(Category.id == CategoryClosure.id)
        )
        .where(
            (CategoryClosure.root == books) &
            (CategoryClosure.depth == 1)
        )
    )
    for d in direct_descendants:
        print(d.name)

    # We can use a subquery.
    print("## Books direct descendants 3:")
    subquery = (CategoryClosure
        .select(CategoryClosure.id)
        .where(
            (CategoryClosure.root == books) &
            (CategoryClosure.depth == 1)
        )
    )
    direct_descendants = Category.select().where(
        Category.id << subquery
    )
    for d in direct_descendants:
        print(d.name)

    # Using helper method.
    print("## Books direct descendants 4:")
    direct_descendants = CategoryClosure.descendants(
        books, depth=1
    )
    for d in direct_descendants:
        print(d.name)
