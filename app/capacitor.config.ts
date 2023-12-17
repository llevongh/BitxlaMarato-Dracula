import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.example.app',
  appName: 'CycleH',
  webDir: 'build',
  server: {
    androidScheme: 'https',
    url: "http://localhost:3000",
    cleartext: true
  },
  plugins: {
    CapacitorHttp: {
      "enabled": true
    }
  }
};

export default config;
