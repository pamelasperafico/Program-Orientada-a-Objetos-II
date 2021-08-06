- HERANÇA: Esse requisito foi atendido nas classes cliente.py, que se utiliza da Pessoa na classe abstracao.py
	   Esse requisito também pode ser vizualidado na classe contas.py, que se utiliza da Conta da abstracao.py

- AGREGAÇÃO: Esse requisito foi atendido na classe contas.py, observando que a ContaCorrente e a ContaPoupanca se utilizam da Conta

- COMPOSIÇÃO: Esse requisito pode ser observado na classe banco.py self._agencias, self._clientes, self._contas

- REUSABILIDADE: O reúso é fator garantido devido a orientação a objetos. Assim, a herança é um recurso que permite reusabilidade por diferenciação.
		 A herança pode ser vista  na classe cliente.py, que utiliza-se do conceito de herança da classe abtsracao.py.
		 Assim, a alocação de arquivos em subpasta (como utilizado no projeto) é um indício de reusabilidade
		

- BIBLIOTECAS: Cada classe foi implementada de modo a organizar melhor o código, fazendo ou não parte do mesmo arquivo.
	       As classes geraram bibliotecas e essas podem ser reutilizadas e aprimoradas para uso em outras aplicações.
	       Um exemplo bem claro de biblioteca que foi utilizada no projeto foi a classe contas.py, que importa a classe Conta da abtsracao.py


- EXECUÇÃO DO CÓDIGO: Realizar o clone da pasta src e a partir dela executar o aquivo main.py.
		      A versão do Python utilizado para construção/compilação é a 3.8.5