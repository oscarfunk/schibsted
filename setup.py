import pip

def install(package):
    pip.main(['install', package])


def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('nose')
install_and_import('selenium')
install('nose-html-reporting')
install('lxml')
install('werkzeug')