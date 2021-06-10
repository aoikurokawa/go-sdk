import React, { Fragment, useEffect, useState } from 'react';
import { useParams } from "react-router-dom";
import Account from '../components/Account';

function AccountPage() {
    const { address } = useParams();
    const { account, setAccount } = useState({});
    const { loaded, setLoaded } = useState(false);
    return loaded ? <Account account={account}></Account> : <Fragment></Fragment>;
}

export default AccountPage;

