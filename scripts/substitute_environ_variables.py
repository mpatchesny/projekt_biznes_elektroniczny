with open("../config/local.env", "r") as f:
    variables = f.read().split("\n")
    for line in variables:
        if line.startswith("DB_NAME"):
            db_name = line.split("=")[1]
        if line.startswith("DOMAIN_NAME"):
            domain_name = line.split("=")[1]
        if line.startswith("LOCAL_HTTP"):
            local_http = line.split("=")[1]
        if line.startswith("LOCAL_HTTPS"):
            local_https = line.split("=")[1]

with open("../mysql/presta_db_config_template.sql", "r") as f:
    input = f.read()

input = input.replace(r"${DB_NAME}", db_name)
input = input.replace(r"${DOMAIN_NAME}", domain_name)
input = input.replace(r"${LOCAL_HTTP}", local_http)
input = input.replace(r"${LOCAL_HTTPS}", local_https)
print(input)

with open("../mysql/presta_db_config.sql", "w") as f:
    f.write(input)
