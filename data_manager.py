from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor, last_name):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE last_name = %(last_name)s
        ORDER BY first_name"""
    value = {'last_name': last_name}
    cursor.execute(query, value)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor, city_name):
    query = """
            SELECT first_name, last_name, city
            FROM mentor
            WHERE city = %(city)s
            ORDER BY first_name"""
    value = {'city': city_name}
    cursor.execute(query, value)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicants(cursor):
    query = """
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_name(cursor, first_name, last_name):
    query = """
                SELECT first_name, last_name, phone_number
                FROM applicant
                WHERE first_name = %(first_name)s or last_name = %(last_name)s
                ORDER BY first_name"""
    data = {'first_name': first_name, 'last_name': last_name}
    cursor.execute(query, data)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_email_ending(cursor, email):
    email = f"%{email}%"
    query = """
            SELECT first_name, last_name, phone_number
            FROM applicant
            WHERE email LIKE (%(email)s);"""
    data = {'email': email}
    cursor.execute(query, data)
    return cursor.fetchall()


@database_common.connection_handler
def update_phone_number(cursor, phone_number, application_code):
    query = """
                UPDATE applicant
                SET phone_number = %(phone_number)s
                WHERE application_code = %(application_code)s"""
    data = {'phone_number': phone_number, 'application_code': application_code}
    cursor.execute(query, data)


@database_common.connection_handler
def add_new_applicant(cursor, first_name, last_name, phone_number, email, application_code):
    query = f"""
                INSERT INTO applicant (first_name, last_name, phone_number, email, application_code)
                VALUES('{first_name}', '{last_name}', '{phone_number}', '{email}', '{application_code}');
                """
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant(cursor):
    pass