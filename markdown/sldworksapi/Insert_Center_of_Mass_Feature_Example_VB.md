---
title: "Insert Center of Mass Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Center_of_Mass_Feature_Example_VB.htm"
---

# Insert Center of Mass Feature Example (VBA)

This example shows how to insert Center of Mass and Center of Mass Reference Point features.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a part.
 '
 ' Postconditions: The FeatureManager design tree contains:
 ' * Center of Mass
 ' * Center of Mass Reference Point1
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim COM As SldWorks.Feature
 Dim COMRP As SldWorks.Feature
Option Explicit

 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
    Set COM = Part.FeatureManager.InsertCenterOfMass
     Set COMRP = Part.FeatureManager.InsertCenterOfMassReferencePoint

End Sub
```
