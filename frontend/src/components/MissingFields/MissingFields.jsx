import "./MissingFields.css";

function MissingFields({ fields }) {

    return (

        <div className="missing-card">

            <h2>Missing Fields</h2>

            {

                fields.length === 0

                ?

                <p className="success">

                    ✅ No missing fields.

                </p>

                :

                <ul>

                    {fields.map(field=>(

                        <li key={field}>

                            {field}

                        </li>

                    ))}

                </ul>

            }

        </div>

    );

}

export default MissingFields;