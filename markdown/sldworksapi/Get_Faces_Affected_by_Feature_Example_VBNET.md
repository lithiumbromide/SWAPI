---
title: "Get Faces Affected by Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Affected_by_Feature_Example_VBNET.htm"
---

# Get Faces Affected by Feature Example (VB.NET)

This example shows how to get the faces affected by a feature. This example also highlights the edges on each affected face in blue.

```vb
 '-------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document.
 ' 2. Select a feature, such as a draft, that affects faces.
 '
 ' Postconditions:
 ' 1. Highlights the edges of the faces in blue that are affected
 '    by the selected feature.
 ' 2. Examine the graphics area.
 '-------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swModelExt As ModelDocExtension
     Dim swFeature As Feature
     Dim vAffectedFaces As Object
     Dim vEdges As Object
     Dim nFaceCount As Integer
     Dim nEdgeCount As Integer
     Dim i As  Integer
     Dim j As  Integer

     Sub main()

         swModel = swApp.ActiveDoc
         swModelExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         swFeature = swSelMgr.GetSelectedObject6(1, -1)
         swModel.ClearSelection2(True)

         nFaceCount = swFeature.GetAffectedFaceCount
         Debug.Print("Number of faces affected by selected feature = " & nFaceCount)
         vAffectedFaces = swFeature.GetAffectedFaces

         For i = 0 To (nFaceCount - 1)
             nEdgeCount = vAffectedFaces(i).GetEdgeCount
             Debug.Print("   Number of edges on Face " & i   " = " & nEdgeCount)
             vEdges = vAffectedFaces(i).GetEdges

             For j = 0 To (nEdgeCount - 1)
                 vEdges(j).Display(2, 0, 0, 1,  True)
             Next j
         Next i

     End Sub

     Public swApp As SldWorks

 End  Class
```
