# 1source-python
Demonstration code which accesses the 1Source REST API in a command-line Python program

## Description

This project provides sample code and a template for accessing the 1Source REST API in [Python](https://www.python.org/). The code runs as a command-line program which utilizes switch to exercise the various API endpoints.

To view sample code in Java and JavaScript, please see the following GitHub repository:

https://github.com/Equilend/1source-api

To view sample code in C++, please see the following GitHub repository:

https://github.com/dharm-kapadia/1source-c++

To view sample code in Go, please see the following GitHub repository:

https://github.com/dharm-kapadia/1source-python


## Getting Started

### Dependencies

* Download and install [Anaconda](https://www.anaconda.com/download) or [Miniconda] (https://docs.conda.io/projects/miniconda/en/latest/index.html) packages 

### Installing

Clone the code repository locally from GitHub with the following command:
```
> git clone https://github.com/dharm-kapadia/1source-python
> cd 1source-python
```

Create and activate the Conda enviroment for 1source-python:

```
1source-python>  conda create --name 1source-python python=3.11
1source-python>  conda activate 1source-python

```

Install the required 3rd-party Python packages into the created conda environment by entering the following command:

```
(1source-python) 1source-python> pip install -r requirements.txt

```

  ### Executing program

The 1source-python application can be run directly from the command line in the terminal after it is successfully built. The following comman will run the application:

```
1source-python> ./1source-python
```

The output of that will show the command line options available:

```
1source-python> ./1source-python
-t: required.
Usage: 1Source [--help] [--version] -t VAR [-g VAR] [-a agreement_id] [-e events] [-c contract_id] [-p party_id] [-i JSON]
Note: -t is required

Optional arguments:
  -h, --help     shows help message and exits
  -v, --version  prints version information and exits

  -t             1Source configuration TOML file [required]
  -g             1Source API Endpoint to query [agreements, contracts, events, parties, returns, rerates, recalls, buyins]
  -a             1Source API Endpoint to query trade agreements by agreement_id
  -e             1Source API Endpoint to query events by event_id
  -c             1Source API Endpoint to query contracts by contract_id
  -p             1Source API Endpoint to query parties by party_id

  -cp            1Source API Endpoint to PROPOSE a contract from a JSON file
  -cc            1Source API Endpoint to CANCEL a proposed contract by contract_id
  -ca            1Source API Endpoint to APPROVE a proposed contract by contract_id
  -cd            1Source API Endpoint to DECLINE a proposed contract by contract_id
```

The '-t' command line parameter specifies the application TOML configuration file and is required, even if no other command line parameters are included.

The default TOML configuration file is called 'configuration.toml' and is included in the repository.

```
1source-python> ./1source -t configuration.toml

```

The 1Source REST API can return the following entities:
* events
* parties
* agreements
* contracts
* rerates
* returns
* recalls
* buyins

#### Events
To retrieve all events which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -g events
```

The output of the command to retrieve events will be a JSON response from the 1Source REST API similar to:
```
1Source events
==============
[
  {
    "eventDateTime": "2023-11-02T13:42:16.049Z",
    "eventId": 10012358,
    "eventType": "TRADE",
    "resourceUri": "/v1/ledger/agreements/2cf9d8cc-2b77-49bf-8bb2-9956aaf9cf97"
  },

  .
  .
  .

  {
    "eventDateTime": "2023-11-02T11:00:05.436Z",
    "eventId": 10012335,
    "eventType": "TRADE",
    "resourceUri": "/v1/ledger/agreements/ed0b656e-6931-4b85-b5be-1bbe6b71b099"
  }
]
```

The REST API can be queried for a particular event with an event_id
```
1source-python> ./1source -t configuration.toml -e 10012349
```

The expected response for that call would be similar to:
```
1Source event
=============
{
  "eventDateTime": "2023-11-02T11:00:11.448Z",
  "eventId": 10012349,
  "eventType": "TRADE",
  "resourceUri": "/v1/ledger/agreements/d7f0cf8d-2c8f-4741-bf4c-3e793b67a0ee"
}
```

#### Parties
Similar to the Events call, to retrieve all parties which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -g parties
```

The REST API can be queried for a particular party with a party_id
```
1source-python> ./1source -t configuration.toml -p XXXX-US
```

#### Agreements
Similar to the Events call, to retrieve all agreements which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -o agreements
```

The REST API can be queried for a particular agreement with an agreement_id
```
1source-python> ./1source -t configuration.toml -a 56e7a7fb-309b-4f49-b92f-b789b37e3f07
```

#### Contracts
Similar to the Events call, to retrieve all contracts which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -g contracts
```

The REST API can be queried for a particular contract with a contract_id
```
1source-python> ./1source -t configuration.toml -c c2098d72-89c0-49f7-829a-e9
```

#### Rerates
Similar to the Events call, to retrieve all rerates which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -g rerates
```

#### Returns
Similar to the Events call, to retrieve all returns which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -g returns
```

#### Recalls
Similar to the Events call, to retrieve all recalls which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -g recalls
```

#### Buyins
Similar to the Events call, to retrieve all buyins which the user is authorized to view, the following command will do so:

```
1source-python> ./1source -t configuration.toml -g buyins
```

### Proposing a Contract
The 1Source command line application supports proposing a new contract. The command to do that is:

```
1source-python> ./1source -t configuration.toml -cp <JSON contract file>
```
* The application will read in the data from the JSON file and post it to the 1Source API to directly create a new contract in a 'PROPOSED' state. 
* The project contains a sample JSON contract file called 'proposed_trade.json'.

### Canceling a Contract
The 1Source command line application supports canceling a proposed contract. The command to do that is:

```
1source-python> ./1source -t configuration.toml -cc <contract_id>
```
* The application will retrieve the contract and verify it is in a "PROPOSED" state before canceling.
* Only the original proposer of the contract can cancel it. The counterparty can decline the proposed contract instead.

### Approving a Contract
The 1Source command line application supports approving a proposed contract. The command to do that is:

```
1source-python> ./1source -t configuration.toml -ca <contract_id>
```
* The application will retrieve the contract and verify it is in a "PROPOSED" state before approving.
* Only the counterparty to the original proposer of the contract can approve it. The original contract proposer can cancel it instead.

### Declining a Contract
The 1Source command line application supports decling a proposed contract. The command to do that is:

```
1source-python> ./1source -t configuration.toml -cd <contract_id>
```
* The application will retrieve the contract and verify it is in a "PROPOSED" state before declining.
* Only the counterparty to the original proposer of the contract can decline it. The original contract proposer can cancel it instead.

### Notes
* The 1Source command line application logs output to a file called '1source-python.log'.
* The name of the output log file can be changed in the source, which will require the program to be recompiled as detailed above.

### Configuration TOML Specification
The 1source command-line application reads data from a configuration file in TOML format. The file contains information required for the application to connect to the 1Source REST API, the individual endpoints, and the authentication details. The TOML file reflects that by have 3 required sections
* general
* endpoints
* authentication

Of the 3 sections, only a few of the attributes in the authentication section should be changed by the user. The rest should be left as-is unless otherwise instructed.

#### General

This section contains details of the 1Source REST API "auth_url" and realm This endpoint is for user login authentication and retrieval of the auth token on successful login. That auth token is required on subsequent calls to the 1Source REST API.

These values should not be changed by the user unless otherwise instructed.

#### Endpoints
This section contains key/value pairs related to the 1Source REST API endpoints for events, parties, agreements, and contracts. These values should not be changed by the user unless otherwise instructed.

#### Authentication
This section contains key/value pairs related to the 1Source REST API login authentication (username, password, etc.)

## Authors

Contributors names and contact info

[@Dharm Kapadia](dharm.kapadia@equilend.com)

## Version History

* 0.1
    * Initial Release
* 0.2
    * Refactor code
    * Add support for rerates, returns, recalls, buyins

## Acknowledgments

