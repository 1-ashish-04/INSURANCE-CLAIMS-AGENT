import { useState } from "react";
import "./UploadCard.css";
import api from "../../services/api";

function UploadCard({ onResult }) {
    const [selectedFile, setSelectedFile] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            alert("Please select a PDF or TXT file.");
            return;
        }

        const formData = new FormData();
        formData.append("file", selectedFile);

        try {
            setLoading(true);

            const response = await api.post(
                "/process-claim",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            onResult(response.data);
        } catch (error) {
            console.error(error);
            alert("Failed to process the document.");
        } finally {
            setLoading(false);
        }
    };

   return (

    <div className="upload-card">

        <h2>Upload First Notice of Loss (FNOL)</h2>

        <p>
            Upload a PDF or TXT document to process an
            insurance claim using AI.
        </p>

        <div className="upload-box">

            <div className="upload-icon">
                📄
            </div>

            <p className="upload-text">
                Click below to choose your FNOL document
            </p>

            <p className="supported">
                Supported formats: PDF, TXT
            </p>

            <label className="choose-btn">

                Choose File

                <input
                    type="file"
                    accept=".pdf,.txt"
                    onChange={handleFileChange}
                    hidden
                />

            </label>

        </div>

        <div className="selected-file">

            {selectedFile ? (

                <span>
                    ✅ {selectedFile.name}
                </span>

            ) : (

                <span>No file selected</span>

            )}

        </div>

        <button

            onClick={handleUpload}

            disabled={loading}

        >

            {loading

                ? "Processing..."

                : "Process Claim"}

        </button>

    </div>

);
}

export default UploadCard;