/**
 * @author Copilot
 * @stage Start
 */

import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';

const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleLogin = () => {
    // Add your login logic here
    console.log('Email:', email);
    console.log('Password:', password);
  };

  return (
    <div>
      <TextField
        label="Email"
        value={email}
        onChange={handleEmailChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Password"
        value={password}
        onChange={handlePasswordChange}
        type="password"
        fullWidth
        margin="normal"
      />
      <Button variant="contained" color="primary" onClick={handleLogin}>
        Login
      </Button>
    </div>
  );
};

export default LoginPage;

/**
 * @author Copilot
 * @stage End
 */