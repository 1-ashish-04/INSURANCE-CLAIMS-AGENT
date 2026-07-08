import React from 'react'
import Header from "../../components/Header/Header";
import UploadCard from "../../components/UploadCard/UploadCard";

import "../../styles/home.css";

function Home() {
    return (
        <>
            <Header />

            <main className="home">

                <UploadCard />

            </main>
        </>
    );
}

export default Home;