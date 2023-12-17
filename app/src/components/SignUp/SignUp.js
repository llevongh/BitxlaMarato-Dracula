import { IonButton, IonCard, IonCol, IonContent, IonDatetime, IonGrid, IonHeader, IonInput, IonItem, IonLabel, IonPage, IonRedirect, IonRow, IonText, IonTitle, IonToolbar } from '@ionic/react';
import { CapacitorHttp } from '@capacitor/core';
import { Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';

function SignUp() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    first_name: '',
    last_name: '',
    password: '',
    email: '',
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
      url: 'https://capital-eagle-smiling.ngrok-free.app/v1/user/register',
      headers: { 'Content-Type': 'application/json' },
      data: form
    }

    var response = await CapacitorHttp.post(options);

    if (response.status === 200) {
      alert("yes");
    } else {
      alert("error")
    }
  }
  return (

    < IonPage style={{ paddingTop: 'env(safe-area-inset-bottom)' }
    }>
      <IonContent>
        <div className='centered-element'>
          <IonText className="ion-text-center ion-padding">
            <h1 className='title-login'>Uneix-te!</h1>
          </IonText>
          <form className='ion-padding-horizontal' onSubmit={login}>
            <IonItem>
              <IonLabel position="floating">Nom</IonLabel>
              <IonInput
                type="text"
                name="first_name"
                required
                value={form.first_name}
                onIonChange={handleChange}
              />
            </IonItem>
            <IonItem>
              <IonLabel position="floating">Cognoms</IonLabel>
              <IonInput
                type="text"
                name="last_name"
                required
                value={form.last_name}
                onIonChange={handleChange}
              />
            </IonItem>
            <IonItem>
              <IonLabel position="floating">Correu Electrònic</IonLabel>
              <IonInput
                type="email"
                name="email"
                required
                value={form.email}
                onIonChange={handleChange}
              />
            </IonItem>
            <IonItem>
              <IonLabel position="floating">Contrasenya</IonLabel>
              <IonInput
                type="password"
                name="password"
                required
                value={form.password}
                onIonChange={handleChange}
              />
            </IonItem>
            <IonButton expand="block" type="submit" className='marginTop'>
              Unir-me
            </IonButton>
            <IonText className="ion-text-center ion-padding">
              <p>Ja tens un compte? <Link to={"/"}><b>Iniciar Sessió!</b></Link> </p>
            </IonText>
          </form>
        </div>
      </IonContent>
    </IonPage >

  );
}

export default SignUp;
