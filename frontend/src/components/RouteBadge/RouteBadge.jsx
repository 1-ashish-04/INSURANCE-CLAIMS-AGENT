import "./RouteBadge.css";

function RouteBadge({ route }) {

    if (!route) return null;

    let badgeClass = "badge";

    if (route === "Fast-track")
        badgeClass += " fast";

    else if (route === "Manual Review")
        badgeClass += " manual";

    else if (route === "Investigation Flag")
        badgeClass += " investigation";

    else
        badgeClass += " specialist";

    return (

        <div className="route-card">

            <h2>Recommended Route</h2>

            <span className={badgeClass}>

                {route}

            </span>

        </div>

    );

}

export default RouteBadge;