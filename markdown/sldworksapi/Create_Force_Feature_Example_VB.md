---
title: "Create Force Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Force_Feature_Example_VB.htm"
---

# Create Force Feature Example (VBA)

This example shows how to create a force feature for use with Basic Motion and Motion Analysis studies.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\motionstudies\weldingrobot\weldingrobot.sldasm.
' 2. Click View > User Interface > MotionManager in SOLIDWORKS Design
'    if the Motion Study 1 tab is not displayed.
' 3. Add a reference to the SOLIDWORKS MotionStudy type library in
'    the Microsoft Visual Basic for Applications IDE (click
'    Tools > SolidWorks version MotionStudy Type library > OK).
' 4. Open the Immediate window.
'
'
' Postconditions:
' 1. Gets the MotionManager.
' 2. Gets and activates Motion Study 1.
' 3. Selects a face.
' 4. Creates the definition for the Force feature.
' 5. Defines the Force feature.
' 6. Gets the component to which the selected face belongs.
' 7. Selects another face on the component.
' 8. Creates Force1.
' 9. Examine the Immediate window and the MotionManager.
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swMotionMgr As SwMotionStudy.MotionStudyManager
    Dim swMotionStudy1 As SwMotionStudy.MotionStudy
    Dim swForceFeat As SldWorks.SimulationForceFeatureData
    Dim boolstatus As Boolean
    Dim swFeat As SldWorks.Feature
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
    ' Get Motion Study 1
    Set swMotionStudy1 = swMotionMgr.GetMotionStudy("Motion Study 1")
    If (swMotionStudy1 Is Nothing) Then
        MsgBox "Motion Study 1 is not available."
        End
    End If
```

```
    ' Activate Motion Study 1
    swMotionStudy1.Activate
```

```
    ' Select a face
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 2.07474494005737E-02, -3.42078458101582E-02, -0.137793984025564, False, 0, Nothing, 0)
```

```
   ' Create the definition for the Force feature
    Set swForceFeat = swMotionStudy1.CreateDefinition(swFmAEMLinearForce)
    If swForceFeat Is Nothing Then
       Debug.Print "ERROR: Creation of Force feature data object failed."
        Exit Sub
    End If
```

```
    ' Define the Force feature
    swForceFeat.ActionType = swSimulationForceAction_ActionOnly
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Get the selected face
    swForceFeat.ActionLocation = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Get the component to which the selected face belongs
    Dim RelObj As Component2
    Set RelObj = swSelMgr.GetSelectedObjectsComponent3(1, -1)
```

```
    ' Select a face on a component and create the Force feature relative to this component
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 3.29445368450365E-02, -2.94946206198006E-02, -9.99182361467206E-02, False, 0, Nothing, 0)
    swForceFeat.ReferenceComponent = RelObj
    Set swFeat = swMotionStudy1.CreateFeature(swForceFeat)
```

```
    If swFeat Is Nothing Then
        Debug.Print " ERROR: Creation of the Force feature failed."
    Else
        Debug.Print "Name of Force feature : " & swFeat.Name
    End If
```

```
End Sub
```
