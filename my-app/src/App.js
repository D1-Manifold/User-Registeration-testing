import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function RegisterForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("https://testing.saigujral.repl.co/register", { email, password, confirm_password: confirmPassword });
      setIsSubmitted(true);
      setTimeout(() => {
        setIsSubmitted(false);
        window.location.href = response.data;
      }, 5000);
    } catch (error) {
      setError(error.response.data);
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="register-form">
        <h2>Create an Account</h2>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            className="form-control"
            name="email"
            required
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            className="form-control"
            name="password"
            required
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="confirmPassword">Confirm Password:</label>
          <input
            type="password"
            className="form-control"
            name="confirmPassword"
            required
            value={confirmPassword}
            onChange={(event) => setConfirmPassword(event.target.value)}
          />
        </div>
        {error && <div className="alert alert-danger">{error}</div>}
        <button type="submit" className="btn btn-primary btn-block">Create Account</button>
        {isSubmitted && (
          <div className="text-center mt-3">
            Form is submitted.
          </div>
        )}
      </form>
    </div>
  );
}

export default RegisterForm;