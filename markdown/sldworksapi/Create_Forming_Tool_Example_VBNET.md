---
title: "Create Forming Tool Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Forming_Tool_Example_VBNET.htm"
---

# Create Forming Tool Example (VB.NET)

This example shows how to create a forming tool for a sheet metal part.

```
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim myFeature As Feature
    Dim boolstatus As Boolean

    Sub main()

        Part = swApp.ActiveDoc
        'Select the stopping face: Mark = 1
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0283459459495816, 0.0187563215566229, 0, True,
1, Nothing, 0)
        'Select the face to remove: Mark = 2
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0358143533097106, 0.0308169322714775, 0.0066335048657038, True, 2, Nothing, 0)

        'Create a forming tool with insertion point x=0, y=0
        myFeature = Part.FeatureManager.CreateFormTool2(0, 0)

    End Sub

    Public swApp As SldWorks

End Class
```
