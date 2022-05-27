# airflow_base_RU
<h2> Установка Apache Airflow на Windows 10 и простые первые даги DAG's </h2>

Для установки airflow на windows 10 необходимо сначала установить подсистему Windows для Linux (Windows subsystem for Linux - WSL), т.к. airflow не поддерживает windows((

<h3> Шаг 1. </h3>

Изначально компонент WSL отключен. Чтобы его включить, вам необходимо зайти в <b> Пуск -> Панель управления -> Программы и компоненты -> Включение и отключение компонентов windows </b>, активировать галочку -> <b> Подсистема Windows для Linux (Windows Subsystem for Linux) </b>, нажать кнопку ОК, и перезагрузить компьютер.

<h3> Шаг 2. </h3>

Качаем и устанавливаем любой понравившийся дистрибьютив.

Все готово к началу установки.

<h3> Шаг 3. </h3>

Сама установка описана в официальной документации и разбита на следующие действия:
- сначала в командной строке вводим `wsl` для доступа к установленной подсистеме;
- затем непостредственно установка - `pip install apache-airflow`;
- если "по-хорошему" не прошло, то выполняем следующий набор команд для выбора и установки определенной версии:
  1. `export AIRFLOW_HOME=~/airflow`
  2. `source ~/.bashrc`
  3. `AIRFLOW_VERSION=2.2.3`
  4. `PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"`
  5. `CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"`
  6. `pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"`
  7. `export PATH=$PATH:~/.local/bin`
  8. `source ~/.bashrc`
- инициализация базы данных, по умолчанию sqlite - `airflow db init`;
- создание пользователя - `airflow users create \
                               --username admin \ 
                               --firstname Peter \
                               --lastname Parker \
                               --role Admin \
                               --email spiderman@superhero.org`
- запуск локального сервера - `airflow webserver --port 8080`
- запуск шедулера в новом окне - `airflow scheduler`

Если все сделано верно, то при посещении localhost:8080 и после ввода данных пользователя вам будут доступны для ознакомления с функциональностью стандартные даги, их уже можно покрутить/позапускать и посмотреть на результаты.

<h3> П.С. </h3>

По умолчанию создается домашняя папка AIRFLOW_HOME=~/airflow, ее можно сменить `export AIRFLOW_HOME='ваш путь'`. В папку airflow/dags необходимо будет поместить все ваши новые даги для последующей с ними работы.
Для того чтобы получить доступ к папкам подсистемы проделаем следующее `cmd -> wsl -> cd ~/ -> explorer.exe .`
