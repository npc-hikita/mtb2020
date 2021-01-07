import { useEffect, useState } from "react"

function UserList() {
  // データを詰める先を用意
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const f = async () => {
      const res = await fetch("/api/users");
      const data = await res.json();
      // とってきたデータを詰める
      setUsers(data.users);
    }
    f();
  }, [])

  return (
    <div className="App">
      <h1>ユーザー一覧</h1>
      <table>
        <thead>
          <tr>
            <th>名前</th>
            <th>部署</th>
          </tr>
        </thead>
        <tbody>
          {/* データをぐるぐる回して表示（JavaScriptが書けるよ！） */}
          {users.map(user => (
            <tr key={user.name}>
              <td>{user.name}</td>
              <td>{user.dept}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default UserList;
