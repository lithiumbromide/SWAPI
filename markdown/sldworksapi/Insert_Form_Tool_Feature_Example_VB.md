---
title: "Insert Forming Tool Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Form_Tool_Feature_Example_VB.htm"
---

# Insert Forming Tool Feature Example (VBA)

This example shows how to insert a forming tool feature into a sheet metal
part.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Verify that the specified forming tool part exists.
' 3. Select a face on which to apply the counter sink emboss forming tool from
'    the Design Library.
'
' Postconditions:
' 1. Inserts the counter sink emboss1 feature.
' 2. Examine the FeatureManager design tree and graphics area.
' ---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim myFeature As SldWorks.Feature
Dim formingTool As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
```

```
    ' Insert a counter sink emboss forming tool feature
    formingTool = "C:\ProgramData\SolidWorks\SOLIDWORKS 2025\design library\forming tools\embosses\counter sink emboss.sldprt"
    Set myFeature = Part.FeatureManager.InsertFormToolFeature(formingTool, False, 0#, "", True, True, True, True, False)
```

```
End Sub
```
