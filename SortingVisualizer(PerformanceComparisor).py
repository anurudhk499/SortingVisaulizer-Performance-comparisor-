import matplotlib.pyplot as plt
import time
import random
from rich.console import Console
from rich import print

console = Console()


def get_user_input():
    size = int(input("Enter the size of the array: "))
    print("Choose an option:")
    print("1. Enter your own array elements")
    print("2. Generate a random array")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Enter {size} elements separated by spaces:")
        user_input = input().strip()
        array = list(map(int, user_input.split()))
        if len(array) != size:
            print(f"Error: Expected {size} elements, but got {len(array)}. Using random array instead.")
            array = [random.randint(1, 100) for _ in range(size)]
    elif choice == 2:
        array = [random.randint(1, 100) for _ in range(size)]
    else:
        print("Invalid choice! Generating a random array.")
        array = [random.randint(1, 100) for _ in range(size)]

    return array


def visualize(array, highlight1=None, highlight2=None, title="Sorting Visualizer"):
    plt.clf() 
    colors = ['black'] * len(array)
    if highlight1 is not None:
        colors[highlight1] = 'yellow'
    if highlight2 is not None:
        colors[highlight2] = 'yellow'
    plt.bar(range(len(array)), array, color=colors)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.5)  

 
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
            
                array[j], array[j + 1] = array[j + 1], array[j]
                visualize(array, j, j + 1, "Bubble Sort")
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]
       
        visualize(array, i, min_index, "Selection Sort")
    return array


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        
        visualize(array, j + 1, i, "Insertion Sort")
    return array


def quick_sort(array, low, high):
    if low < high:
       
        pi = partition(array, low, high)
       
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
           
            visualize(array, i, j, "Quick Sort")
    array[i + 1], array[high] = array[high], array[i + 1]
    visualize(array, i + 1, high, "Quick Sort")
    return i + 1


def measure_sorting_time(sort_function, array, *args):
    
    start_time = time.time()
    sorted_array = sort_function(array, *args) if args else sort_function(array)
    end_time = time.time()
    return sorted_array, end_time - start_time


def display_sorted_array(sorted_array, algorithm_name):
  
    print(f"\n[bold magenta]Sorted Array using {algorithm_name}:[/bold magenta]")
    print(f"[bold green]{' '.join(map(str, sorted_array))}[/bold green]")


def main():
    array = get_user_input()
    print("\nOriginal Array:", array)
    plt.ion() 
    visualize(array, title="Initial Array")
    time.sleep(0.1)  
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": lambda arr: quick_sort(arr, 0, len(arr) - 1)
    }

    performance_results = {}
    for name, algorithm in sorting_algorithms.items():
        print(f"\nRunning {name}...")
        array_copy = array.copy() 
        sorted_array, time_taken = measure_sorting_time(algorithm, array_copy)
        performance_results[name] = time_taken
        print(f"{name} completed in {time_taken:.6f} seconds.")
        display_sorted_array(sorted_array, name)  
        visualize(sorted_array, title=f"{name} (Sorted)")

    print("\n[bold cyan]Performance Comparison:[/bold cyan]")
    for name, time_taken in performance_results.items():
        print(f"{name}: [bold yellow]{time_taken:.6f}[/bold yellow] seconds")

    plt.figure()
    plt.bar(performance_results.keys(), performance_results.values(), color='blue')
    plt.title("Sorting Algorithm Performance Comparison")
    plt.xlabel("Sorting Algorithm")
    plt.ylabel("Time Taken (seconds)")
    plt.show(block=True)  

if __name__ == "__main__":
    main()