import { useState } from "react";
import axios from "axios";
import { components, defaultTheme } from "react-select";
import AsyncSelect from "react-select/async";
import "./App.sass";

const API_SERVER = "http://localhost:8000";
const { colors } = defaultTheme;

function App() {
  const [query, setQuery] = useState("");
  const [currentQuestion, setCurrentQuestion] = useState({
    Question: "",
    Answer: "",
  });

  return (
    <>
      <section class="hero">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">NLP FAQ Engine</h1>
            <h2 class="subtitle">React Client</h2>
          </div>
        </div>
      </section>
      <body>
        <section class="section">
          <div class="container">
            <AsyncSelect
              cacheOptions
              onInputChange={(query) => {
                setQuery(query);
              }}
              value={query}
              placeholder={"Search questions..."}
              noOptionsMessage={() => "Suggestions will come here..."}
              onChange={(question) => {
                setCurrentQuestion(question);
              }}
              loadOptions={() => {
                return axios
                  .get(`${API_SERVER}/faqengine?query=${query}`)
                  .then((response) => response.data.results)
                  .catch((e) => {
                    console.log(e);
                  });
              }}
              components={{
                Option: customComponent,
                DropdownIndicator,
              }}
            />
          </div>
        </section>
        <body>
          <section class="section">
            <div class="container">
              <div class="heading">
                <h1 class="title">{currentQuestion.Question}</h1>
                <h2 class="subtitle">{currentQuestion.Answer}</h2>
              </div>
            </div>
          </section>
        </body>
      </body>
    </>
  );
}

const customComponent = (props) => {
  return (
    <components.Option {...props}>
      <div style={{ display: "inline-block" }}>{props.data.Question}</div>
    </components.Option>
  );
};

const Svg = (p) => (
  <svg
    width="30"
    height="30"
    viewBox="-5 -5 30 30"
    focusable="false"
    role="presentation"
    {...p}
  />
);

const DropdownIndicator = () => (
  <div css={{ color: colors.neutral20, height: 24, width: 32 }}>
    <Svg>
      <path
        d="M16.436 15.085l3.94 4.01a1 1 0 0 1-1.425 1.402l-3.938-4.006a7.5 7.5 0 1 1 1.423-1.406zM10.5 16a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11z"
        fill="currentColor"
        fillRule="evenodd"
      />
    </Svg>
  </div>
);

export default App;
