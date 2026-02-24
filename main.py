import os
import sys
import time
import platform
import math
import tempfile
import psutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(" bencmark TEST utility️")

def system_info():
    print("\n sytem info")
    print(f"OS: {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"Processor: {platform.processor()}")
    print(f"Физических ядер CPU: {psutil.cpu_count(logical=False)}")
    print(f"Логических потоков CPU: {psutil.cpu_count(logical=True)}")
    ram = psutil.virtual_memory()
    print(f"RAM: {round(ram.total / (1024**3), 2)} ГБ")
    print("-" * 50)

def cpu_benchmark():
    print("\n CPU test (maths)...")
    start_time = time.time()
    
    # Синтетическая нагрузка: вычисление квадратных корней и факториалов
    score = 0
    for i in range(1, 5_000_000):
        score += math.sqrt(i)
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    # Высчитываем условные баллы
    points = int(10000 / elapsed)
    print(f" CPU test end {elapsed:.2f} sec.")
    print(f" result: {points} points")
    return points

def ram_benchmark():
    print("\nRAM test...")
    start_time = time.time()
    
    # Создаем большой массив данных (около 200 МБ) и манипулируем им
    data = bytearray(200 * 1024 * 1024)
    for i in range(0, len(data), 1024):
        data[i] = 255 # Запись
    
    _ = data[::2] # Чтение
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    points = int(5000 / elapsed)
    print(f" RAM test end {elapsed:.2f} sec.")
    print(f"  resultRAM: {points} point")
    return points

def disk_benchmark():
    print("\n testing the drive (Disk I/O)...")
    temp_file = os.path.join(tempfile.gettempdir(), "naparnik_test.tmp")
    data_chunk = b'01010101' * 1024 * 1024  # 8 MB chunk
    
    start_time = time.time()
    
    # Запись 160 МБ
    with open(temp_file, "wb") as f:
        for _ in range(20):
            f.write(data_chunk)
            
    # Чтение 160 МБ
    with open(temp_file, "rb") as f:
        _ = f.read()
        
    os.remove(temp_file)
    end_time = time.time()
    elapsed = end_time - start_time
    
    points = int(3000 / elapsed)
    print(f" Disk test end {elapsed:.2f} sec.")
    print(f"result Disk: {points} point")
    return points

def run_all_tests():
    sys_score = 0
    sys_score += cpu_benchmark()
    sys_score += ram_benchmark()
    sys_score += disk_benchmark()
    
    print(f" All result: {sys_score} points")

def main_menu():
    while True:
        clear_screen()
        print_header()
        system_info()
        print("Select action:")
        print("1. System test (CPU + RAM + Disk)")
        print("2. Processor test (CPU)")
        print("3. RAM test (RAM)")
        print("4. testing of disk (Disk)")
        print("0. exit")
        
        choice = input("\nchoose: ")
        
        if choice == '1':
            run_all_tests()
        elif choice == '2':
            cpu_benchmark()
        elif choice == '3':
            ram_benchmark()
        elif choice == '4':
            disk_benchmark()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Incorrect try again.")
            
        input("\nEnter  to countinue...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()
