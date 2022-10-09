def list_to_arq(lt):
    return [str(i)+'\n' for i in lt]   

class Arq_txt:
    def __init__(self, local_file, section_key=None):
        self.local_file = local_file
        self.get_lines()
    
    def connect(self, open_form='r'):
        try:
            self.arq = open(self.local_file, open_form)
        except:
            print(f"Erro ao conectar em {self.local_file}")
            return None

    def desconnect(self):
        self.arq.close()
    
    def find(self, content):
        self.get_lines()
        locais = []
        for line in self.lines:
            if content in line:
                locais.append(self.lines.index(line))
        return locais

    def get_lines(self, line="all"):
        self.connect()
        self.lines = self.arq.readlines()
        self.desconnect()
        if line != "all":
            return self.lines[line]
        return self.lines
    
    def rewrite_all(self, content=['']):
        self.connect('w')
        self.arq.writelines(content)
        self.desconnect()
    
    def rewrite_line(self, content='', line=-1):
        self.connect()
        last_content = self.arq.readlines()
        if (len(last_content) - line) < 1:
            for i in range((len(last_content) - line)*-1+1):
                last_content.append('\n')      
        last_content[line] = content+'\n'
        new_content = last_content
        self.desconnect()
        self.rewrite_all(new_content)

def main():
    while True:
        local = input("\nLocal: ")
        arqm = Arq_txt(local)

        while arqm:
            print(f"\n###### Arq_manipulator: {local} ######\n\nc - Trocar arquivo\n0 - Ver arquivo\n1 - Alterar linha\n2 - Encontrar linha\n")
            
            parts = input("> ").split()
            resp = parts[0]
            
            if len(parts) > 1:
                args1 = int(parts[1])
            else:
                args1 = None

            if resp == "c":
                break

            if resp == "0":
                print("\n"+"-"*30+'\n')
                for line in arqm.get_lines():
                    if not args1:
                        print(line, end="")
                    else:
                        print(arqm.get_lines()[(args1)])
                        break
                print("-"*30+"\n")

            elif resp == "1":
                texto = input("\nTexto:\n> ")
                linha = int(input("\nLinha:\n> "))
                arqm.rewrite_line(content=texto, line=linha)

            elif resp == "2":
                texto = input("\nTexto:\n> ")
                print(f'\nOcorrências de "{texto}" no arquivo: '+str(arqm.find(content=texto)))

if __name__ == '__main__':
    main()
