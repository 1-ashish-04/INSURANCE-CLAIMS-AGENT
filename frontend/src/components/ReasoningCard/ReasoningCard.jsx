import "./ReasoningCard.css";

function ReasoningCard({ reasoning }) {

    return (

        <div className="reasoning-card">

            <h2>AI Decision Explanation</h2>

            <p>
                {reasoning}
            </p>

        </div>

    );

}

export default ReasoningCard;