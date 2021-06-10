export const fetchNodeInfo = async () => {
    return fetch("http://localhost:4000/api/node/info")
    .then((res) => res.json())
    .then((res) => res.data);
};
