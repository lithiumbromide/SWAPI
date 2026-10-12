---
title: "Create 3D Contact Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3D_Contact_Feature_Example_VBNET.htm"
---

# Create 3D Contact Feature Example (VB.NET)

This example shows how to create a 3D Contact feature for use in motion studies.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. In SOLIDWORKS Design, verify that View > MotionManager is selected.
  ' 3. In the IDE, right-click the project name in the Project Explorer,
 '    click Add Reference, browse to install_dir\api\redist, and select
 '    SolidWorks.Interop.swmotionstudy.dll.
 ' 4. Click OK.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Selects the components to study.
 ' 2. Sets the static contact friction option.
 ' 3. Adds Solid Body Contact1 to the MotionManager design tree on the
 '    Motion Study 1 tab.
 ' 4. Inspect the Immediate window.
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

     Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swMotionMgr As MotionStudyManager
         Dim swMotionStudy1 As MotionStudy
         Dim swContFeat As Simulation3DContactFeatureData
         Dim boolstatus As Boolean
         Dim swFeat As Feature
         Dim longstatus As Integer, longwarnings As Integer

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

         ' Create the feature data object
         swContFeat = swMotionStudy1.CreateDefinition(swFeatureNameID_e.swFmAEM3DContact)

         If swContFeat Is Nothing Then
             Debug.Print("Failed to create feature data object")
         End If

         Dim swSelMgr As SelectionMgr
         swSelMgr = swModel.SelectionManager

         ' Select the components to study
         boolstatus = swModelDocExt.SelectByID2("Beam with holes-1@beam_boltconnection", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         boolstatus = swModelDocExt.SelectByID2("Beam with holes-2@beam_boltconnection", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)

         ' Set the 3D Contact components
         Dim ContactObj(1) As Component
         ContactObj(0) = swSelMgr.GetSelectedObject6(1, -1)
         ContactObj(1) = swSelMgr.GetSelectedObject6(2, -1)

         swContFeat.ContactComponents = ContactObj

         ' Set the static contact friction option
         swContFeat.FrictionOption = swMotionContactFrictionType_e.swMotionContactFrictionFull

         ' Create a 3D Contact feature
         swFeat = swMotionStudy1.CreateFeature(swContFeat)

         boolstatus = swModelDocExt.SelectByID2("Solid Body Contact1", "SIMULATION_ELEMENT", 0, 0, 0, False, 0, Nothing, 0)

         If swFeat Is Nothing Then
             Debug.Print("Failed to create feature")
         Else
             Debug.Print(swFeat.Name)
             If swContFeat.UseRestitutionCoefficient Then
                 Debug.Print("  Use coefficient of restitution:")
                 Debug.Print("    Coefficient of restitution: " & swContFeat.RestitutionCoefficient)
             Else
                 Debug.Print("  Use impact force:")
                 Debug.Print("    Exponent of exponential force: " & swContFeat.Exponent)
                 Debug.Print("    Maximum damping coefficient: " & swContFeat.MaxDamping)
                 Debug.Print("    Penetration at which maximum damping is applied: " & swContFeat.Penetration)
                 Debug.Print("    Stiffness of material at boundary of interaction: " & swContFeat.Stiffness)
             End If
             If swContFeat.SpecifyMaterial Then
                 Debug.Print("  Type of material as defined by swCosmosWorksMat:")
                 Debug.Print("    First object: " & swContFeat.MaterialID(0))
                 Debug.Print("    Second object: " & swContFeat.MaterialID(1))
             End If
             If swContFeat.FrictionOption = swMotionContactFrictionType_e.swMotionContactFrictionFull Then
                 Debug.Print("  Static contact friction:")
                 Debug.Print("    Coefficient: " & swContFeat.StaticFrictionCoefficient)
                 Debug.Print("    Velocity: " & swContFeat.StaticFrictionVelocity)
             Else
                 Debug.Print("  Dynamic contact friction:")
                 Debug.Print("    Coefficient: " & swContFeat.DynamicFrictionCoefficient)
                 Debug.Print("    Velocity: " & swContFeat.DynamicFrictionVelocity)
             End If

         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
