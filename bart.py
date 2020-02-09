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
from psychopy import gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
import os  # handy system and path functions
import init
import format_datafile

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
init.generate_excel()
# Store info about the experiment session
psychopyVersion = '3.0.3'
expName = 'bart'  # from the Builder filename that created this script
expInfo = {'participant': '', 'gender (m/f)': '', 'age': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if not dlg.OK:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
# expInfo['expName'] = expName
# expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
expInfo['date'] = expInfo['date'][4:].replace('_', '', 1)
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s_%s_%s' % (expInfo['participant'], expInfo['gender (m/f)'], expInfo['age'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=_thisDir,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
# logFile = logging.LogFile(filename + '.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='gainsboro', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
# expInfo['frameRate'] = win.getActualFrameRate()
# if expInfo['frameRate'] is not None:
#     frameDur = 1.0 / round(expInfo['frameRate'])
# else:
#     frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrMessage = visual.TextStim(win=win, name='instrMessage',
                               text="This is a game where you have to optimise your earnings"
                                    " in a balloon pumping competition.\nThroughout the task, you will be presented "
                                    "with 90 balloons, one at the time. You can pump it to increase its size."
                                    " \nYou will accumulate 5 cents "
                                    "in a temporary bank for each pump. But if you pump it too far it will"
                                    " pop and you'll get nothing for that balloon.\n\nBalloons differ in their"
                                    "\n-Maximum size:\tThey can occasionally reach to almost the size of the screen"
                                    " but most\n\t\t\t\twill pop well before that."
                                    "\n-Color:\t\t\tThe explosion point varies across balloons\n\n"
                                    "Press\n    [SPACE] to pump the balloon\n    [RETURN] to keep accumulated cash"
                                    " for this balloon and move onto the next balloon\n",
                               font='Arial',
                               units='height', pos=[0, 0], height=0.025, wrapWidth=None, ori=0,
                               color='black', colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=0.0)

credits = visual.TextStim(win=win, name='credits',
        text='Credits: Kevin Barba (based on pavlovia.org/demos/bart)\
        \n\t  Department of Electrical and Computer Engineering\
        \n\t  University of Texas at San Antonio\
        \n\t  Summer 2019',
                              font='Arial',
                              # alignHoriz='center', alignVert='top',
                              pos=(.7, -.9),
                              color='black', colorSpace='rgb', opacity=1, height=0.03,
                              languageStyle='LTR')

# Initialize components for Routine "trial"
trialClock = core.Clock()
bankedEarnings = 0.0
balloonEarnings = ''
bankedText = ''
lastBalloonEarnings = 0.0
thisBalloonEarnings = 0.0
balloonSize = 0.08
balloonMsgHeight = 0.01

