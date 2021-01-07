import { BrowserRouter as Router, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import UserList from './pages/UserList';
import Home from './pages/Home';

function App() {
  return (
    <div className="App">
      <h1>演習App</h1>

      <Router>
        <div>
          <Navbar /><hr />
          <Route exact path='/' component={Home} />
          <Route path='/users' component={UserList} />
        </div>
      </Router>

    </div>
  );
}

export default App;
