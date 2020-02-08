/*************** 
 * Script Test *
 ***************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'script';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(instructionRoutineBegin);
flowScheduler.add(instructionRoutineEachFrame);
flowScheduler.add(instructionRoutineEnd);
flowScheduler.add(trialRoutineBegin);
flowScheduler.add(trialRoutineEachFrame);
flowScheduler.add(trialRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var instructionClock;
var instructiontext;
var key_resp_instruction;
var trialClock;
var Eye_text;
var Eye_sound;
var cap_text;
var cap_sound;
var pun_text;
var pun_sound;
var pan_text;
var pan;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  instructiontext = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructiontext',
    text: "Hello!\n\nWelcome to join this experiment. \n\nPlease type 'space' for going to the next page",
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_instruction = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Eye_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Eye_text',
    text: 'Eye',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.75), 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  Eye_sound = new Sound({
    win: psychoJS.window,
    value: 'C:\\Users\\kevin\\Documents\\Spring 2020\\Psy Independent Study\\Eye.wav',
    secs: (- 1),
    });
  Eye_sound.setVolume(1);
  cap_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'cap_text',
    text: 'Cap',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.25), 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: -2.0 
  });
  
  cap_sound = new Sound({
    win: psychoJS.window,
    value: 'C:\\Users\\kevin\\Documents\\Spring 2020\\Psy Independent Study\\Cap.wav',
    secs: (- 1),
    });
  cap_sound.setVolume(1);
  pun_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'pun_text',
    text: 'Pun',
    font: 'Arial',
    units : undefined, 
    pos: [0.25, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: -4.0 
  });
  
  pun_sound = new Sound({
    win: psychoJS.window,
    value: 'C:\\Users\\kevin\\Documents\\Spring 2020\\Psy Independent Study\\Pun.wav',
    secs: (- 1),
    });
  pun_sound.setVolume(1);
  pan_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'pan_text',
    text: '潘',
    font: 'Arial',
    units : undefined, 
    pos: [0.75, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -6.0 
  });
  
  pan = new Sound({
    win: psychoJS.window,
    value: 'C:\\Users\\kevin\\Documents\\Spring 2020\\Psy Independent Study\\pan.wav',
    secs: (- 1),
    });
  pan.setVolume(1);
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var instructionComponents;
function instructionRoutineBegin() {
  //------Prepare to start Routine 'instruction'-------
  t = 0;
  instructionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_instruction.keys = undefined;
  key_resp_instruction.rt = undefined;
  // keep track of which components have finished
  instructionComponents = [];
  instructionComponents.push(instructiontext);
  instructionComponents.push(key_resp_instruction);
  
  instructionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instructionRoutineEachFrame() {
  //------Loop for each frame of Routine 'instruction'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instructiontext* updates
  if (t >= 0.0 && instructiontext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructiontext.tStart = t;  // (not accounting for frame time here)
    instructiontext.frameNStart = frameN;  // exact frame index
    instructiontext.setAutoDraw(true);
  }

  
  // *key_resp_instruction* updates
  if (t >= 0.0 && key_resp_instruction.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_instruction.tStart = t;  // (not accounting for frame time here)
    key_resp_instruction.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_instruction.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_instruction.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_instruction.clearEvents(); });
  }

  if (key_resp_instruction.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_instruction.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_instruction.keys = theseKeys[0].name;  // just the last key pressed
      key_resp_instruction.rt = theseKeys[0].rt;
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
  instructionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instructionRoutineEnd() {
  //------Ending Routine 'instruction'-------
  instructionComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_instruction.keys', key_resp_instruction.keys);
  if (typeof key_resp_instruction.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_instruction.rt', key_resp_instruction.rt);
      routineTimer.reset();
      }
  
  key_resp_instruction.stop();
  // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  Eye_sound.secs=4.0;
  Eye_sound.setVolume(1);
  cap_sound.secs=4.0;
  cap_sound.setVolume(1);
  pun_sound.secs=4;
  pun_sound.setVolume(1);
  pan.secs=4.0;
  pan.setVolume(1);
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(Eye_text);
  trialComponents.push(Eye_sound);
  trialComponents.push(cap_text);
  trialComponents.push(cap_sound);
  trialComponents.push(pun_text);
  trialComponents.push(pun_sound);
  trialComponents.push(pan_text);
  trialComponents.push(pan);
  
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Eye_text* updates
  if (t >= 0.0 && Eye_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Eye_text.tStart = t;  // (not accounting for frame time here)
    Eye_text.frameNStart = frameN;  // exact frame index
    Eye_text.setAutoDraw(true);
  }

  // start/stop Eye_sound
  if (t >= 0.0 && Eye_sound.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Eye_sound.tStart = t;  // (not accounting for frame time here)
    Eye_sound.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ Eye_sound.play(); });  // screen flip
    Eye_sound.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Eye_sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (4.0 > 0.5) {  Eye_sound.stop();  // stop the sound (if longer than duration)
      Eye_sound.status = PsychoJS.Status.FINISHED;
    }
  }
  
  // *cap_text* updates
  if (t >= 4.0 && cap_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cap_text.tStart = t;  // (not accounting for frame time here)
    cap_text.frameNStart = frameN;  // exact frame index
    cap_text.setAutoDraw(true);
  }

  // start/stop cap_sound
  if (t >= 4.0 && cap_sound.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cap_sound.tStart = t;  // (not accounting for frame time here)
    cap_sound.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ cap_sound.play(); });  // screen flip
    cap_sound.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 4.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cap_sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (4.0 > 0.5) {  cap_sound.stop();  // stop the sound (if longer than duration)
      cap_sound.status = PsychoJS.Status.FINISHED;
    }
  }
  
  // *pun_text* updates
  if (t >= 8.0 && pun_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pun_text.tStart = t;  // (not accounting for frame time here)
    pun_text.frameNStart = frameN;  // exact frame index
    pun_text.setAutoDraw(true);
  }

  // start/stop pun_sound
  if (t >= 8 && pun_sound.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pun_sound.tStart = t;  // (not accounting for frame time here)
    pun_sound.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ pun_sound.play(); });  // screen flip
    pun_sound.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 8 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (pun_sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (4 > 0.5) {  pun_sound.stop();  // stop the sound (if longer than duration)
      pun_sound.status = PsychoJS.Status.FINISHED;
    }
  }
  
  // *pan_text* updates
  if (t >= 12.0 && pan_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pan_text.tStart = t;  // (not accounting for frame time here)
    pan_text.frameNStart = frameN;  // exact frame index
    pan_text.setAutoDraw(true);
  }

  // start/stop pan
  if (t >= 12.0 && pan.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pan.tStart = t;  // (not accounting for frame time here)
    pan.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ pan.play(); });  // screen flip
    pan.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 12.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (pan.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (4.0 > 0.5) {  pan.stop();  // stop the sound (if longer than duration)
      pan.status = PsychoJS.Status.FINISHED;
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
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
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
  trialComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  Eye_sound.stop();  // ensure sound has stopped at end of routine
  cap_sound.stop();  // ensure sound has stopped at end of routine
  pun_sound.stop();  // ensure sound has stopped at end of routine
  pan.stop();  // ensure sound has stopped at end of routine
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
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
