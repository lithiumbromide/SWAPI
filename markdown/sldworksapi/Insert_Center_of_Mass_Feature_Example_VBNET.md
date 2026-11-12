---
title: "Insert Center of Mass Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Center_of_Mass_Feature_Example_VBNET.htm"
---

# Insert Center of Mass Feature Example (VB.NET)

This example shows how to insert Center of Mass and Center of Mass Reference Point features.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a part.
 '
 ' Postconditions: The FeatureManager design tree contains:
 ' * Center of Mass
 ' * Center of Mass Reference Point1
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim COM As Feature
     Dim COMRP As Feature

     Sub main()

         Part = swApp.ActiveDoc

         COM = Part.FeatureManager.InsertCenterOfMass
         COMRP = Part.FeatureManager.InsertCenterOfMassReferencePoint

     End Sub

     Public swApp As SldWorks

 End  Class
```
