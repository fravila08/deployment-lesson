import App from './App'
import { createHashRouter, createBrowserRouter } from 'react-router-dom';
import { SignUp } from './components/SignUp';
import { LogIn } from './components/LogIn';
import { Task } from './components/Tasks';
import { getTasks } from './utilities';

const Router = createHashRouter([{
    path: '/',
    element: <App />,
    children: [
        {
            index: true,
            element: <SignUp />
        },
        {
            path:"/login/",
            element: <LogIn />
        },
        {
            path:"/tasks/",
            element: <Task />,
            loader: getTasks
        }
    ]
}])

export default Router;