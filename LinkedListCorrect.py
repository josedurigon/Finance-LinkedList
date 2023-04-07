import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from datetime import date


'''esse codigo que está correto!!!!! Se for fzer mudanças ou colocar coisas novas fazer no teste.py pelo amorrrrr de deus! Nao foi pro github ainda
    presta atenção
'''


# Estrutura do Node e Da lista ligada
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
#Função especial para poder fazer uma iteração na lista ligada
    def __iter__(self):
        self.current_node = self.head
        while self.current_node:
            yield self.current_node
            self.current_node = self.current_node.next
#Método especial usado juntamente do de cima. Esse retorna o proximo valor da sequencia de iteração até que o fluxo de codigo chegue no
# StopIteration. Sem isso nao tem como usar loop for na lista ligada.
    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        else:
            data = self.current_node.data
            self.current_node = self.current_node.next
            return data

# função para calcular as estatísticas so que adaptada para receber uma lista ligada
def calculate_statistics(linked_list):
    prices_list =[]
    current_node = linked_list.head

    while current_node is not None:
        prices_list.append(current_node.data)
        current_node = current_node.next

    mean = sum(prices_list) / len(prices_list)
    variance = np.var(prices_list)
    std_dev = np.std(prices_list)
    return mean, variance, std_dev

def plot_prices(linkedlist):

    prices_list = []

    current_node = linkedlist.head
    while current_node is not None:
        prices_list.append(current_node.data)
        current_node = current_node.next

    plt.plot(prices_list)
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.title(f'Stock Prices - {ticker}')
    plt.show()


# aplicação dos conceitos de lista ligada ao estudo de caso
tickers = ["^BVSP", "DAX", "BRL=X", "^SSMI","VALE3.SA", "LMT", "RTX"]
now = date.today()


for ticker in tickers:
    print(f"Getting data for {ticker}...")

    stock_data = yf.download(ticker, start="2012-01-01", end=now)

    stock_prices = LinkedList()

    for price in stock_data['Close']:
        stock_prices.append(price)

    mean, variance, std_dev = calculate_statistics(stock_prices)

    print(f"{ticker} statistics:")
    print(f"Mean: {mean:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard deviation: {std_dev:.2f}")

    plot_prices(stock_prices)
   
