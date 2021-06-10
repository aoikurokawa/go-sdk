import React, { Fragment, useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Link as RouterLink,
  Switch,
  Route
} from "react-router-dom";
import {
  AppBar,
  Toolbar,
  Typography,
  Link,
  IconButton,
  Container,
  Chip,
  Icon
} from "@material-ui/core";
import { SpeedDial, SpeedDialAction, SpeedDialIcon } from "@material-ui/lab";
import { makeStyles } from "@material-ui/core/styles";
import MenuIcon from "@material-ui/icons/Menu";
import AddIcon from "@material-ui/icons/Add";
import AddPhotoAlternateIcon from "@material-ui/icons/AddPhotoAlternate";
import { nodeInfoContextDefaultValue, NodeInfoContext } from "./context";

import './App.css';

const useStyles = makeStyles((theme) => ({
  appBarLink: {
    margin: theme.spacing(0, 2),
    flex: 1,
  },
  speedDial: {
    position: 'absolute',
    bottom: theme.spacing(2),
    right: theme.spacing(2),
  },
  contentContainer: {
    padding: theme.spacing(5, 6),
  }
}));

function App() {
  const classes = useStyles();
  const [nodeInfoState, updateNodeInfoState] = useState(nodeInfoContextDefaultValue);
  const [openSpeedDial, setOpenSpeedDial] = useState(false);
  const [openDialog, setOpenDialog] = useState(null);

  const handleSpeedDialClose = () => {
    setOpenSpeedDial(false);
  }

  const handleSpeedDialOpen = () => {
    setOpenSpeedDial(true);
  }
  return (
    <Fragment>
      <NodeInfoContext.Provider value={nodeInfoState}>
        <Router>
          <AppBar position="static">
            <Toolbar>
              <IconButton edge="start" color="inherit" aria-label="menu">
                <MenuIcon />
              </IconButton>
              <Typography variant="h6">QUIZ APP</Typography>

              <Link
                color="inherit"
                component={RouterLink}
                to="/"
                className={classes.appBarLink}
              >
                Home
              </Link>
              <Link
                color='inherit'
                component={RouterLink}
                to="/transactions"
                className={classes.appBarLink}
              >
                Transactions
              </Link>
              <div className={classes.grow} />
              <Chip label={nodeInfoState.height} />
            </Toolbar>
          </AppBar>

          <SpeedDial
            ariaLabel="SpeedDial example"
            color="secondary"
            className={classes.speedDial}
            icon={<SpeedDialIcon />}
            onClose={handleSpeedDialClose}
            onOpen={handleSpeedDialOpen}
            open={openSpeedDial}
            direction="up"
          >
            <SpeedDialAction
              key={'Create NFT'}
              icon={<AddPhotoAlternateIcon />}
              tooltipTitle={'Create QUIZ'}
              onClick={() => {
                setOpenSpeedDial(false);
                setOpenDialog('CreateQuizDialog');
              }}
            />

            <SpeedDialAction
              key={'Create Account'}
              icon={<AddIcon />}
              tooltipTitle={'Create Account'}
              onClick={() => {
                setOpenSpeedDial(false);
                setOpenDialog('CreateAccountDialog');
              }}
            />

          </SpeedDial>
        </Router>

      </NodeInfoContext.Provider>
      <div className="App">

      </div>
    </Fragment>

  );
}

export default App;
