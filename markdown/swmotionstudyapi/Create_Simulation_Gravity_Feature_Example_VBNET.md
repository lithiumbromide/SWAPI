---
title: "Create Simulation Gravity Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Create_Simulation_Gravity_Feature_Example_VBNET.htm"
---

# Create Simulation Gravity Feature Example (VB.NET)

This example shows how to create a simulation gravity feature in a motion study.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. In SOLIDWORKS, verify that View > MotionManager is selected.
  ' 3. In the IDE, right-click the project name in the Project Explorer,
 '    click Add Reference, browse to install_dir\api\redist, and select
 '    SolidWorks.Interop.swmotionstudy.dll.
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swmotionstudy
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swMotionMgr As MotionStudyManager
     Dim swMotionStudy1 As MotionStudy
     Dim swGravityFeat As SimulationGravityFeatureData
     Dim boolstatus As Boolean
     Dim swFeat As Feature
     Dim longstatus As Integer, longwarnings As Integer

     Sub main()

         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam_boltconnection.sldasm", 2, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("beam_boltconnection", False, longstatus)
         swModel = swApp.ActiveDoc

         swModelDocExt = swModel.Extension

         swMotionMgr = swModelDocExt.GetMotionStudyManager()
         swMotionStudy1 = swMotionMgr.GetMotionStudy("Motion Study 1")

         If (swMotionStudy1 Is Nothing) Then
             Debug.Print("Motion Study 1 is not available")
         End If

         swMotionStudy1.StudyType = swMotionStudyType_e.swMotionStudyTypePhysicalSimulation

         ' Activate Motion Study 1
         swMotionStudy1.Activate()

         ' Define feature data
         swGravityFeat = swMotionStudy1.CreateDefinition(swFeatureNameID_e.swFmAEMGravity)
         If swGravityFeat Is Nothing Then
             Debug.Print("Creation of feature data object failed")
         End If
         swGravityFeat.ReverseDirection = False
         swGravityFeat.Axis = 0
         swGravityFeat.Strength = 12

         ' Create feature
         swFeat = swMotionStudy1.CreateFeature(swGravityFeat)

         If swFeat Is Nothing Then
             Debug.Print("Creation of feature failed")
         Else
             Debug.Print("Name of the feature added: " & swFeat.Name)
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
