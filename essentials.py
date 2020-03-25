import platform
import subprocess
import sys
import os

# print(platform.platform())

def execCmd(cmd):
    try:
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return result
    
    except Exception:
        return 'Could not execute function'

    
def getPath():
    
    '''
        Sets path automatically if path is not assigned by the user
    '''
    if 'Windows' in platform.platform():
        try:
            result = execCmd('whoami')
            user = result.stdout.readline().decode('utf-8').split('\\')[1].strip()
            PATH = 'C:/Users/' + user + '/Documents/'
            with open('path.txt', 'r') as f:
                PATH = f.readline()
                f.close()
        
        except AttributeError:
            print(result)
        
        except FileNotFoundError:
            pass
        
        finally:
            return PATH

    else:
        try:
            result = execCmd('whoami')
            user = result.stdout.readline().decode('utf-8').strip()
            PATH = user + '/Documents/'
            with open('path.txt', 'r') as f:
                PATH = f.readline()
                f.close()
        
        except AttributeError:
            print(result)
        
        except FileNotFoundError:
            pass
        
        finally:
            return PATH


def createFolder(name):

    '''
        Creates the said folder in said directory
    '''
    try:
        # print(os.getcwd())
        create = execCmd(['mkdir', name])
        out = create.stdout.readline().decode('utf-8').strip()
        if 'cannot create dir' in out:
            raise ZeroDivisionError

    except Exception:
        out = 'Folder exists. Try another name.'

    finally:
        return out

def gitInit():
    try:
        result = execCmd(['git', 'init'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitAdd():
    try:
        result = execCmd(['git', 'add', '.'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)


def gitCommit():
    try:
        result = execCmd(['git', 'commit', '-m', '\"initial commit\"'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitPush():
    try:
        result = execCmd(['git', 'push', '-u', 'origin', 'master'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def openCode():
    try:
        # result = execCmd(['code', '.'])
        # out = result.stdout.readline().decode('utf-8').strip()
        # print(out)
        os.system('code .')

    except Exception:
        pass


if __name__ == "__main__":
    # print(sys.argv[1])
    os.chdir(getPath())
    name = sys.argv[-1]
    createFolder(name)
    os.chdir(name)
    gitInit()
    # print(name)
    openCode()
    