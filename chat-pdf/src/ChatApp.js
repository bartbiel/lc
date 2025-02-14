import React, { useState } from "react";
import axios from "axios";

function ChatApp() {
  const [pdf, setPdf] = useState(null);
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);  // We now track the entire response object

  const handleFileChange = (event) => {
    setPdf(event.target.files[0]);
  };

  const uploadPdf = async () => {
    if (!pdf) return alert("Please select a PDF file.");
    
    const formData = new FormData();
    formData.append("file", pdf);

    try {
      await axios.post("http://localhost:8000/upload_pdf/", formData);
      alert("PDF uploaded and processed successfully!");
    } catch (error) {
      console.error("Upload error:", error);
      alert("Failed to upload PDF.");
    }
  };

  const askQuestion = async () => {
    if (!question) return alert("Please enter a question.");

    try {
      const res = await axios.post("http://localhost:8000/mistralchat/", { query: question });

      // Assuming the response is an object with query and result fields
      setResponse(res.data);  // Store the whole response object
    } catch (error) {
      console.error("Chat error:", error);
      alert("Failed to fetch response.");
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "50px auto", textAlign: "center" }}>
      <h2>Chat with PDF_ (Mistral 7B)</h2>

      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <button onClick={uploadPdf} style={{ margin: "10px" }}>Upload PDF</button>

      <br />
      <input 
        type="text" 
        placeholder="Ask a question..." 
        value={question} 
        onChange={(e) => setQuestion(e.target.value)} 
        style={{ width: "80%", padding: "10px", marginTop: "20px" }}
      />
      <button onClick={askQuestion} style={{ marginLeft: "10px" }}>Ask</button>

      <div style={{ marginTop: "20px", padding: "10px", border: "1px solid #ddd", minHeight: "50px" }}>
        <strong>Response:</strong>
        {/* Ensure we render the response correctly */}
        {response ? (
          <>
            <p><strong>Query:</strong> {response.query}</p>
            <p><strong>Result:</strong> {response.result}</p>
          </>
        ) : (
          <p>Waiting for response...</p>
        )}
      </div>
    </div>
  );
}

export default ChatApp;
