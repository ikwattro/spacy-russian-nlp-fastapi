# Russian NLP with Spacy

#### Installation

Clone this repository

```bash
git clone git@github.com/ikwattro/spacy-russian-nlp-fastapi
cd spacy-russian-nlp-fastapi
```

Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install packages

```bash
pip install fastapi[all]
pip install spacy

pip install https://github.com/explosion/spacy-models/releases/download/ru_core_news_lg-3.2.0/ru_core_news_lg-3.2.0-py3-none-any.whl
pip install https://github.com/explosion/spacy-models/releases/download/ru_core_news_lg-3.2.0/ru_core_news_lg-3.2.0.tar.gz
```

Run the app

```
uvicorn src.main:app --reload
```

Make an http request : 

```
curl -X POST http://localhost:8000/entities -H 'Content-Type: application/json' -d '{"text":"Изменение системы выплат зарплат госслужащим власти России обсуждают с весны 2021 года. Как заявлял руководитель аппарата правительства Дмитрий Григоренко, основой для изменения системы оплаты чиновникам стать реформа госаппарата. «Провести преобразования мешали пустующие ставки. Сложилась ситуация, когда разрыв между ведомствами стал критическим: по министерствам — в 1,5 раза, по службам — 1,7 раза, по агентствам — 1,9 раза, а по территориальным органам — достиг двукратной отметки», — объяснял он. Это привело к тому, что квалифицированные сотрудники стали переходить в ведомства с более высокими зарплатами, отметил зампредседателя кабмина."}'
```

