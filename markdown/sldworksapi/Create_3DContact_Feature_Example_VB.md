---
title: "Create 3D Contact Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3DContact_Feature_Example_VB.htm"
---

# Create 3D Contact Feature Example (VBA)

This example shows how to create a 3D Contact feature for use in motion studies.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. In SOLIDWORKS Design, verify that View > MotionManager is selected.
 ' 3. In the IDE, click Tools > References and select
 '    SOLIDWORKS version MotionStudy Type library.
 ' 4. Click OK.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Selects the faces of the components to study.
 ' 2. Sets the static contact friction option.
 ' 3. Adds Solid Body Contact1 to the MotionManager design tree on the
 '    Motion Study 1 tab.
 ' 4. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 '----------------------------------------------------------------------------
Option Explicit

 Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swModelDocExt As SldWorks.ModelDocExtension
     Dim swMotionMgr As SwMotionStudy.MotionStudyManager
     Dim swMotionStudy1 As SwMotionStudy.MotionStudy
     Dim swContFeat As SldWorks.Simulation3DContactFeatureData
     Dim boolstatus As Boolean
     Dim swFeat As SldWorks.Feature
     Dim longstatus As Long, longwarnings As Long
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

     ' Create the feature data object
     Set swContFeat = swMotionStudy1.CreateDefinition(swFmAEM3DContact)
    If swContFeat Is Nothing Then
        Debug.Print "Failed to create feature data object"
     End If
    Dim swSelMgr As SldWorks.SelectionMgr
     Set swSelMgr = swModel.SelectionManager
    ' Select the faces of the components to study
     boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.131022323560273, 1.29484035505811E-02, 6.10848486814461E-02, False, 0, Nothing, 0)
     boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.08742646002122, 1.52756897197435E-02, 6.10848486815598E-02, True, 0, Nothing, 0)

    ' Set the 3D Contact components
     Dim ContactObj(1) As Object
     Set ContactObj(0) = swSelMgr.GetSelectedObject6(1, -1)
     Set ContactObj(1) = swSelMgr.GetSelectedObject6(2, -1)
    Dim vContact As Variant
     vContact = ContactObj
     swContFeat.ContactComponents = vContact

    ' Set the static contact friction option
     swContFeat.FrictionOption = swMotionContactFrictionFull

    ' Create a 3D Contact feature
     Set swFeat = swMotionStudy1.CreateFeature(swContFeat)
    If swFeat Is Nothing Then
         Debug.Print "Failed to create feature"
     Else
         Debug.Print swFeat.Name
         If swContFeat.UseRestitutionCoefficient Then
             Debug.Print "  Use coefficient of restitution:"
             Debug.Print "    Coefficient of restitution: " & swContFeat.RestitutionCoefficient
         Else
             Debug.Print "  Use impact force:"
             Debug.Print "    Exponent of exponential force: " & swContFeat.Exponent
             Debug.Print "    Maximum damping coefficient: " & swContFeat.MaxDamping
             Debug.Print "    Penetration at which maximum damping is applied: " & swContFeat.Penetration
             Debug.Print "    Stiffness of material at boundary of interaction: " & swContFeat.Stiffness
         End If
         If swContFeat.SpecifyMaterial Then
             Debug.Print "  Type of material as defined by swCosmosWorksMat:"
             Debug.Print "    First object: " & swContFeat.MaterialID(0)
             Debug.Print "    Second object: " & swContFeat.MaterialID(1)
         End If
         If swContFeat.FrictionOption = swMotionContactFrictionType_e.swMotionContactFrictionFull Then
             Debug.Print "  Static contact friction:"
             Debug.Print "    Coefficient: " & swContFeat.StaticFrictionCoefficient
             Debug.Print "    Velocity: " & swContFeat.StaticFrictionVelocity
         Else
             Debug.Print "  Dynamic contact friction:"
             Debug.Print "    Coefficient: " & swContFeat.DynamicFrictionCoefficient
             Debug.Print "    Velocity: " & swContFeat.DynamicFrictionVelocity
         End If

    End If

End Sub
```
