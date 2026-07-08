import React from 'react'
import './UploadCard.css'

function UploadCard() {

    return (

        <div className="upload-card">

            <h2>Upload First Notice of Loss (FNOL)</h2>

            <p>
                Upload a PDF or TXT document to extract insurance
                claim information using AI.
            </p>

            <div className="upload-box">

                <div className="upload-icon">
                    📄
                </div>

                <p>
                    Drag & Drop or Click Below
                </p>

                <input
                    type="file"
                    accept=".pdf,.txt"
                />

            </div>

            <button>
                Process Claim
            </button>

        </div>

    );

}

export default UploadCard;