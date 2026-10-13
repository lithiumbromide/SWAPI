---
title: "Get Faces Affected by Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Affected_by_Feature_Example_VB.htm"
---

# Get Faces Affected by Feature Example (VBA)

This example shows how to get the faces affected by a feature. This example also highlights the edges on each affected face in blue.

```vb
 '----------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document.
 ' 2. Select a feature, such as a draft, that affects faces.
 '
 ' Postconditions:
 ' 1. Highlights the edges of the faces in blue that are affected
 '    by the selected feature.
 ' 2. Examine the graphics area.
 '----------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelExt As SldWorks.ModelDocExtension
 Dim swFeature As SldWorks.Feature
 Dim vAffectedFaces As Variant
 Dim vEdges As Variant
 Dim nFaceCount As Long
 Dim nEdgeCount As Long
 Dim i As Long
 Dim j As Long

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
     Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
     swModel.ClearSelection2 (True)
    nFaceCount = swFeature.GetAffectedFaceCount
     Debug.Print "Number of faces affected by selected feature = " & nFaceCount
     vAffectedFaces = swFeature.GetAffectedFaces
    For i = 0 To (nFaceCount - 1)
         nEdgeCount = vAffectedFaces(i).GetEdgeCount
         Debug.Print "   Number of edges on Face " & i; " = " & nEdgeCount
         vEdges = vAffectedFaces(i).GetEdges
        For j = 0 To (nEdgeCount - 1)
          vEdges(j).Display 2, 0, 0, 1, True
         Next j
     Next i
End Sub
```
