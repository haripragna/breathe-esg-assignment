import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [sourceType, setSourceType] = useState("SAP");
  const [message, setMessage] = useState("");
  const [records, setRecords] = useState([]);

  const fetchRecords = async () => {
    const response = await axios.get("http://127.0.0.1:8000/api/records/");
    setRecords(response.data);
  };

  const handleUpload = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        { source_type: sourceType }
      );

      setMessage(response.data.message);
      fetchRecords();
    } catch (error) {
      setMessage("Upload failed");
    }
  };

  useEffect(() => {
    fetchRecords();
  }, []);

  return (
    <div style={{ padding: "40px" }}>
      <h1>Breathe ESG Analyst Dashboard</h1>

      <h3>Upload Source Data</h3>

      <select
        value={sourceType}
        onChange={(e) => setSourceType(e.target.value)}
      >
        <option value="SAP">SAP</option>
        <option value="UTILITY">Utility</option>
        <option value="TRAVEL">Travel</option>
      </select>

      <button onClick={handleUpload} style={{ marginLeft: "10px" }}>
        Upload
      </button>

      <p>{message}</p>

      <h2>Normalized Records</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Category</th>
            <th>Scope</th>
            <th>Value</th>
            <th>Unit</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {records.map((record) => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.category}</td>
              <td>{record.scope}</td>
              <td>{record.value}</td>
              <td>{record.unit}</td>
              <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;