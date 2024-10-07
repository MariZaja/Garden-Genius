# PostgreSQL Database

PostgreSQL is a powerful, open-source object-relational database system. It has a strong reputation for reliability, feature robustness, and performance. PostgreSQL supports both SQL (relational) and JSON (non-relational) querying, making it a versatile choice for various applications.

Key features include:
- ACID compliance
- Advanced indexing techniques
- Full-text search
- Support for various data types
- Extensible through custom functions and plugins

For more information, visit the [official PostgreSQL documentation](https://www.postgresql.org/docs/).

### `data.json` File Description

The `data.json` file contains the initial dataset used by the Garden Genius application. This file is structured in JSON format and includes various pieces of information necessary for the application's functionality.

### Running app

To run your Docker Compose services defined in `compose.yaml` in the background, you can use the `-d` flag, which stands for "detached" mode. This allows your services to run in the background without tying up your terminal.


Run the following command to start your services in detached mode:
    ```sh
    docker-compose up -d
    ```

To check the status of your running services, use:
    ```sh
    docker-compose ps
    ```

If you need to stop the services, you can run:
    ```sh
    docker-compose down
    ```

### Database Cleanup

The `./utils/deleteDB.sh` script can be used to delete the existing PostgreSQL database. This script is useful for resetting the database to a clean state, especially during development or testing.

To run the script, use the following command:
```sh
./utils/deleteDB.sh
```