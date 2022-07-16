# PythonLab

Repositorio de ejercicios hechos con Python 

## How to use?
1. To clone the repository using HTTPS, under "HTTPS", click "copy".

![ScreenShot](https://github.com/eddcf9/PythonLab/blob/master/OpenBootcamp/images/captura.png)

2. Open Terminal.

3. Change the current working directory to the location where you want to clone the directory.

4. Type `git clone`, and then paste the URL you copied earlier.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
## Note 

- **For _proper compilation of `.db`_ files, use the following commands in the terminal:**
```
$ sudo apt update
$ sudo apt install sqlite3
$ sqlite3 'midb.db'
sqlite> CREATE TABLE alumnos(
   id INT PRIMARY KEY,
   nombre TEXT NOT NULL,
   apellido TEXT NOT NULL
);
```
- If using VSC, install extension `SQLITE`
