---
title: "Duplicate, Delete, and Create Motion Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm"
---

# Duplicate, Delete, and Create Motion Study Example (VBA)

This example shows how to create a duplicate motion study, delete an existing motion study, and create a new motion study.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document that has a motion study named
'    Motion Study 1 and a collapsed exploded view.
' 2. Verify that a ray-trace rendering engine is active.
' 3. Click Tools > References > SOLIDWORKS version Motion
'    Study Type Library.
' 4. Verify that c:\test exists.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Observe the graphics area.
' 2. Makes a copy of Motion Study 1 called Motion Study 2.
' 3. Deletes and creates a new motion study for Motion Study 1.
' 4. Runs the animation (i.e., rotates, explodes,
'    stops rotating, and collapses the assembly).
' 5. Saves the motion study as c:\test\Anim1.avi.
' 6. Examine the Immediate window.
' 7. Play c:\test\Anim1.avi.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMotionMgr As SwMotionStudy.MotionStudyManager
Dim swMotionStudy1 As SwMotionStudy.MotionStudy
Dim swSaveAVIData As SwMotionStudy.AVIParameter
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Get the MotionManager
    Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    If (swMotionMgr Is Nothing) Then
          End
    End If
```

```
    'Get the motion study named Motion Study 1
    Set swMotionStudy1 = swMotionMgr.GetMotionStudy("Motion Study 1")
    If (swMotionStudy1 Is Nothing) Then
        MsgBox "Motion Study 1 is not available."
        End
    End If
```

```
    'Create a copy of the motion study
    swMotionStudy1.Duplicate
```

```
    'Get the supported motion study types
    Dim MSTypes As Long
    boolstatus = swMotionStudy1.GetSupportedStudyTypes(MSTypes)
    Debug.Print ""
    Debug.Print "Supported study types: "
    Debug.Print "    Assembly: " & ((MSTypes And swMotionStudyType_e.swMotionStudyTypeAssembly) > 0)
    Debug.Print "    PhysicalSimulation: " & ((MSTypes And swMotionStudyType_e.swMotionStudyTypePhysicalSimulation) > 0)
    Debug.Print "    CosmosMotion: " & ((MSTypes And swMotionStudyType_e.swMotionStudyTypeCosmosMotion) > 0)
    Debug.Print "    LegacyCosmosMotion: " & ((MSTypes And swMotionStudyType_e.swMotionStudyTypeLegacyCosmosMotion) > 0)
```

```
    'Get the current motion study type
    Dim CurStudyType As Long
    CurStudyType = swMotionStudy1.StudyType
    Debug.Print ""
    Debug.Print "Current study type: "
    Select Case CurStudyType
        Case swMotionStudyType_e.swMotionStudyTypeAssembly
            Debug.Print "    Assembly"
        Case swMotionStudyType_e.swMotionStudyTypePhysicalSimulation
            Debug.Print "    PhysicalSimulation"
        Case swMotionStudyType_e.swMotionStudyTypeCosmosMotion
            Debug.Print "    CosmosMotion"
        Case swMotionStudyType_e.swMotionStudyTypeLegacyCosmosMotion
            Debug.Print "    LegacyCosmosMotion"
    End Select
```

```
    'Is the motion study active?  If not, activate it
    If Not swMotionStudy1.IsActive Then swMotionStudy1.Activate
```

```
    'Create an animation of the rotating model
    'Delete any existing animation sequences
    'Set the animation duration to 10 seconds
    boolstatus = swMotionStudy1.CreateByRotateModel(True, swAnimatorAxisOfRotation_e.swRotationAboutYAxis, 1, swAnimatorDirectionOfRotation_e.swRotationClockwise, 10, 0)
```

```
    'Play the animation
    PlayAnimation swMotionStudy1
```

```
    'Stop playing the animation
    swMotionStudy1.Stop
```

```
    'Add an explode to the animation
    'Set the animation duration to 5 seconds
    boolstatus = swMotionStudy1.CreateByExplode(False, 5, 0)
```

```
    'Add a collapse to the animation
    'Set the animation duration to 5 seconds
    boolstatus = swMotionStudy1.CreateByCollapse(False, 10, 5)
```

```
    'Set duration of animation to 15 seconds
    swMotionStudy1.SetDuration (15)
```

```
    'Play the animation
    PlayAnimation swMotionStudy1
```

```
    'Calculate
    swMotionStudy1.Calculate
```

```
    Debug.Print ""
    Debug.Print "Study duration: " & swMotionStudy1.GetDuration
```

```
    'Play animation
    PlayAnimation swMotionStudy1
```

```
    'Set and save AVI parameters
    Set swSaveAVIData = swMotionMgr.CreateAVIParameter()
    swSaveAVIData.FramePerSecond = 7.5
    swSaveAVIData.SaveEntireAnimation = True
    swSaveAVIData.OutputType = swAnimationOutputType_e.swAnimationOutput_AVI
    swSaveAVIData.RendererType = swRendererType_e.swRendererType_Solidworks_Screen
    swSaveAVIData.MotionBlur = True
    swSaveAVIData.BlurLength = 10
    swSaveAVIData.BlurOffset = -100
```

```
    swMotionStudy1.Stop
```

```
    'Save animation as .avi file
    swMotionStudy1.SaveToAVI "C:\test\Anim1.avi", swSaveAVIData
```

```
End Sub
```

```
Private Sub PlayAnimation(SwMotionStudy As SwMotionStudy.MotionStudy)
    Debug.Print ""
    Dim cPlayMode As Long
    Debug.Print "Current play mode: "
    cPlayMode = SwMotionStudy.PlayMode
```

```
    'Get current play mode
    Select Case cPlayMode
        Case 1
            Debug.Print "    Normal"
        Case 2
            Debug.Print "    Loop"
        Case 3
            Debug.Print "    Reciprocate"
    End Select
```

```
    'Set play mode to Loop
    Dim nPlayMode As Long
    Debug.Print "New play mode: "
    SwMotionStudy.PlayMode = swAnimationPlayMode_e.swAnimationPlayModeLoop
    nPlayMode = SwMotionStudy.PlayMode
    'Get new play mode
    Select Case nPlayMode
        Case 1
            Debug.Print "    Normal"
        Case 2
            Debug.Print "    Loop"
        Case 3
            Debug.Print "    Reciprocate"
    End Select
```

```
    'Set timebar to 0 on timeline
    SwMotionStudy.SetTime 0
```

```
    'Play the animation
    SwMotionStudy.Play
```

```
End Sub
```
