#Necessario definir a classe dos tokens, que contem as seguintes informações sobre o token
#tipo, lexema, valor literal e linha
class Token:

    def __init__(self, tipo, lexema, literal, linha):
        self.tipo = tipo
        self.lexema = lexema
        self.literal = literal
        self.linha = linha

    def __str__(self):
        return str(self.tipo)+" "+str(self.lexema)+" "+str(self.linha)

#classe do Scanner, que sera usado para percorrer a entrada e pegar todos os tokens existentes
#string = o codigo fonte bruto que sera lido, listaTokens = uma lista que será preenchida com os
#tokens encontrados, comeco e atual são posições dos caracteres presentes nos lexemas sendo analisados
class Scanner(object):

    def __init__(self, string):
        self.string = string
        self.listaTokens = []
        self.comeco = 0
        self.atual = 0
        self.linha = 1

    #final eh uma função que nos diz se todos os caracteres do lexema já foram checados
    def final(self):
        return self.atual >= len(self.string)

    def scanTokens(self):
        while(not self.final()):
            self.comeco = self.atual
            self.scanToken()            

        self.palavrasReservadas()
        return self.listaTokens        

    #funcao responsável por reconhecer lexemas
    def scanToken(self):
        c = self.avancar()
        #lexemas simples
        if c == '(':
            self.addToken("PAREN_ESQ")
        elif c == ')':
            self.addToken("PAREN_DIR")
        elif c == '{':
            self.addToken("CHAVE_ESQ")
        elif c == '}':
            self.addToken("CHAVE_DIR")
        elif c == ',':
            self.addToken("VIRGULA")
        elif c == '.':
            self.addToken("PONTOFINAL")
        elif c == '-':
            self.addToken("MENOS")
        elif c == '+':
            self.addToken("MAIS")
        elif c == ':':
            if self.match('='):
                self.addToken("ATRIBUICAO")
            else:
                self.addToken("DECLARACAO")
        elif c == ';':
            self.addToken("PONTOVIRGULA")
        elif c == '*':
            self.addToken("MULTIPLICACAO")
        #lexemas de comparação
        elif c == '!':
            if self.match('='):
                self.addToken("DIFERENTE")
            else:
                self.addToken("NEGACAO")
        elif c == '=':
            if self.match('='):
                self.addToken("COMPARADORIGUAL")
        elif c == '<':
               if self.match('='):
                   self.addToken("MENORIGUAL")
               else:
                    self.addToken("MENORQUE")
        elif c == '>':
            if self.match('='):
                self.addToken("MAIORIGUAL")
            else:
                self.addToken("MAIORQUE")
        #lexemas que devem ser pulados
        elif c == ' ':
            None
        elif c == '\r':
            None
        elif c == '\t':
            None
        elif c == '\n':
            self.linha = self.linha + 1   

        else:
            #literais numericos
            if self.digito(c):
                self.numero()
            elif self.alfa(c):
                self.identificador()
            else:
                print("Erro na linha", self.linha, "Caractere", c, "invalido")
                raise Exception()

    #Lista com todas as palavras reservadas, esta funcao checa todos os tokens
    #adicionados como IDENTIFICADOR para ver se eles são na verdade palavras
    #reservadas da linguagem
    def palavrasReservadas(self):
        for k in self.listaTokens:
            if k.tipo == "IDENTIFICADOR":
                if k.lexema == "programa":
                    k.tipo = k.lexema.upper()
                if k.lexema == "var":
                    k.tipo = k.lexema.upper()
                if k.lexema == "inteiro":
                    k.tipo = k.lexema.upper()
                if k.lexema == "booleano":
                    k.tipo = k.lexema.upper()
                if k.lexema == "procedimento":
                    k.tipo = k.lexema.upper()
                if k.lexema == "funcao":
                    k.tipo = k.lexema.upper()
                if k.lexema == "inicio":
                    k.tipo = k.lexema.upper()
                if k.lexema == "fim":
                    k.tipo = k.lexema.upper()
                if k.lexema == "se":
                    k.tipo = k.lexema.upper()
                if k.lexema == "entao":
                    k.tipo = k.lexema.upper()
                if k.lexema == "senao":
                    k.tipo = k.lexema.upper()
                if k.lexema == "enquanto":
                    k.tipo = k.lexema.upper()
                if k.lexema == "faca":
                    k.tipo = k.lexema.upper()
                if k.lexema == "leia":
                    k.tipo = k.lexema.upper()
                if k.lexema == "escreva":
                    k.tipo = k.lexema.upper()
                if k.lexema == "ou":
                    k.tipo = k.lexema.upper()
                if k.lexema == "div":
                    k.tipo = k.lexema.upper()
                if k.lexema == "e":
                    k.tipo = k.lexema.upper()
                if k.lexema == "verdadeiro" or k.lexema == "falso" or k.lexema == "nao":
                    k.tipo = "BOOLEANO"

    #Funcão responsável por adicionar os tokens de tipo IDENTIFICADOR, checando se
    #eles são construidos de forma alfanumerica
    def identificador(self):
        while self.alfaNum(self.olhar()):
            self.avancar()
        self.addToken("IDENTIFICADOR",str(self.string[self.comeco:self.atual]))

    def alfaNum(self, c):
        return self.alfa(c) or self.digito(c)

    def alfa(self,c):
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

    def numero(self):
        while self.digito(self.olhar()):
            self.avancar()
        self.addToken("NUMERO: ",int(self.string[self.comeco:self.atual]))            

    def digito(self,c):
        return c >= '0' and c <= '9'

    def olhar(self):
        if self.final():
            return '\0'
        return self.string[self.atual]

    def match(self, esperado):
        if self.final():
            return False
        elif self.string[self.atual] != esperado:
            return False

        self.atual = self.atual + 1
        return True

    def avancar(self):
        self.atual = self.atual + 1
        return self.string[self.atual - 1]

    #Função que adiciona os tokens na lista de Tokens da classe Scanner
    def addToken(self, tipo, literal = None):
        literal = None
        string2 = self.string[self.comeco:self.atual]
        self.listaTokens.append(Token(tipo,string2,literal,self.linha))

#================== main temporário ==================
sentinel = ''
programa = '\n'.join(iter(input, sentinel))
scan = Scanner(programa)
tokens = scan.scanTokens()
for linha in tokens:
    print(linha)
    
