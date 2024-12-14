import markdown
import sys

# memo: [python3 markdown_to_HTML.py markdown inputfile outputfile]
def validate():
    print(f"arg:{sys.argv}")
    match sys.argv[1]:
        case "markdown":
            if len(sys.argv) == 4:
                convert_markdown()

            else:
                errorMessage("Incorrect number of arguments. markdown is 4")
            
def errorMessage(error_message):
    raise ValueError(f"error:{error_message}")

def convert_markdown():
    inpoutfile = sys.argv[2]
    outputfile = sys.argv[3]
    try:
        with open(inpoutfile, 'r') as f:
            markdown_text = f.read()

        html_text = markdown.markdown(markdown_text)

        with open (outputfile, 'w') as f:
            f.write(html_text)
        
    except Exception as e:
        print(f"An error ocurred: {e}")

if __name__=="__main__":
    validate()
