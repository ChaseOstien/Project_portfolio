import { useState } from 'react';
import './App.css';
import Api from './Api';
import projectData from './utils/projects.json';
import ListItem from './ListItem';

export default function App() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    phoneNumber: '',
    email: '',
    message: ''
  });
  const [trackSubmission, setTrackSubmission] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prevFormData) => ({
      ...prevFormData, [name]: value
    }))
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    

    setTrackSubmission(!null);

    console.log(formData);

  }


  return (
    <>
      <div className='container'>
        <form className='form'>
          <label className='label'>First Name:
            <input name='firstName'  className='input' onChange={handleChange} placeholder='First Name'></input>
          </label>
          <label className='label'>Last Name:
            <input name='lastName' className='input' onChange={handleChange} placeholder='Last Name'></input>
          </label>
          <label className='label'>Phone Number:
            <input name='phoneNumber' className='input' onChange={handleChange} placeholder='Phone Number'></input>
          </label>
          <label className='label'>Email:
            <input name='email' className='input' onChange={handleChange} placeholder='Email'></input>
          </label>
          <label className='label'>Message:
            <textarea name='message' className='input' onChange={handleChange} placeholder='Message'></textarea>
          </label>
          <button onClick={handleSubmit} type='submit' className='button'>Submit</button>
        </form>
      <>
        <div className='message'>
          {trackSubmission !== null ? 
            <>
              <h3 className='info'>
                Hello, my name is {formData.firstName} {formData.lastName}, you can call me at {formData.phoneNumber}, or email me at {formData.email}!
              </h3>
              <h3>Check the console to see your message!
              </h3>
            </> : <h3>Fill out the form to see this message!</h3>}
        </div>
      </>
      </div>
      <Api />
      <h2>Project List:</h2>
      <div className='projects'>
        {projectData.map((project) => (
          <ListItem project={project} key={project.id}/>
        ))}
      </div>
    </>
  )
}
