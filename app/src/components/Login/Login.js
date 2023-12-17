import { IonButton, IonCard, IonCol, IonContent, IonDatetime, IonGrid, IonHeader, IonInput, IonItem, IonLabel, IonPage, IonRedirect, IonRow, IonText, IonTitle, IonToolbar } from '@ionic/react';
import './Login.css'
import { CapacitorHttp } from '@capacitor/core';
import { Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';

function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    email: '',
    password: '',
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  }

  const login = async (e) => {
    e.preventDefault();

    const options = {
      url: 'https://capital-eagle-smiling.ngrok-free.app/v1/user/login',
      headers: { 'Content-Type': 'application/json' },
      data: form
    }

    var response = await CapacitorHttp.post(options);
    console.log(response)

    if (response.status === 200) {
      localStorage.setItem('token', response.data.access_token)
      navigate("/dashboard")
    } else {
      alert("error")
    }
  }
  return (

    <IonPage style={{ paddingTop: 'env(safe-area-inset-bottom)' }}>
      <IonContent>
        <div className='centered-element'>
          <IonText className="ion-text-center ion-padding">
            <h1 className='title-login'>Iniciar Sessió</h1>
          </IonText>
          <form className='ion-padding-horizontal' onSubmit={login}>
            <IonItem>
              <IonLabel position="floating">Correu Electrònic</IonLabel>
              <IonInput
                type="email"
                name="email"
                value={form.email}
                onIonChange={handleChange}
                required />
            </IonItem>
            <IonItem>
              <IonLabel position="floating">Contrasenya</IonLabel>
              <IonInput
                type="password"
                name="password"
                value={form.password}
                onIonChange={handleChange}
                required />
            </IonItem>
            <IonButton expand="block" type="submit" className='marginTop'>
              Submit
            </IonButton>
            <IonText className="ion-text-center ion-padding">
              <p>Encara no ets membre de CycleH?&nbsp;<Link to={"/signup"}><b>Registra't!</b></Link> </p>
            </IonText>
          </form>
        </div>
      </IonContent>
    </IonPage >

  );
}

export default Login;
