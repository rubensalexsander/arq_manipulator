def list_to_arq(lt):
    return [str(i)+'\n' for i in lt]   

class Arq_txt:
    def __init__(self, local_file):
        self.local_file = local_file
        self.get_lines()
    
    def connect(self, open_form='r'):
        try:
            arq = open(self.local_file, open_form)
            return arq
        except:
            print(f"Erro ao conectar em {self.local_file}")
            return None

    def desconnect(self, arq):
        arq.close()
    
    def find(self, content):
        self.get_lines()
        locais = []
        for line in self.lines:
            if content in line:
                locais.append(self.lines.index(line))
        return locais

    def get_lines(self, line="all"):
        arq = self.connect('r')
        self.lines = arq.readlines()
        self.desconnect(arq)
        if line != "all":
            return self.lines[line]
        return self.lines
    
    def rewrite_all(self, content=['']):
        arq = self.connect('w')
        arq.writelines(content)
        self.desconnect(arq)
    
    def rewrite_line(self, content='', line=-1):
        arq = self.connect()
        last_content = arq.readlines()
        if (len(last_content) - line) < 1:
            for i in range((len(last_content) - line)*-1+1):
                last_content.append('\n')      
        last_content[line] = content+'\n'
        new_content = last_content
        self.rewrite_all(new_content)
        self.desconnect(arq)

def main():
    while True:
        local = input("\nLocal: ")
        arqm = Arq_txt(local)

        while arqm:
            print(f"\n## Arq_manipulator: {local} ##\n\nc - Trocar arquivo\n0 - Ver arquivo\n1 - Alterar linha\n2 - Encontrar linha\n")
            resp = input("> ")
            if resp == "c":
                break

            if resp == "0":
                print("\n"+"-"*30)
                for line in arqm.get_lines(): print(line, end="")
                print("\n"+"-"*30+"\n")
            elif resp == "1":
                texto = input("\nTexto:\n> ")
                linha = int(input("\nLinha:\n> "))
                arqm.rewrite_line(content=texto, line=linha)
            elif resp == "2":
                texto = input("\nTexto:\n> ")
                print(f"\nOcorrências de {texto} no arquivo: "+str(arqm.find(content=texto)))

if __name__ == '__main__':
    main()
