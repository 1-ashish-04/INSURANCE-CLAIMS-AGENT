import "./ResultCard.css";

function formatLabel(label) {

    return label

        .replace(/([A-Z])/g, " $1")

        .replace(/^./, str => str.toUpperCase());

}

function ResultCard({ extractedFields }) {

    if (!extractedFields) return null;

    return (
        <div className="result-card">

            <h2>Claim Information</h2>

            <table>

                <tbody>

                    {Object.entries(extractedFields).map(([key, value]) => (

                        <tr key={formatLabel(key)}>

                            <td className="label">
                                {formatLabel(key)}
                            </td>

                            <td>
                               {
    key === "estimatedDamage" && value !== null
        ? `₹ ${Number(value).toLocaleString()}`
        : value ?? "N/A"
                               }
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}

export default ResultCard;