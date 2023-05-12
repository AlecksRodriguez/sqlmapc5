import website_checker
import command_executor

def main():
    website_url = "https://c5jalisco.gob.mx/"

    if website_checker.check_website_connection(website_url):
        print("¡Conexión exitosa con el sitio web!")
        command_executor.execute_sqlmap_command()
    else:
        print("No se pudo establecer conexión con el sitio web.")

if __name__ == "__main__":
    main()
