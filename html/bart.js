/************* 
 * Bart Test *
 *************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'bart';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'gender (m/f)': '', 'age': '', 'session': '004'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin);
flowScheduler.add(instructionsRoutineEachFrame);
flowScheduler.add(instructionsRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(finalScoreRoutineBegin);
flowScheduler.add(finalScoreRoutineEachFrame);
flowScheduler.add(finalScoreRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.1.3';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('completedURL', 'incompleteURL');

  return Scheduler.Event.NEXT;
}

var instructionsClock;
var instrMessage;
var trialClock;
var bankedEarnings;
var balloonEarnings;
var bankedText;
var lastBalloonEarnings;
var thisBalloonEarnings;
var balloonSize;
var balloonMsgHeight;
var balloonBody;
var reminderMsg;
var balloonValMsg;
var bankedMsg;
var feedbackClock;
var feedbackText;
var bang;
var feedbackMsg;
var finalScoreClock;
var finalScore_2;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instrMessage = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrMessage',
    text: "This is a game where you have to optimise your earnings in a balloon pumping competition.\n\nYou get prize money for each balloon you pump up, according to its size. But if you pump it too far it will pop and you'll get nothing for that balloon.\n\nBalloons differ in their maximum size - they can occasionally reach to almost the size of the screen but most will pop well before that.\n\nPress\n    SPACE to pump the balloon\n    RETURN to bank the cash for this balloon and move onto the next\n",
    font: 'Arial',
    units : 'height', 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  bankedEarnings = 0.0;
  balloonEarnings = '';
  bankedText = '';
  lastBalloonEarnings = 0.0;
  thisBalloonEarnings = 0.0;
  balloonSize=0.08;
  balloonMsgHeight=0.01;
  balloonBody = new visual.ImageStim({
    win : psychoJS.window,
    name : 'balloonBody', units : 'height', 
    image : 'redBalloon.png', mask : undefined,
    ori : (- 90), pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  reminderMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminderMsg',
    text: 'Press SPACE to pump the balloon\nPress RETURN to bank this sum',
    font: 'Arial',
    units : 'height', 
    pos: [0, (- 0.8)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  balloonValMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'balloonValMsg',
    text: 'default text',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.05], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  bankedMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'bankedMsg',
    text: 'default text',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.8], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedbackText=""
  
  bang = new Sound({
      win: psychoJS.window,
      value: "bang.mp3",
      secs: 1.0,
      });
  
  bang.setVolume(1);
  
  balloonBody.setSize(0.10)
  feedbackMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackMsg',
    text: 'default text',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "finalScore"
  finalScoreClock = new util.Clock();
  finalScore_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'finalScore_2',
    text: 'default text',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var resp;
var instructionsComponents;
function instructionsRoutineBegin() {
  //------Prepare to start Routine 'instructions'-------
  t = 0;
  instructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instructionsComponents = [];
  instructionsComponents.push(instrMessage);
  instructionsComponents.push(resp);
  
  for (const thisComponent of instructionsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instrMessage* updates
  if (t >= 0.0 && instrMessage.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instrMessage.tStart = t;  // (not accounting for frame time here)
    instrMessage.frameNStart = frameN;  // exact frame index
    instrMessage.setAutoDraw(true);
  }

  
  // *resp* updates
  if (t >= 0.0 && resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp.tStart = t;  // (not accounting for frame time here)
    resp.frameNStart = frameN;  // exact frame index
    resp.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instructionsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEnd() {
  //------Ending Routine 'instructions'-------
  for (const thisComponent of instructionsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1.0, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialTypes.xlsx',
    seed: 1832, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(feedbackRoutineBegin);
    thisScheduler.add(feedbackRoutineEachFrame);
    thisScheduler.add(feedbackRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisTrial));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var popped;
var nPumps;
var bankButton;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  balloonSize=0.08;
  popped=false;
  nPumps=0;
  balloonBody.ori = 90;
  bankButton = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(balloonBody);
  trialComponents.push(reminderMsg);
  trialComponents.push(balloonValMsg);
  trialComponents.push(bankedMsg);
  trialComponents.push(bankButton);
  
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  thisBalloonEarnings=nPumps*0.05;
  balloonEarnings = "This balloon value:\n£" + thisBalloonEarnings.toFixed(2);
  bankedText = "You have banked:\n£" + bankedEarnings.toFixed(2);
  balloonSize=0.1+nPumps*0.015;
  
  // *balloonBody* updates
  if (t >= 0.0 && balloonBody.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    balloonBody.tStart = t;  // (not accounting for frame time here)
    balloonBody.frameNStart = frameN;  // exact frame index
    balloonBody.setAutoDraw(true);
  }

  
  if (balloonBody.status === PsychoJS.Status.STARTED){ // only update if being drawn
    balloonBody.setPos([0, ((balloonSize / 2) - 0.5)]);
    balloonBody.setSize(balloonSize);
  }
  
  // *reminderMsg* updates
  if (t >= 0.0 && reminderMsg.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    reminderMsg.tStart = t;  // (not accounting for frame time here)
    reminderMsg.frameNStart = frameN;  // exact frame index
    reminderMsg.setAutoDraw(true);
  }

  
  // *balloonValMsg* updates
  if (t >= 0.0 && balloonValMsg.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    balloonValMsg.tStart = t;  // (not accounting for frame time here)
    balloonValMsg.frameNStart = frameN;  // exact frame index
    balloonValMsg.setAutoDraw(true);
  }

  
  if (balloonValMsg.status === PsychoJS.Status.STARTED){ // only update if being drawn
    balloonValMsg.setText(balloonEarnings);
  }
  
  // *bankedMsg* updates
  if (t >= 0.0 && bankedMsg.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    bankedMsg.tStart = t;  // (not accounting for frame time here)
    bankedMsg.frameNStart = frameN;  // exact frame index
    bankedMsg.setAutoDraw(true);
  }

  
  if (bankedMsg.status === PsychoJS.Status.STARTED){ // only update if being drawn
    bankedMsg.setText(bankedText);
  }
  var thisResp = psychoJS.eventManager.getKeys();
  if ("space" == thisResp[0]) {
      nPumps = nPumps+1;
      if (nPumps > maxPumps) {
          popped=true;
          continueRoutine=false;
      }
  }
  
  if ("return" == thisResp[0]) {
      popped=false;
      continueRoutine=false;
  }
  
  // *bankButton* updates
  if (t >= 0.0 && bankButton.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    bankButton.tStart = t;  // (not accounting for frame time here)
    bankButton.frameNStart = frameN;  // exact frame index
    bankButton.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (bankButton.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['return']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  for (const thisComponent of trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  //calculate cash 'earned'
  if (popped) {
    thisBalloonEarnings=0.0;
    lastBalloonEarnings=0.0;
  } else {
    lastBalloonEarnings=thisBalloonEarnings;
  }
  bankedEarnings = bankedEarnings + lastBalloonEarnings
  //save data
  psychoJS.experiment.addData('nPumps', nPumps);
  psychoJS.experiment.addData('size', balloonSize);
  psychoJS.experiment.addData('earnings', thisBalloonEarnings);
  psychoJS.experiment.addData('popped', popped);
  
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var feedbackComponents;
function feedbackRoutineBegin() {
  //------Prepare to start Routine 'feedback'-------
  t = 0;
  feedbackClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  if (popped == true) {
      feedbackText = "Oops! Lost that one!";
      bang.play();
  } else {
      feedbackText="You banked £" + lastBalloonEarnings.toFixed(2);
  }
  feedbackMsg.setText(feedbackText);
  // keep track of which components have finished
  feedbackComponents = [];
  feedbackComponents.push(feedbackMsg);
  
  for (const thisComponent of feedbackComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function feedbackRoutineEachFrame() {
  //------Loop for each frame of Routine 'feedback'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = feedbackClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *feedbackMsg* updates
  if (t >= 0.0 && feedbackMsg.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    feedbackMsg.tStart = t;  // (not accounting for frame time here)
    feedbackMsg.frameNStart = frameN;  // exact frame index
    feedbackMsg.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (feedbackMsg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    feedbackMsg.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of feedbackComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEnd() {
  //------Ending Routine 'feedback'-------
  for (const thisComponent of feedbackComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var scoreText;
var doneKey;
var finalScoreComponents;
function finalScoreRoutineBegin() {
  //------Prepare to start Routine 'finalScore'-------
  t = 0;
  finalScoreClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  scoreText="Well done! You banked a total of\n£" + bankedEarnings.toFixed(2);
  finalScore_2.setText(scoreText);
  doneKey = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  finalScoreComponents = [];
  finalScoreComponents.push(finalScore_2);
  finalScoreComponents.push(doneKey);
  
  for (const thisComponent of finalScoreComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function finalScoreRoutineEachFrame() {
  //------Loop for each frame of Routine 'finalScore'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = finalScoreClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *finalScore_2* updates
  if (t >= 0.0 && finalScore_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    finalScore_2.tStart = t;  // (not accounting for frame time here)
    finalScore_2.frameNStart = frameN;  // exact frame index
    finalScore_2.setAutoDraw(true);
  }

  
  // *doneKey* updates
  if (t >= 0.0 && doneKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    doneKey.tStart = t;  // (not accounting for frame time here)
    doneKey.frameNStart = frameN;  // exact frame index
    doneKey.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { doneKey.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (doneKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys();
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      doneKey.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      doneKey.rt = doneKey.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of finalScoreComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function finalScoreRoutineEnd() {
  //------Ending Routine 'finalScore'-------
  for (const thisComponent of finalScoreComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (doneKey.keys === undefined || doneKey.keys.length === 0) {    // No response was made
      doneKey.keys = undefined;
  }
  
  psychoJS.experiment.addData('doneKey.keys', doneKey.keys);
  if (typeof doneKey.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('doneKey.rt', doneKey.rt);
      routineTimer.reset();
      }
  
  // the Routine "finalScore" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisScheduler, thisTrial) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
