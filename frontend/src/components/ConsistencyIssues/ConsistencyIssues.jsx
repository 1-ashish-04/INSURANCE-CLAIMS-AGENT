import "./ConsistencyIssues.css";

function ConsistencyIssues({ issues }) {

    return (

        <div className="consistency-card">

            <h2>Consistency Issues</h2>

            {
                !issues || issues.length === 0 ? (

                    <p className="success">
                        ✅ No consistency issues found.
                    </p>

                ) : (

                    <ul>

                        {issues.map((issue, index) => (

                            <li key={index}>
                                {issue}
                            </li>

                        ))}

                    </ul>

                )
            }

        </div>

    );

}

export default ConsistencyIssues;