---
title: "Create Forming Tool Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Forming_Tool_Example_VB.htm"
---

# Create Forming Tool Example (VBA)

This example shows how to create a forming tool for a sheet metal part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\formingTool.sldprt.
 '
 ' Postconditions:
 ' 1. Creates FormTool1 with the specified stopping face, face to remove,
 '    and insertion point.
 ' 2. Examine the FeatureManager design tree and graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Option Explicit

 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myFeature As SldWorks.Feature
 Dim boolstatus As Boolean
Sub main()
     Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     'Select the stopping face: Mark = 1
     boolstatus = Part.Extension.SelectByID2("", "FACE", 2.83459459495816E-02, 1.87563215566229E-02, 0, True, 1, Nothing, 0)
     'Select the face to remove: Mark = 2
     boolstatus = Part.Extension.SelectByID2("", "FACE", 3.58143533097106E-02, 3.08169322714775E-02, 6.6335048657038E-03, True, 2, Nothing, 0)
     'Create a forming tool with insertion point x=0, y=0
     Set myFeature = Part.FeatureManager.CreateFormTool2(0, 0)
 End Sub
```
