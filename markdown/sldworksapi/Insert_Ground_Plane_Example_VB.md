---
title: "Insert and Activate Ground Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Ground_Plane_Example_VB.htm"
---

# Insert and Activate Ground Plane Example (VBA)

This example shows how to insert and activate a ground plane in the current configuration of an assembly.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\introsw\vanity_assembly.sldasm.
 '
 ' Postconditions:
 ' 1. Inserts Ground Plane1 in the Ground Planes folder.
 ' 2. Inspect the FeatureManager design tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim featMgr As SldWorks.FeatureManager
 Dim feat As SldWorks.Feature
 Dim groundPlanes As Variant
 Dim boolstatus As Boolean
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set featMgr = Part.FeatureManager

    boolstatus = Part.Extension.SelectByRay(-9.07572786993001E-02, -3.35232970080597E-02, -0.329520078481409, -0.560777860996441, 0.738723196597798, -0.373920084275486, 1.28607075733318E-02, 2, False, 0, 0)
     Set feat = featMgr.InsertGroundPlane(False)

    boolstatus = Part.Extension.SelectByID2("Ground Plane1", "MAGNETICGROUNDPLANE", 0, 0, 0, False, 0, Nothing, 0)
     boolstatus = Part.ActivateGroundPlane(swThisConfiguration, Null)
    groundPlanes = Part.GetActiveGroundPlane(swAllConfiguration, Null)

End Sub
```
