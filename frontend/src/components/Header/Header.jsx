import React from 'react'
import './Header.css'


function Header() {
    return (
        <header className="header">
            <div className="header-container">

                <div className="logo">

                    <div className="logo-icon">
                        🚗
                    </div>

                    <div>
                        <h1>Insurance Claim Processor</h1>

                        <p>
                            Autonomous FNOL Processing Agent
                        </p>
                    </div>

                </div>

            </div>
        </header>
    );
}

export default Header;