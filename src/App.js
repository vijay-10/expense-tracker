import Expenses from "./components/Expenses/Expenses";
import NewExpense from "./components/NewExpense/NewExpense";
import { useState } from "react";

const DUMMY_DATA = [
  {
    id: 'e1',
    title: 'Groceries',
    amount: 100,
    date: new Date(2023, 7, 14),
  },
  { 
    id: 'e2',
    title: 'New TV',
    amount: 7999,
    date: new Date(2022, 2, 12)
  },
  {
    id: 'e3',
    title: 'Car Insurance',
    amount: 299,
    date: new Date(2022, 2, 28),
  },
  {
    id: 'e4',
    title: 'New Sofa',
    amount: 4500,
    date: new Date(2020, 5, 12),
  },
];
const App = () => {

  const [expenses, setExpenses] = useState(DUMMY_DATA)
  
  function addExpenseHandler(expense) {
    console.log(expenses)
    setExpenses((prevState) => {
      return [expense, ...prevState]
    })
  }

  return (
    <div className="App">
      <h1 className="text-center text-[#ececec] font-bold text-[3rem] mt-[1rem]">Expense Tracker</h1>
      <NewExpense onAddExpense={addExpenseHandler}/>
      <Expenses expenses={expenses}/>
    </div>
  );
}

export default App;
