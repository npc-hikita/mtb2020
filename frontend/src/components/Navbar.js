import { Link } from 'react-router-dom'

// ReactはJavaScriptの関数を使ってコンポーネントを作成します
function Navbar() {
  // JSXという、HTMLとほぼ同じ文法の言語でUIを記述します
  return (
    <div>
    <Link to="/">Home</Link>
    <Link to="/users">ユーザー一覧</Link>
  </div>
  );
}

export default Navbar;