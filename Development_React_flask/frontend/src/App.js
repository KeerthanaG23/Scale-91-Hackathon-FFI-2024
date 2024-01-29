import "./App.css";
import React from "react";
import Sidebar from "./Components/Sidebar";
import RealTimeStockPrice from "./Components/RealTimeStockPrice";
import Dashboard from "./Components/dashboard";
import Header from "./Components/header";
import StockPerformanceComparison from "./Components/StockPerformanceComparison";
import StockPrediction from "./Components/StockPrediction";
import Pesonalisedinvestmentinsights from "./Pesonalisedinvestmentinsights";
import Trading from "./Trading";
function App() {
  const currentPath = window.location.pathname;
  const renderPage = () => {
    switch (currentPath) {
      case "/dashboard":
        return <Dashboard />;
      case "/rtsp":
        return <RealTimeStockPrice />;
      case "/spc":
        return <StockPerformanceComparison />;
      case "/forecast":
        return <StockPrediction />;
      case "/pii":
        return <Pesonalisedinvestmentinsights />;
      case "/trading":
        return <Trading />;
      // Add cases for other pages
      default:
        return <Dashboard />;
    }
  };

  return (
    <div className="App">
      <Header />
      <Sidebar />
      <div className="content" style={{ marginLeft: "300px", padding: "20px" }}>
        {renderPage()}
      </div>
    </div>
  );
}

export default App;
