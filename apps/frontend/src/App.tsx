/**
 * @author ChatGPT
 * @stage Start
 */

import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from 'react-router-dom';
import LoginPage from './pages/login.page';
import { UserPage } from './pages/user.page'; // brackets #1 added by MZ
import PrivateRoute from './components/PrivateRoute'; // #1 updated by ChatGPT
import { AuthProvider } from './context/AuthContext'; // #1 added by ChatGPT

const App: React.FC = () => {
  return (
    <AuthProvider>
      {/* #1 updated by ChatGPT*/}
      <Router>
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/user"
            element={
              <PrivateRoute>
                <UserPage />
              </PrivateRoute>
            }
          />
          {/* #8 updated by ChatGPT*/}
        </Routes>
      </Router>
      {/* #1 updated by ChatGPT*/}
    </AuthProvider>
  );
};

export default App;

/**
 * @author ChatGPT
 * @stage End
 */