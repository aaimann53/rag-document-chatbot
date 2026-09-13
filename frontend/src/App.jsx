import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      setAnswer("Unable to connect to the RAG backend.");
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      askQuestion();
    }
  };

  return (
    <div className="app">

      {/* Sidebar */}
      <aside className="sidebar">
        <div className="logo">
          <div className="logo-icon">✦</div>
          <div>
            <h2>DocuMind</h2>
            <span>RAG Assistant</span>
          </div>
        </div>

        <div className="sidebar-section">
          <p className="section-title">DOCUMENT</p>

          <div className="document-card">
            <div className="pdf-icon">PDF</div>
            <div>
              <strong>Production House</strong>
              <span>Production House.pdf</span>
            </div>
          </div>
        </div>

        <div className="sidebar-info">
          <span>●</span>
          <div>
            <strong>Knowledge base ready</strong>
            <p>Ask anything from your document.</p>
          </div>
        </div>

        <div className="sidebar-footer">
          <span>Powered by</span>
          <strong>FastAPI + Gemini</strong>
        </div>
      </aside>

      {/* Main Content */}
      <main className="main">

        {/* Header */}
        <header className="topbar">
          <div>
            <h1>Production House Assistant</h1>
            <p>Ask questions and get answers from your document.</p>
          </div>

          <div className="status">
            <span className="status-dot"></span>
            Online
          </div>
        </header>

        {/* Chat Area */}
        <section className="chat-area">

          {!answer && !loading && (
            <div className="welcome">

              <div className="welcome-icon">✦</div>

              <h2>How can I help you?</h2>

              <p>
                Ask a question about the Production House document.
                I'll retrieve the relevant information and generate an answer.
              </p>

              <div className="suggestions">

                <button
                  onClick={() =>
                    setQuestion("What services does a production house provide?")
                  }
                >
                  <span>📋</span>
                  What services does a production house provide?
                </button>

                <button
                  onClick={() =>
                    setQuestion("What is a production house?")
                  }
                >
                  <span>💡</span>
                  What is a production house?
                </button>

                <button
                  onClick={() =>
                    setQuestion("What are the stages of the production process?")
                  }
                >
                  <span>🎬</span>
                  What are the stages of production?
                </button>

              </div>
            </div>
          )}

          {(answer || loading) && (
            <div className="conversation">

              <div className="message user-message">
                <div className="avatar user-avatar">U</div>
                <div className="message-content">
                  <span className="message-label">You</span>
                  <p>{question}</p>
                </div>
              </div>

              <div className="message assistant-message">
                <div className="avatar ai-avatar">✦</div>

                <div className="message-content">
                  <span className="message-label">DocuMind</span>

                  {loading ? (
                    <div className="typing">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  ) : (
                    <p>{answer}</p>
                  )}
                </div>
              </div>

            </div>
          )}

        </section>

        {/* Input */}
        <div className="input-wrapper">
          <div className="input-box">

            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask something about your document..."
              rows="1"
            />

            <button
              className="send-button"
              onClick={askQuestion}
              disabled={loading || !question.trim()}
            >
              ↑
            </button>

          </div>

          <p className="input-hint">
            Press <strong>Enter</strong> to send
          </p>
        </div>

      </main>
    </div>
  );
}

export default App;