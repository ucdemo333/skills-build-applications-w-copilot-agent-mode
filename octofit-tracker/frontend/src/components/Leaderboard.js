import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [data, setData] = useState([]);
  const [endpoint, setEndpoint] = useState('');

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const url = `https://${codespace}-8000.app.github.dev/api/leaderboard/`;
    setEndpoint(url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        console.log('Leaderboard API endpoint:', url);
        console.log('Leaderboard data:', json);
        setData(json.results || json);
      })
      .catch(err => console.error('Fetch error:', err));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header bg-warning text-dark">
          <h2 className="mb-0"><i className="bi bi-trophy"></i> 排行榜</h2>
        </div>
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle">
              <thead className="table-dark">
                <tr>
                  {data[0] && Object.keys(data[0]).map((key) => (
                    <th key={key}>{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    {Object.values(item).map((val, i) => (
                      <td key={i}>{val}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
            {data.length === 0 && <div className="text-center text-muted">無資料</div>}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
