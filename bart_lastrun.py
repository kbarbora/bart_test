#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on February 07, 2019, at 11:16
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.3'
expName = 'bart'  # from the Builder filename that created this script
expInfo = {'participant': '', 'gender (m/f)': '', 'age': '', 'session': '004'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\lpzdb\\pavloviaDemos\\BART\\bart_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrMessage = visual.TextStim(win=win, name='instrMessage',
    text="This is a game where you have to optimise your earnings in a balloon pumping competition.\n\nYou get prize money for each balloon you pump up, according to its size. But if you pump it too far it will pop and you'll get nothing for that balloon.\n\nBalloons differ in their maximum size - they can occasionally reach to almost the size of the screen but most will pop well before that.\n\nPress\n    SPACE to pump the balloon\n    RETURN to bank the cash for this balloon and move onto the next\n",
    font='Arial',
    units='height', pos=[0, 0], height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
bankedEarnings=0.0
balloonEarnings = ''
bankedText = ''
lastBalloonEarnings=0.0
thisBalloonEarnings=0.0
balloonSize=0.08
balloonMsgHeight=0.01
balloonBody = visual.ImageStim(
    win=win, name='balloonBody',units='height', 
    image='blueBalloon.png', mask=None,
    ori=-90, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
reminderMsg = visual.TextStim(win=win, name='reminderMsg',
    text='Press SPACE to pump the balloon\nPress RETURN to bank this sum',
    font='Arial',
    units='height', pos=[0, -0.8], height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
balloonValMsg = visual.TextStim(win=win, name='balloonValMsg',
    text='default text',
    font='Arial',
    units='height', pos=[0,0.05], height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
bankedMsg = visual.TextStim(win=win, name='bankedMsg',
    text='default text',
    font='Arial',
    units='height', pos=[0, 0.8], height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
from psychopy import sound
feedbackText=""
bang = sound.Sound("bang.wav")
cash = sound.Sound("cash.wav")

feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    units='height', pos=[0, 0], height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "finalScore"
finalScoreClock = core.Clock()

finalScore_2 = visual.TextStim(win=win, name='finalScore_2',
    text='default text',
    font='Arial',
    units='height', pos=[0, 0], height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instrMessage, resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrMessage* updates
    if t >= 0.0 and instrMessage.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrMessage.tStart = t  # not accounting for scr refresh
        instrMessage.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instrMessage, 'tStartRefresh')  # time at next scr refresh
        instrMessage.setAutoDraw(True)
    
    # *resp* updates
    if t >= 0.0 and resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp.tStart = t  # not accounting for scr refresh
        resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
        resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrMessage.started', instrMessage.tStartRefresh)
thisExp.addData('instrMessage.stopped', instrMessage.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=1832, name='trials')
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
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    balloonSize = 0.08
    popped = False
    nPumps = 0
    
    bankButton = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [balloonBody, reminderMsg, balloonValMsg, bankedMsg, bankButton]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        thisBalloonEarnings=nPumps*0.05
        balloonEarnings = u"This balloon value:\n$%.2f" % thisBalloonEarnings
        bankedText = u"You have banked:\n$%.2f" % bankedEarnings
        balloonSize=0.1+nPumps*0.015
        
        # *balloonBody* updates
        if t >= 0.0 and balloonBody.status == NOT_STARTED:
            # keep track of start time/frame for later
            balloonBody.tStart = t  # not accounting for scr refresh
            balloonBody.frameNStart = frameN  # exact frame index
            win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
            balloonBody.setAutoDraw(True)
        if balloonBody.status == STARTED:  # only update if drawing
            balloonBody.setPos([0, balloonSize/2-.5], log=False)
            balloonBody.setSize(balloonSize, log=False)
        
        # *reminderMsg* updates
        if t >= 0.0 and reminderMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            reminderMsg.tStart = t  # not accounting for scr refresh
            reminderMsg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(reminderMsg, 'tStartRefresh')  # time at next scr refresh
            reminderMsg.setAutoDraw(True)
        
        # *balloonValMsg* updates
        if t >= 0.0 and balloonValMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            balloonValMsg.tStart = t  # not accounting for scr refresh
            balloonValMsg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(balloonValMsg, 'tStartRefresh')  # time at next scr refresh
            balloonValMsg.setAutoDraw(True)
        if balloonValMsg.status == STARTED:  # only update if drawing
            balloonValMsg.setText(balloonEarnings, log=False)
        
        # *bankedMsg* updates
        if t >= 0.0 and bankedMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            bankedMsg.tStart = t  # not accounting for scr refresh
            bankedMsg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(bankedMsg, 'tStartRefresh')  # time at next scr refresh
            bankedMsg.setAutoDraw(True)
        if bankedMsg.status == STARTED:  # only update if drawing
            bankedMsg.setText(bankedText, log=False)
        if event.getKeys(['space']):
          nPumps=nPumps+1
          if nPumps > maxPumps:
            popped = True
            continueRoutine=False
        if event.getKeys(['return']):
            popped = False
            continueRoutine = False
        
        # *bankButton* updates
        if t >= 0.0 and bankButton.status == NOT_STARTED:
            # keep track of start time/frame for later
            bankButton.tStart = t  # not accounting for scr refresh
            bankButton.frameNStart = frameN  # exact frame index
            win.timeOnFlip(bankButton, 'tStartRefresh')  # time at next scr refresh
            bankButton.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if bankButton.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    #calculate cash 'earned'
    if popped:
      thisBalloonEarnings = 0.0
      lastBalloonEarnings = 0.0
    else:
        lastBalloonEarnings = thisBalloonEarnings
    bankedEarnings = bankedEarnings+lastBalloonEarnings
    #save data
    trials.addData('nPumps', nPumps)
    trials.addData('size', balloonSize)
    trials.addData('earnings', thisBalloonEarnings)
    trials.addData('popped', popped)
    
    
    trials.addData('balloonBody.started', balloonBody.tStartRefresh)
    trials.addData('balloonBody.stopped', balloonBody.tStopRefresh)
    trials.addData('reminderMsg.started', reminderMsg.tStartRefresh)
    trials.addData('reminderMsg.stopped', reminderMsg.tStopRefresh)
    trials.addData('balloonValMsg.started', balloonValMsg.tStartRefresh)
    trials.addData('balloonValMsg.stopped', balloonValMsg.tStopRefresh)
    trials.addData('bankedMsg.started', bankedMsg.tStartRefresh)
    trials.addData('bankedMsg.stopped', bankedMsg.tStopRefresh)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if popped==True:
      feedbackText="Oops! Lost that one!"
      bang.play()
    else:
      feedbackText=u"You banked $%.2f" %lastBalloonEarnings
      cash.play()
    
    feedbackMsg.setText(feedbackText)
    # keep track of which components have finished
    feedbackComponents = [feedbackMsg]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedbackMsg* updates
        if t >= 0.0 and feedbackMsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackMsg.tStart = t  # not accounting for scr refresh
            feedbackMsg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(feedbackMsg, 'tStartRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedbackMsg.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            feedbackMsg.tStop = t  # not accounting for scr refresh
            feedbackMsg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedbackMsg, 'tStopRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    trials.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
    trials.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finalScore"-------
t = 0
finalScoreClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scoreText=u"Well done! You banked a total of\n$%2.f" % bankedEarnings
finalScore_2.setText(scoreText)
doneKey = event.BuilderKeyResponse()
# keep track of which components have finished
finalScoreComponents = [finalScore_2, doneKey]
for thisComponent in finalScoreComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "finalScore"-------
while continueRoutine:
    # get current time
    t = finalScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *finalScore_2* updates
    if t >= 0.0 and finalScore_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        finalScore_2.tStart = t  # not accounting for scr refresh
        finalScore_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(finalScore_2, 'tStartRefresh')  # time at next scr refresh
        finalScore_2.setAutoDraw(True)
    
    # *doneKey* updates
    if t >= 0.0 and doneKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        doneKey.tStart = t  # not accounting for scr refresh
        doneKey.frameNStart = frameN  # exact frame index
        win.timeOnFlip(doneKey, 'tStartRefresh')  # time at next scr refresh
        doneKey.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(doneKey.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if doneKey.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            doneKey.keys = theseKeys[-1]  # just the last key pressed
            doneKey.rt = doneKey.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finalScore"-------
for thisComponent in finalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

thisExp.addData('finalScore_2.started', finalScore_2.tStartRefresh)
thisExp.addData('finalScore_2.stopped', finalScore_2.tStopRefresh)
# check responses
if doneKey.keys in ['', [], None]:  # No response was made
    doneKey.keys=None
thisExp.addData('doneKey.keys',doneKey.keys)
if doneKey.keys != None:  # we had a response
    thisExp.addData('doneKey.rt', doneKey.rt)
thisExp.addData('doneKey.started', doneKey.tStartRefresh)
thisExp.addData('doneKey.stopped', doneKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "finalScore" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
