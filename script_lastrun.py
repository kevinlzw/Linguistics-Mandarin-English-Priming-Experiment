#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on 二月 08, 2020, at 17:34
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, microphone
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'script'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\kevin\\Documents\\Spring 2020\\Psy Independent Study\\PsychoPy Script\\script_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instructiontext = visual.TextStim(win=win, name='instructiontext',
    text="Hello!\n\nWelcome to join this experiment. \n\nPlease type 'space' for going to the next page",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instruction = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
text1 = visual.TextStim(win=win, name='text1',
    text='default text',
    font='Arial',
    pos=(-0.75, 0), height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sound1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound1')
sound1.setVolume(1)
text2 = visual.TextStim(win=win, name='text2',
    text='default text',
    font='Arial',
    pos=(-0.25, 0), height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sound2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound2')
sound2.setVolume(1)
prime_text = visual.TextStim(win=win, name='prime_text',
    text='default text',
    font='Arial',
    pos=(0.25, 0), height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
prime_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='prime_sound')
prime_sound.setVolume(1)
target_text = visual.TextStim(win=win, name='target_text',
    text='default text',
    font='Arial',
    pos=(0.75, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
record_notification = visual.TextStim(win=win, name='record_notification',
    text='default text',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
End_text = visual.TextStim(win=win, name='End_text',
    text='This is the end of the experiment session. \nThank you for your time and cooperation. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
# update component parameters for each repeat
key_resp_instruction.keys = []
key_resp_instruction.rt = []
# keep track of which components have finished
instructionComponents = [instructiontext, key_resp_instruction]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructiontext* updates
    if instructiontext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructiontext.frameNStart = frameN  # exact frame index
        instructiontext.tStart = t  # local t and not account for scr refresh
        instructiontext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructiontext, 'tStartRefresh')  # time at next scr refresh
        instructiontext.setAutoDraw(True)
    
    # *key_resp_instruction* updates
    waitOnFlip = False
    if key_resp_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruction.frameNStart = frameN  # exact frame index
        key_resp_instruction.tStart = t  # local t and not account for scr refresh
        key_resp_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruction, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruction.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruction.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instruction.keys = theseKeys.name  # just the last key pressed
            key_resp_instruction.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructiontext.started', instructiontext.tStartRefresh)
thisExp.addData('instructiontext.stopped', instructiontext.tStopRefresh)
# check responses
if key_resp_instruction.keys in ['', [], None]:  # No response was made
    key_resp_instruction.keys = None
thisExp.addData('key_resp_instruction.keys',key_resp_instruction.keys)
if key_resp_instruction.keys != None:  # we had a response
    thisExp.addData('key_resp_instruction.rt', key_resp_instruction.rt)
thisExp.addData('key_resp_instruction.started', key_resp_instruction.tStartRefresh)
thisExp.addData('key_resp_instruction.stopped', key_resp_instruction.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    text1.setText(word1)
    sound1.setSound(wrecord1, secs=4.0, hamming=True)
    sound1.setVolume(1, log=False)
    text2.setText(word2)
    sound2.setSound(wrecord2, secs=4.0, hamming=True)
    sound2.setVolume(1, log=False)
    prime_text.setText(prime
)
    prime_sound.setSound(precord3, secs=4, hamming=True)
    prime_sound.setVolume(1, log=False)
    target_text.setText(target)
    pan_record = microphone.AdvAudioCapture(name='pan_record', saveDir=wavDirName, stereo=False, chnl=0)
    record_notification.setText('Please say the word: pan')
    # keep track of which components have finished
    trialComponents = [text1, sound1, text2, sound2, prime_text, prime_sound, target_text, pan_record, record_notification]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text1* updates
        if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            text1.setAutoDraw(True)
        if text1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text1.tStartRefresh + 16.0-frameTolerance:
                # keep track of stop time/frame for later
                text1.tStop = t  # not accounting for scr refresh
                text1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                text1.setAutoDraw(False)
        # start/stop sound1
        if sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound1.frameNStart = frameN  # exact frame index
            sound1.tStart = t  # local t and not account for scr refresh
            sound1.tStartRefresh = tThisFlipGlobal  # on global time
            sound1.play(when=win)  # sync with win flip
        if sound1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound1.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                sound1.tStop = t  # not accounting for scr refresh
                sound1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound1, 'tStopRefresh')  # time at next scr refresh
                sound1.stop()
        
        # *text2* updates
        if text2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            text2.frameNStart = frameN  # exact frame index
            text2.tStart = t  # local t and not account for scr refresh
            text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text2, 'tStartRefresh')  # time at next scr refresh
            text2.setAutoDraw(True)
        if text2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text2.tStartRefresh + 12.0-frameTolerance:
                # keep track of stop time/frame for later
                text2.tStop = t  # not accounting for scr refresh
                text2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text2, 'tStopRefresh')  # time at next scr refresh
                text2.setAutoDraw(False)
        # start/stop sound2
        if sound2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            sound2.frameNStart = frameN  # exact frame index
            sound2.tStart = t  # local t and not account for scr refresh
            sound2.tStartRefresh = tThisFlipGlobal  # on global time
            sound2.play(when=win)  # sync with win flip
        if sound2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound2.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                sound2.tStop = t  # not accounting for scr refresh
                sound2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound2, 'tStopRefresh')  # time at next scr refresh
                sound2.stop()
        
        # *prime_text* updates
        if prime_text.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
            # keep track of start time/frame for later
            prime_text.frameNStart = frameN  # exact frame index
            prime_text.tStart = t  # local t and not account for scr refresh
            prime_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prime_text, 'tStartRefresh')  # time at next scr refresh
            prime_text.setAutoDraw(True)
        if prime_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prime_text.tStartRefresh + 8.0-frameTolerance:
                # keep track of stop time/frame for later
                prime_text.tStop = t  # not accounting for scr refresh
                prime_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prime_text, 'tStopRefresh')  # time at next scr refresh
                prime_text.setAutoDraw(False)
        # start/stop prime_sound
        if prime_sound.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            prime_sound.frameNStart = frameN  # exact frame index
            prime_sound.tStart = t  # local t and not account for scr refresh
            prime_sound.tStartRefresh = tThisFlipGlobal  # on global time
            prime_sound.play(when=win)  # sync with win flip
        if prime_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prime_sound.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                prime_sound.tStop = t  # not accounting for scr refresh
                prime_sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prime_sound, 'tStopRefresh')  # time at next scr refresh
                prime_sound.stop()
        
        # *target_text* updates
        if target_text.status == NOT_STARTED and tThisFlip >= 13.0-frameTolerance:
            # keep track of start time/frame for later
            target_text.frameNStart = frameN  # exact frame index
            target_text.tStart = t  # local t and not account for scr refresh
            target_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_text, 'tStartRefresh')  # time at next scr refresh
            target_text.setAutoDraw(True)
        if target_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_text.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                target_text.tStop = t  # not accounting for scr refresh
                target_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_text, 'tStopRefresh')  # time at next scr refresh
                target_text.setAutoDraw(False)
        
        # *pan_record* updates
        if pan_record.status == NOT_STARTED and t >= 13.0-frameTolerance:
            # keep track of start time/frame for later
            pan_record.frameNStart = frameN  # exact frame index
            pan_record.tStart = t  # local t and not account for scr refresh
            pan_record.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pan_record, 'tStartRefresh')  # time at next scr refresh
            pan_record.status = STARTED
            pan_record.record(sec=4.0, block=False)  # start the recording thread
        
        if pan_record.status == STARTED and not pan_record.recorder.running:
            pan_record.status = FINISHED
        
        # *record_notification* updates
        if record_notification.status == NOT_STARTED and tThisFlip >= 13.0-frameTolerance:
            # keep track of start time/frame for later
            record_notification.frameNStart = frameN  # exact frame index
            record_notification.tStart = t  # local t and not account for scr refresh
            record_notification.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(record_notification, 'tStartRefresh')  # time at next scr refresh
            record_notification.setAutoDraw(True)
        if record_notification.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > record_notification.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                record_notification.tStop = t  # not accounting for scr refresh
                record_notification.frameNStop = frameN  # exact frame index
                win.timeOnFlip(record_notification, 'tStopRefresh')  # time at next scr refresh
                record_notification.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text1.started', text1.tStartRefresh)
    trials.addData('text1.stopped', text1.tStopRefresh)
    sound1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound1.started', sound1.tStartRefresh)
    trials.addData('sound1.stopped', sound1.tStopRefresh)
    trials.addData('text2.started', text2.tStartRefresh)
    trials.addData('text2.stopped', text2.tStopRefresh)
    sound2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound2.started', sound2.tStartRefresh)
    trials.addData('sound2.stopped', sound2.tStopRefresh)
    trials.addData('prime_text.started', prime_text.tStartRefresh)
    trials.addData('prime_text.stopped', prime_text.tStopRefresh)
    prime_sound.stop()  # ensure sound has stopped at end of routine
    trials.addData('prime_sound.started', prime_sound.tStartRefresh)
    trials.addData('prime_sound.stopped', prime_sound.tStopRefresh)
    trials.addData('target_text.started', target_text.tStartRefresh)
    trials.addData('target_text.stopped', target_text.tStopRefresh)
    # pan_record stop & responses
    pan_record.stop()  # sometimes helpful
    if not pan_record.savedFile:
        pan_record.savedFile = None
    # store data for trials (TrialHandler)
    trials.addData('pan_record.filename', pan_record.savedFile)
    trials.addData('pan_record.started', pan_record.tStart)
    trials.addData('pan_record.stopped', pan_record.tStop)
    trials.addData('record_notification.started', record_notification.tStartRefresh)
    trials.addData('record_notification.stopped', record_notification.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# ------Prepare to start Routine "End"-------
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [End_text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_text* updates
    if End_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_text.frameNStart = frameN  # exact frame index
        End_text.tStart = t  # local t and not account for scr refresh
        End_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_text, 'tStartRefresh')  # time at next scr refresh
        End_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('End_text.started', End_text.tStartRefresh)
thisExp.addData('End_text.stopped', End_text.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
