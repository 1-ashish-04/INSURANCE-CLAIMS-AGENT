import { useState } from "react";

import Header from "../../components/Header/Header";
import UploadCard from "../../components/UploadCard/UploadCard";
import ResultCard from "../../components/ResultCard/ResultCard";
import RouteBadge from "../../components/RouteBadge/RouteBadge";
import MissingFields from "../../components/MissingFields/MissingFields";
import ConsistencyIssues from "../../components/ConsistencyIssues/ConsistencyIssues";
import ReasoningCard from "../../components/ReasoningCard/ReasoningCard";

import "./home.css";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <>
      <Header />

      <main className="home">
        <UploadCard onResult={setResult} />
        {result && (
          <section className="dashboard">
            <ResultCard extractedFields={result.extractedFields} />
            <div className="dashboard-grid">
              <RouteBadge route={result.recommendedRoute} />

              <ReasoningCard reasoning={result.reasoning} />

              <MissingFields fields={result.missingFields} />

              <ConsistencyIssues issues={result.consistencyIssues} />
            </div>
          </section>
        )}
      </main>
    </>
  );
}

export default Home;
