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

## API

API documentation will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)

## Sample API

Endpoint **[GET]**: [http://localhost:8000/faqengine?query=register%20isd](http://localhost:8000/faqengine?query=register%20isd)

Output:

```
{
  "query": "register isd",
  "results": [
    {
      "Question": "I have migrated under GST but want to register as ISD. Whether I can apply now & what is the procedure? ",
      "Answer": "separate & new registration is required for ISD."
    },
    {
      "Question": "How long can I wait to register in GST ? ",
      "Answer": "unregistered person has 30 days to complete its registration formalities from its date of liability to obtain registration. "
    },
    {
      "Question": "What If I am not liable to register under GST but I was registered under Service tax ? ",
      "Answer": "can apply for cancellation of Provisional ID on or before 31st July 2017. "
    },
    {
      "Question": "If I am not an existing taxpayer and wish to newly register under GST, when can I do so? ",
      "Answer": "would be able to apply for new registration at the GST Portal gst.gov.in"
    }
  ]
}
```

All the examples are available in `example` directory

## React Client

[![FAQ NLP Engine - React Client](https://github.com/feat7/nlp-faq-engine/blob/main/screenshots/react_client_nlp_faq_engine.png?raw=true)](https://github.com/feat7/nlp-faq-engine/blob/main/screenshots/react_client_nlp_faq_engine.png?raw=true)

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