redBalloon = visual.ImageStim(
    win=win, name='red', units='height',
    image='redBalloon.png', mask=None,
    ori=-90, pos=[0, 0], size=1.0,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
greenBalloon = visual.ImageStim(
    win=win, name='green', units='height',
    image='greenBalloon.png', mask=None,
    ori=-90, pos=[0, 0], size=1.0,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
blueBalloon = visual.ImageStim(
    win=win, name='blue', units='height',
    image='blueBalloon.png', mask=None,
    ori=-90, pos=[0, 0], size=1.0,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
balloons = [redBalloon, greenBalloon, blueBalloon]
balloonsCount = [30, 30, 30]
RED_BALLOON = 0
GREEN_BALLOON = 1
BLUE_BALLOON = 2

#
# def get_random_balloon():
#     while True:
#         randomize = randint(0, 3)
#         if balloonsCount[randomize] > 0:
#             break
#     balloonsCount[randomize] -= 1
#     return balloons[randomize], get_random_pumps(randomize)
#
#
# def get_random_pumps(ballooncolor=RED_BALLOON):
#     if ballooncolor == RED_BALLOON:
#         return randint(1, 9)
#     elif ballooncolor == GREEN_BALLOON:
#         return randint(1, 33)
#     elif ballooncolor == BLUE_BALLOON:
#         return randint(1, 65)
#     else:
#         raise Exception("[Error] Balloon not identified")
#         return


reminderMsg = visual.TextStim(win=win, name='reminderMsg',
                              text='Press SPACE to pump the balloon\nPress RETURN to bank this sum',
                              font='Arial',
                              units='height', pos=[0, -0.8], height=0.025, wrapWidth=None, ori=0,
                              color='black', colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-3.0)
balloonValMsg = visual.TextStim(win=win, name='balloonValMsg',
                                text='default text',
                                font='Arial',
                                units='height', pos=[0, 0.05], height=0.025, wrapWidth=None, ori=0,
                                color='black', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=-4.0)
bankedMsg = visual.TextStim(win=win, name='bankedMsg',
                            text='default text',
                            font='Arial',
                            units='height', pos=[0, 0.8], height=0.025, wrapWidth=None, ori=0,
                            color='black', colorSpace='rgb', opacity=1,
                            languageStyle='LTR',
                            depth=-5.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
from psychopy import sound

feedbackText = ""
bang = sound.Sound("bang.wav")
cash = sound.Sound("cash.wav")


moneyEarned = visual.TextStim(win=win, name='moneyEarned',
                              text='default text',
                              font='Arial',
                              # alignHoriz='center', alignVert='top',
                              pos=(.7, .5),
                              color='black', colorSpace='rgb', opacity=1, height=0.05,
                              languageStyle='LTR')

controlKeys = visual.TextStim(win=win, name='controlKeys',
                              text='default text',
                              font='Arial',
                              # alignHoriz='center', alignVert='top',
                              pos=(-.7, -.9),
                              color='black', colorSpace='rgb', opacity=1, height=0.05,
                              languageStyle='LTR')

counter = visual.TextStim(win=win, name='counter',
                              text='default text',
                              font='Arial',
                              # alignHoriz='center', alignVert='top',
                              pos=(-.7, .9),
                              color='black', colorSpace='rgb', opacity=1, height=0.05,
                              languageStyle='LTR')

feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
                              text='default text',
                              font='Arial',
                              units='height', pos=[0, 0], height=0.025, wrapWidth=None, ori=0,
                              color='black', colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)

# Initialize components for Routine "finalScore"
finalScoreClock = core.Clock()

finalScore_2 = visual.TextStim(win=win, name='finalScore_2',
                               text='default text',
                               font='Arial',
                               units='height', pos=[0, 0], height=0.025, wrapWidth=None, ori=0,
                               color='black', colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=-1.0)

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
instructionsComponents = [instrMessage, resp, credits]
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
        credits.setAutoDraw(True)

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
        if hasattr(thisComponent, "status") and thisComponent.status is not FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# thisExp.addData('instrMessage.started', instrMessage.tStartRefresh)
# thisExp.addData('instrMessage.stopped', instrMessage.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential',
                           extraInfo=expInfo,
                           originPath=-1,
                           trialList=data.importConditions('trialTypes.xlsx'),
                           seed=1832, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
thisTrial['time'] = 0
print(thisTrial)
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
# if thisTrial is not None:
#     for paramName in thisTrial:
#         exec('{} = thisTrial[paramName]'.format(paramName))

balloonCounter = 0

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial is not None:
        for paramName in thisTrial:
            # get random balloon
            exec_string = '{} = {}'.format(paramName, thisTrial[paramName])
            exec(exec_string)
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat

    balloonSize = 0.08
    popped = False
    nPumps = 0
    balloonCounter += 1

    bankButton = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [randomBalloon, reminderMsg, balloonValMsg, bankedMsg, bankButton]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    while continueRoutine:

        moneyEarnedText = u"Total Money in Bank $%.2f" % bankedEarnings
        moneyEarned.setText(moneyEarnedText)
        moneyEarned.setAutoDraw(True)

        controlKeysText = u"[SPACE] = pump balloon\n[RETURN] = cash out current balloon"
        controlKeys.setText(controlKeysText)
        controlKeys.setAutoDraw(True)

        counterText = u" %d out of %d Balloons remaining" % (balloonCounter, 90)
        counter.setText(counterText)
        counter.setAutoDraw(True)

        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        thisBalloonEarnings = nPumps * 0.05
        balloonEarnings = u"This %s balloon value:\n$%.2f" % (randomBalloon.name, thisBalloonEarnings)
        bankedText = u"You cash out:\n$%.2f" % bankedEarnings
        balloonSize = 0.1 + nPumps * 0.015

        # *balloonBody* updates
        if t >= 0.0 and randomBalloon.status == NOT_STARTED:
            # keep track of start time/frame for later
            randomBalloon.tStart = t  # not accounting for scr refresh
            randomBalloon.frameNStart = frameN  # exact frame indexB
            win.timeOnFlip(randomBalloon, 'tStartRefresh')  # time at next scr refresh
            randomBalloon.setAutoDraw(True)
        if randomBalloon.status == STARTED:  # only update if drawing
            randomBalloon.setPos([0, balloonSize / 2 - .5], log=False)
            randomBalloon.setSize(balloonSize, log=False)

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
            nPumps = nPumps + 1
            if nPumps > maxPumps:
                popped = True
                continueRoutine = False
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
            if hasattr(thisComponent, "status") and thisComponent.status is not FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # calculate cash 'earned'
    if popped:
        thisBalloonEarnings = 0.0
        lastBalloonEarnings = 0.0
    else:
        lastBalloonEarnings = thisBalloonEarnings
    bankedEarnings = bankedEarnings + lastBalloonEarnings
    # save data
    trials.addData('nPumps', nPumps)
    trials.addData('size', balloonSize)
    trials.addData('earnings', thisBalloonEarnings)
    trials.addData('popped', popped)
    trials.addData('time', '{0:.2f}'.format(round(t, 2)))
    # @TODO get time
    print(t)

    # trials.addData('balloonBody.started', randomBalloon.tStartRefresh)
    # trials.addData('balloonBody.stopped', randomBalloon.tStopRefresh)
    # trials.addData('reminderMsg.started', reminderMsg.tStartRefresh)
    # trials.addData('reminderMsg.stopped', reminderMsg.tStopRefresh)
    # trials.addData('balloonValMsg.started', balloonValMsg.tStartRefresh)
    # trials.addData('balloonValMsg.stopped', balloonValMsg.tStopRefresh)
    # trials.addData('bankedMsg.started', bankedMsg.tStartRefresh)
    # trials.addData('bankedMsg.stopped', bankedMsg.tStopRefresh)

    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if popped:
        feedbackText = "Oops! Lost that one!"
        bang.play()
    else:
        feedbackText = u"You cash out $%.2f" % lastBalloonEarnings
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
        frameRemains = 0.0 + 1.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedbackMsg.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            feedbackMsg.tStop = t  # not accounting for scr refresh
            feedbackMsg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedbackMsg, 'tStopRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            format_datafile.delete_unused_columns(filename + '.csv')
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status is not FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # trials.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
    # trials.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
# trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
#                    stimOut=params,
#                    dataOut=['n', 'all_mean', 'all_std', 'all_raw'])

# ------Prepare to start Routine "finalScore"-------
t = 0
finalScoreClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scoreText = u"Well done! Game finished"
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
        format_datafile.delete_unused_columns(filename + '.csv')
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status is not FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finalScore"-------
for thisComponent in finalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# thisExp.addData('finalScore_2.started', finalScore_2.tStartRefresh)
# thisExp.addData('finalScore_2.stopped', finalScore_2.tStopRefresh)
# check responses
if doneKey.keys in ['', [], None]:  # No response was made
    doneKey.keys = None
# thisExp.addData('doneKey.keys', doneKey.keys)

if doneKey.keys is not None:  # we had a response
    thisExp.addData('doneKey.rt', doneKey.rt)
# thisExp.addData('doneKey.started', doneKey.tStartRefresh)
# thisExp.addData('doneKey.stopped', doneKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "finalScore" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv')
format_datafile.delete_unused_columns(filename + '.csv')
# thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
format_datafile.delete_unused_columns(filename + '.csv')
core.quit()
