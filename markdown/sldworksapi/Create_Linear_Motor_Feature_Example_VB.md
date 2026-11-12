---
title: "Create Linear Motor Feature Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Linear_Motor_Feature_Example_VB.htm"
---

# Create Linear Motor Feature Example VB

## Create Linear Motor Feature Example (VBA)

This example shows how to create a motor feature data object and a linear motor feature.

```
'-----------------------------------------------------------------
' Postconditions:
'  1. Open an assembly document that contains at least
'     two components and a motion study named Motion Study 3.
'  2. In the IDE, add a reference to the SolidWorks MotionStudy
'     type library.
'  3. In SOLIDWORKS Design, click Tools > Add-Ins > SOLIDWORKS Motion > OK.
'  4. Open the Immediate window.
'
'
' Postconditions:
'  1. Gets the MotionManager.
'  2. Gets and activates a motion study named Motion Study 3.
'  3. Selects a face on a component.
'  4. Creates and sets data for a linear motor feature.
'  5. Selects the component whose face was selected in step 3.
'  6. Selects a face on a different component.
'  7. Sets motion relative to the first selected component.
'  8. Select the same face on the first component again and
'     set that face to be the load-bearing face for the motor feature.
'  9. Creates a linear motor feature.
' 10. Gets the name of linear motor feature.
' 11. Examine the Immediate window.
'
' NOTE: For this example to work for you, replace calls to
' select the different faces and components with calls to select the faces
' and components on your assembly. You must also create a file called
' Test_bouncingBall.csv that contains the spline data, and your assembly
' must have a motion-analysis motion study named Motion Study 3.
'------------------------------------------------------------------
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
    Dim swMotionStudy3 As SwMotionStudy.MotionStudy
    Dim swMotorFeat As SldWorks.SimulationMotorFeatureData
    Dim swGravityFeat As Object
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
    ' Get Motion Study 3, a Motion Analysis study
    Set swMotionStudy3 = swMotionMgr.GetMotionStudy("Motion Study 3")
```

```
    If (swMotionStudy3 Is Nothing) Then
        MsgBox "Motion Study 3 is not available."
        End
    End If
```

```
    ' Active Motion Study 3
    swMotionStudy3.Activate
```

```
    ' Select a face on a component
    Set swSelMgr = swModel.SelectionManager
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.07792618280496, 0.06212618843159, 0.02214691016243, False, 0, Nothing, 0)
```

```
    ' Create linear motor feature data
    ' and get and set some options
    Set swMotorFeat = swMotionStudy3.CreateDefinition(swFmAEMLinearMotor)
    If swMotorFeat Is Nothing Then
       Debug.Print "ERROR: Creation of motor feature data object failed."
        Exit Sub
    End If
    swMotorFeat.InterpolatedMotor swSimulationMotorDrive_Velocity, 1
    swMotorFeat.DirectionReference = swSelMgr.GetSelectedObject6(1, -1)
    ' Load the spline data from the specified file
    boolstatus = swMotorFeat.LoadSplineData("Test_bouncingBall.csv")
```

```
    ' Select the component on whose face you previously selected
    Dim RelObj As SldWorks.Component2
    Set RelObj = swSelMgr.GetSelectedObjectsComponent3(1, -1)
```

```
    ' Select a face on a different component
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.07924982844941, 0.06212618843165, 0.03225592518596, False, 0, Nothing, 0)
```

```
    ' Set motion relative to the first selected component
    swMotorFeat.RelativeComponent = RelObj
    swMotorFeat.Location = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Select the same face on the first component again and
    ' Set that face to be the load-bearing face for the motor feature
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.07792618280496, 0.06212618843159, 0.02214691016243, False, 0, Nothing, 0)
    Dim ContactObj(0) As Object
    Set ContactObj(0) = swSelMgr.GetSelectedObject6(1, -1)
    Dim vContact As Variant
    vContact = ContactObj
    swMotorFeat.LoadReferences = vContact
```

```
    ' Get the motor type
    Debug.Print swMotorFeat.MotorType
```

```
     ' Create a motor feature
     Set swFeat = swMotionStudy3.CreateFeature(swMotorFeat)
```

```
    If swFeat Is Nothing Then
        Debug.Print " ERROR: Creation of the motor feature failed."
    Else
        Debug.Print "Name of the feature added : " & swFeat.Name
    End If
```

```
End Sub
```
