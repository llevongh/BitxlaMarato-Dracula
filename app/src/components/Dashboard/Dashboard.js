import React, { useEffect, useRef } from 'react';
import {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonGrid,
    IonRow,
    IonCol,
    IonIcon,
    IonText,
    IonButton,
} from '@ionic/react';
import { logoIonic } from 'ionicons/icons'; // Import the Ionic icon you want to use
import './Dashboard.css';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';
import { addCircleOutline } from 'ionicons/icons';
import { Link, Navigate, useNavigate } from 'react-router-dom';


function Dashboard() {
    const navigate = useNavigate();
    const data = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [
            {
                label: 'Monthly Sales',
                data: [5, 5, 6, 4.4, 4.4, 4.7],
                fill: false,
                borderColor: 'white',
                tension: 0.5
            }
        ]
    };

    const options = {
        scales: {
            x: {
                display: false, // Hides the x-axis
            },
            y: {
                display: false, // Hides the y-axis
            }
        },
        plugins: {
            legend: {
                display: false, // Hides the legend
            }
        },
        elements: {
            point: {
                radius: 0 // Hides the points on the line
            }
        }
    };




    return (
        <IonPage style={{ paddingTop: 'env(safe-area-inset-bottom)' }}>
            <IonContent className='ion-padding-top'>
                <div className='flex-center'>
                    <IonGrid>
                        <IonRow>
                            <IonCol>
                                <IonText>
                                    <h2 className='title-dashboard'>Hola, {"Isabel"}!</h2>
                                </IonText>
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol size="12">
                                <IonRow className='ion-text flex action-menu menu round shadow' >
                                    <IonCol size='8' className='flex-center'>
                                        <Line data={data} options={options} />
                                    </IonCol>
                                    <IonCol size='3' className='flex-center'>
                                        <div className='ion-text-center pbac-score'>
                                            <div>PBAC</div>
                                            <div>100</div>
                                        </div>
                                    </IonCol>
                                </IonRow>
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            {/* Left Button */}
                            <IonCol size="4">
                                <IonButton onClick={() => {navigate("/create")}} className='menu round menu' style={{ width: '100%' }}>PBAC Test</IonButton>
                            </IonCol>

                            {/* Middle Button */}
                            <IonCol size="4">
                                <IonButton className='menu round menu' style={{ width: '100%' }}>Samanta Test</IonButton>
                            </IonCol>

                            {/* Right Button */}
                            <IonCol size="4">
                                <IonButton className='menu round menu' style={{ width: '100%' }}>Detector PBAC</IonButton>
                            </IonCol>
                        </IonRow>
                    </IonGrid>
                </div>
            </IonContent>
        </IonPage >
    );
};

export default Dashboard;