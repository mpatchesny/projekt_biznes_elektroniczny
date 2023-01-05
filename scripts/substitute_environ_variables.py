import sys

env_path = sys.argv[1]

with open(env_path, "r") as f:
    variables = f.read().split("\n")
    for line in variables:
        if line.startswith("DB_NAME"):
            db_name = line.split("=")[1]
        if line.startswith("DOMAIN_NAME"):
            domain_name = line.split("=")[1]
        if line.startswith("HOST_HTTP="):
            host_http = line.split("=")[1]
        if line.startswith("HOST_HTTPS="):
            host_https = line.split("=")[1]

with open("../mysql/presta_db_config_template.sql", "r") as f:
    input = f.read()

input = input.replace(r"${DB_NAME}", db_name)
input = input.replace(r"${DOMAIN_NAME}", domain_name)
input = input.replace(r"${HOST_HTTP}", host_http)
input = input.replace(r"${HOST_HTTPS}", host_https)
print(input)

with open("../mysql/presta_db_config.sql", "w") as f:
    f.write(input)
