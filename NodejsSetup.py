import os , subprocess,time,sys

arguments = sys.argv[1:]

commands = [
    "npm init -y",
    "npm install express",
    "npm install nodemon",
    "touch index.js",
]

index_js_code = """
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send("hello world!");
});

app.listen(5050, () => {
  console.log("server listening on port 5050");
});
"""

package_json_code = """
{
  "name": "server",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \\"Error: no test specified\\" && exit 1",
    "dev": "nodemon index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "nodemon": "^3.0.1"
  }
}
"""

try:
    subprocess.run(f"mkdir {arguments[0]}", shell=True,check=True)

except subprocess.CalledProcessError as e:
    print(f"Error executing command creating folder: {e}")

os.chdir(arguments[0])

for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Command '{command}' executed successfully.")

        if(command == "touch index.js"):
            with open("index.js", "w") as file:
                file.write(index_js_code)
                file.close()
            with open("package.json",'w') as file:
                file.write(package_json_code)
                file.close()
        
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

print("successfully completed server setup.")