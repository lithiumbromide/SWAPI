---
title: "Insert Weldment Cut List Example #2 (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List2_Example_VB.htm"
---

# Insert Weldment Cut List Example #2 (VBA)

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
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
Dim Part As ModelDoc2
Dim obj() As Object
Dim v As Variant

Sub main()
```

```vb
Dim PartName As String
Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc
v = Part.GetBodies2(0, True)
Dim cutListFeature As Feature
Set cutListFeature = Part.FeatureManager.InsertWeldmentCutList2(v)
```

```vb
End Sub
```
