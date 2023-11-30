# -*- coding: utf-8 -*-

"""
    <To Do>
    
    The program will log output to a log file called '1source-pyton.log'
"""

__author__ = "Dharm Kapadia"
__copyright__ = "© 2023 EquiLend"
__version__ = "1.0.0"
__email__ = "dharm.kapadia@equilend.com"


import argparse
import logging
from rich.pretty import pprint

from net.query_by_id import get_by_id
from utils.logger import configure_logging
from utils.app_config import app_conf
from net.auth import get_auth_token
from net.entities import get_entity

# Create file specific logger
logger: logging.Logger = configure_logging(logging, app_conf.log_file, app_conf.log_format, "main")


def print_output(data_type: str, data: str) -> None:
    """
        Print output of received data
    """
    pprint(f"1Source {data_type} for {app_conf.username}:")
    pprint(data)


def main():
    """
        Start of the application
    :return:
    """

    parser = argparse.ArgumentParser(description='1Source Python command line example')
    parser.add_argument(
        '-g',
        metavar='<Entity to query>',
        help='1Source API Endpoint to query',
        required=False,
        choices=[
            'agreements',
            'contracts',
            'events',
            'parties',
            'returns',
            'rerates',
            'recalls',
            'delegations',
            'buyins'])

    parser.add_argument(
        '-a',
        metavar='<Trade Agreement Id>',
        required=False,
        help='1Source API Endpoint to query Trade Agreements by agreement_id')

    parser.add_argument(
        '-e',
        metavar='<Event Id>',
        required=False,
        help='1Source API Endpoint to query Events by event_id')

    parser.add_argument(
        '-c',
        metavar='<Contract Id>',
        required=False,
        help='1Source API Endpoint to query Contracts by contract_id')

    parser.add_argument(
        '-ch',
        metavar='<Contract Id>',
        required=False,
        help='1Source API Endpoint to query Contract History by contract_id')

    parser.add_argument(
        '-p',
        metavar='<Party Id>',
        required=False,
        help='1Source API Endpoint to query Parties by party_id')

    # Parse command line arguments
    args = parser.parse_args()
    vargs: dict = vars(args)

    token: str = get_auth_token()

    if "g" in vargs and vargs["g"] is not None:
        entity = vargs["g"]

        match entity:
            case "agreements":
                if token:
                    # Got an auth token, call the agreements endpoint to get the data
                    data = get_entity(app_conf.agreements, token)
                    print_output("Trade Agreements", data)

            case "contracts":
                if token:
                    # Got an auth token, call the contracts endpoint to get the data
                    data = get_entity(app_conf.contracts, token)
                    print_output("Contracts", data)

            case "events":
                # Got an auth token, call the events endpoint to get the data
                data = get_entity(app_conf.events, token)
                print_output("Events", data)

            case "parties":
                if token:
                    # Got an auth token, call the parties endpoint go get the data
                    data = get_entity(app_conf.parties, token)
                    print_output("Parties", data)

            case "returns":
                if token:
                    # Got an auth token, call the returns endpoint go get the data
                    data = get_entity(app_conf.returns, token)
                    print_output("Returns", data)

            case "recalls":
                if token:
                    # Got an auth token, call the recalls endpoint go get the data
                    data = get_entity(app_conf.recalls, token)
                    print_output("Recalls", data)

            case "rerates":
                if token:
                    # Got an auth token, call the rerates endpoint go get the data
                    data = get_entity(app_conf.rerates, token)
                    print_output("Rerates", data)

            case "delegations":
                if token:
                    # Got an auth token, call the delegations endpoint go get the data
                    data = get_entity(app_conf.delegations, token)
                    print_output("Delegations", data)

            case "buyins":
                if token:
                    # Got an auth token, call the buyins endpoint go get the data
                    data = get_entity(app_conf.buyins, token)
                    print_output("Buyins", data)

            case _:
                logger.error(f"Unsupported 1Source endpoint '{entity}'")
                pprint(f"Unsupported 1Source endpoint '{entity}'")
                exit(1)
        exit(0)

    if "a" in vargs and vargs["a"] is not None:
        entity_id: str = vargs["a"]
        data = get_by_id(app_conf.agreements, entity_id, token)
        if data:
            print_output("Trade Agreement", data)
        exit(0)

    if "e" in vargs and vargs["e"] is not None:
        entity_id: str = vargs["e"]
        data = get_by_id(app_conf.events, entity_id, token)
        if data:
            print_output("Event", data)
        exit(0)

    if "c" in vargs and vargs["c"] is not None:
        entity_id: str = vargs["c"]
        data = get_by_id(app_conf.contracts, entity_id, token)
        if data:
            print_output("Contract", data)
        exit(0)

    if "ch" in vargs and vargs["ch"] is not None:
        entity_id: str = vargs["ch"]
        data = get_by_id(app_conf.contracts, entity_id, token, True)
        if data:
            print_output("Contract History", data)
        exit(0)

    if "p" in vargs and vargs["p"] is not None:
        entity_id: str = vargs["p"]
        data = get_by_id(app_conf.parties, entity_id, token)
        if data:
            print_output("Party", data)
        exit(0)


if __name__ == "__main__":
    main()
