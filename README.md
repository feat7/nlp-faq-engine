# NLP FAQEngine

FAQEngine helps you build a FAQ search solution.
It internally uses NLP techniques to find out the most related question for a given user query.

# Server

1. Install dependencies

```
pip install -r requirements.txt
```

2. Provide your own `faqs.csv` file having two columns viz., `Question` and `Answer`

3. Start `fastAPI` server

```
uvicorn fast_api:app
```

# Usage

All the examples are available in `example` directory

## React Client

React Client code example is provided in `example/react-example`.

To Run:

1. Move to react code

```
cd example/react-example
```

2. Install dependencies

```
yarn install            OR          npm install
```

3. Run

```
yarn start              OR          npm start
```
