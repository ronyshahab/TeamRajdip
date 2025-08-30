import hydro_agent


generate_data = hydro_agent.generate(input("Enter the place name: "))

with open("output.html", "w") as file:
        file.write(generate_data)
