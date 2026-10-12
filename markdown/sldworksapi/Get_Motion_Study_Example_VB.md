---
title: "Get Motion Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Motion_Study_Example_VB.htm"
---

# Get Motion Study Example (VBA)

This example shows how to get a Physical Simulation motion study and its properties.

```
'-----------------------------------------
' Preconditions:
' 1. Open a model that has a Physical Simulation motion study
'    named PhysSim.
' 2. In SOLIDWORKS Design, load the SOLIDWORKS Motion Study add-in
'    (click Tools > Add-Ins > SOLIDWORKS Motion).
' 3. In the SOLIDWORKS VBA IDE, add a reference to the
'    SolidWorks MotionStudy type library.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets the MotionManager.
' 2. Gets and activates the PhysSim motion study.
' 3. Gets some motion study properties and features.
' 4. Plays the motion study.
' 5. In SOLIDWORKS Design, click Stop in the MotionManager
'    to stop playing the motion study.
' 6. Gets the motion study results and whether the
'    results are out of date.
' 7. Examine the Immediate window.
'-----------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMotionMgr As SwMotionStudy.MotionStudyManager
Dim swMotionStudy1 As SwMotionStudy.MotionStudy
Dim swResults As SwMotionStudy.MotionStudyResults
Dim swMotionStudyProps As SwMotionStudy.MotionStudyProperties
Dim swPhysicalSimProps As SwMotionStudy.PhysicalSimulationMotionStudyProperties
Dim boolstatus As Boolean
Dim i As Long
Dim vMotionFeatures As Variant
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
    ' Get the MotionManager
    Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    If (swMotionMgr Is Nothing) Then
          End
    End If
```

```
    ' Get motion study named PhysSim
    Set swMotionStudy1 = swMotionMgr.GetMotionStudy("PhysSim")
    If (swMotionStudy1 Is Nothing) Then
        MsgBox "PhysSim is not available."
        End
    End If
```

```
    swMotionStudy1.StudyType = swMotionStudyType_e.swMotionStudyTypePhysicalSimulation
```

```
    'Active the motion study
    If Not swMotionStudy1.IsActive Then swMotionStudy1.Activate
    Debug.Print "Duration of motion study: " & swMotionStudy1.GetDuration
    Debug.Print "Timebar position on timeline: " & swMotionStudy1.GetTime
    Debug.Print "Number of motion features: " & swMotionStudy1.GetMotionFeaturesCount
    Set swMotionStudyProps = swMotionStudy1.GetProperties(2)
    Set swPhysicalSimProps = swMotionStudyProps
    Debug.Print ""
    Debug.Print "Physical simulation properties: "
    Debug.Print "    Frame rate: " & swMotionStudyProps.GetFrameRate
    Debug.Print "    Geometric accuracy: " & swPhysicalSimProps.GeometricAccuracy
    Debug.Print "    Mate accuracy: " & swPhysicalSimProps.MateAccuracy
    swPhysicalSimProps.MateAccuracy = 1
    vMotionFeatures = swMotionStudy1.GetMotionFeatures
    For i = 0 To UBound(vMotionFeatures)
    Dim swFeat As Feature
        Set swFeat = vMotionFeatures(i)
        PhysicalSimFeatureTests swFeat, swModel
    Next i
```

```
    'Calculate
    swMotionStudy1.Calculate
    WaitForCaluculation swMotionStudy1
    Set swResults = swMotionStudy1.GetResults(2)
    Debug.Print ""
    Debug.Print "Are the motion study results out of date? " & swResults.IsOutOfDate
```

```
End Sub
```

```
Private Sub WaitForCaluculation(SwMotionStudy As MotionStudy)
    Do While SwMotionStudy.IsPlaying
        DoEvents
    Loop
End Sub
```

```
Private Sub PhysicalSimFeatureTests(swFeat As Feature, TopDoc As ModelDoc2)
    Dim SimTypeName As String
    Dim SimulationGravityFeatureData As SldWorks.SimulationGravityFeatureData
```

```
    SimTypeName = swFeat.GetTypeName
    Debug.Print ""
        ' Print the name of the type of simulation and its gravity strength
        Select Case SimTypeName
        Case "AEMGravity"
            Debug.Print "    Type of feature: AEMGravity"
        Case "AEMLinearMotor"
            Debug.Print "    Type of feature: AEMLinearMotor"
        Case "AEMRotationalMotor"
            Debug.Print "    Type of feature: AEMRotationalMotor"
        Case "AEMLinearSpring"
            Debug.Print "    Type of feature: AEMLinearSpring"
        Case Else
            Debug.Print "    Type of feature: " & SimTypeName
            MsgBox SimTypeName
    End Select
```

```
End Sub
```
