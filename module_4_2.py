# Namespace

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

# Функция inner_function() будет исполняться внутри функции test_function() во время ее запуска.
test_function()

# Однако, за пределами функции test_function(), функция inner_function() выполняться не будет, так как она находится в
# локальном пространстве имен функции.
inner_function()
