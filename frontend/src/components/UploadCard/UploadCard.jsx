import React from 'react'
import './UploadCard.css'

const UploadCard = () => {
   return (
        <div className="upload-card">

            <h2>Upload FNOL Document</h2>

            <p>
                Upload a PDF or TXT First Notice of Loss document.
            </p>

            <input
                type="file"
                accept=".pdf,.txt"
            />

            <button>
                Process Claim
            </button>

        </div>
    );
}

export default UploadCard