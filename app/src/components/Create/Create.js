import { IonButton, IonCol, IonContent, IonGrid, IonImg, IonModal, IonPage, IonRow } from "@ionic/react";
import { useState } from "react";
import './Create.css';

const CounterRow = ({ value, setValue, imageSrc }) => (
    <div style={{ textAlign: 'center' }}>
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <IonButton
                onClick={() => setValue(value - 1)}
                className="btn"
            >
                -
            </IonButton>
            <IonImg src={imageSrc} style={{ width: '50px', height: '50px', margin: '0 10px' }} />
            <IonButton
                onClick={() => setValue(value + 1)}
                className="btn"
            >
                +
            </IonButton>
        </div>
        <div style={{ marginTop: '10px' }}>
            <span>{value}</span>
        </div>
    </div>
);

const Create = () => {
    const [value1, setValue1] = useState(0);
    const [value2, setValue2] = useState(0);
    const [value3, setValue3] = useState(0);

    return (
        <IonPage>
            <IonContent>
                <div style={{ display: 'flex', margin: 'auto', justifyContent: 'center', alignItems: 'center', height: '100%' }}>
                    <IonGrid style={{ maxWidth: '600px', margin: 'auto', justifyContent: 'center' }}>
                        <IonRow>
                            <IonCol size="4" className="ion-align-self-center">
                                <CounterRow value={value1} setValue={setValue1} imageSrc="" />
                            </IonCol>

                            <IonCol size="4" className="ion-align-self-center">
                                <CounterRow value={value2} setValue={setValue2} imageSrc="" />
                            </IonCol>

                            <IonCol size="4" className="ion-align-self-center">
                                <CounterRow value={value3} setValue={setValue3} imageSrc="" />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol size="auto">
                                <IonButton>Next</IonButton>
                            </IonCol>
                        </IonRow>
                    </IonGrid>
                </div>
            </IonContent>
        </IonPage >
    );
};

export default Create;
