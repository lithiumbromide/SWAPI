---
title: "Add Highlighting to or Remove Highlight from Edges Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Highlighting_to_or_Remove_Highlight_from_Edges_Example_VB.htm"
---

# Add Highlighting to or Remove Highlight from Edges Example (VBA)

This example shows how to highlight or remove highlight from the selected face's edges.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a face.
'
' Postconditions:
' 1. Displays a message box asking whether to highlight
'    the edges on the selected face.
' 2. Click Yes.
' 3. Examine the part.
'-------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face
    Dim vEdgeArr As Variant
    Dim vEdge As Variant
    Dim swEdge As SldWorks.Edge
    Dim nResponse As Integer
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
```

```
    nResponse = MsgBox("Highlight edges on selected face?", vbYesNo)
```

```
    swModel.ClearSelection2 True
```

```
    vEdgeArr = swFace.GetEdges
    For Each vEdge In vEdgeArr
        Set swEdge = vEdge
        If nResponse = vbYes Then
            swEdge.Display 2, 1#, 0#, 0#, True
        Else
            swEdge.Display 0, 0#, 0#, 0#, False
        End If
    Next vEdge
```

```
End Sub
```
