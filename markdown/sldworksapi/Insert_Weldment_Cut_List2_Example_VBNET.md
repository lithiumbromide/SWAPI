---
title: "Insert Weldment Cut List Example #2 (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List2_Example_VBNET.htm"
---

# Insert Weldment Cut List Example #2 (VB.NET)

This example shows how to insert a weldment cut list into the FeatureManager design tree.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\assemblymates\bracket.sldprt.
' 2. Click Tools > Options > System Options > FeatureManager >
'    Solid Bodies > Show > OK.
' 3. Expand the Solid Bodies(1) folder in the FeatureManager design tree
'    and note its contents.
'
' Postconditions:
' 1. Inserts a cut-list-item folder feature containing the specified
'    weldment body.
' 2. Expand the Cut-List-Item1 folder in the Solid Bodies(1) folder
'    in the the FeatureManager design tree to verify step 1.
'
' NOTE: Because this part is used elsewhere,
' do not save changes.
'----------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim obj(0) As Body2
    Dim v As Array
    Dim i As Long

    Sub main()
        Part = swApp.ActiveDoc
        v = Part.GetBodies2(0, True)
        For i = 0 To UBound(v)
            obj(i) = CType(v(i), Body2)
        Next
        Dim cutListFeature As Feature
        cutListFeature = Part.FeatureManager.InsertWeldmentCutList2(obj)
    End Sub
    Public swApp As SldWorks
End Class
```
