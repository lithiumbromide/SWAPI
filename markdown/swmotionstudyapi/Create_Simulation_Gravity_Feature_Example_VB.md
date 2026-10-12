---
title: "Create Simulation Gravity Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Create_Simulation_Gravity_Feature_Example_VB.htm"
---

# Create Simulation Gravity Feature Example (VBA)

This example shows how to create a simulation gravity feature in a motion study.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. In SOLIDWORKS, verify that View > MotionManager is selected.
 ' 3. In the IDE, click Tools > References and select
 '    SOLIDWORKS version MotionStudy Type library.
 ' 4. Click OK.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Adds Gravity to the MotionManager design tree on the Motion Study 1 tab.
 ' 2. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 '----------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swMotionMgr As SwMotionStudy.MotionStudyManager
 Dim swMotionStudy1 As SwMotionStudy.MotionStudy
 Dim swGravityFeat As SldWorks.SimulationGravityFeatureData
 Dim swFeat As SldWorks.Feature
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam_boltconnection.sldasm", 2, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "beam_boltconnection", False, longstatus
     Set swModel = swApp.ActiveDoc

    Set swModelDocExt = swModel.Extension

     Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    Set swMotionStudy1 = swMotionMgr.GetMotionStudy("Motion Study 1")

    If (swMotionStudy1 Is Nothing) Then
         Debug.Print "Motion Study 1 is not available"
     End If

     swMotionStudy1.StudyType = swMotionStudyType_e.swMotionStudyTypePhysicalSimulation
    ' Activate Motion Study 1
     swMotionStudy1.Activate
    ' Define feature data
     Set swGravityFeat = swMotionStudy1.CreateDefinition(swFmAEMGravity)
    If swGravityFeat Is Nothing Then
         Debug.Print "Creation of feature data object failed"
     End If
    swGravityFeat.ReverseDirection = False
     swGravityFeat.Axis = 0
     swGravityFeat.Strength = 12
     ' Create feature
      Set swFeat = swMotionStudy1.CreateFeature(swGravityFeat)

    If swFeat Is Nothing Then
         Debug.Print "Creation of feature failed"
     Else
         Debug.Print "Name of the feature added: " & swFeat.Name
     End If

 End Sub
```
