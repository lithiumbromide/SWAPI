---
title: "Insert Revision Cloud into a Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Revision_Cloud_into_Drawing_Example_VB.htm"
---

# Insert Revision Cloud into a Drawing Example (VBA)

This example shows how to insert revision clouds into a drawing and access revision cloud data.

```vb
 '--------------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\resetsketchvisibility.slddrw.
 '
 ' Postconditions:
 ' 1. Inserts an elliptical revision cloud in the drawing.
 ' 2. Examine the graphics area.
 '
 ' NOTE: Because the drawing is used elsewhere, do not save changes.
 ' --------------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.DrawingDoc
 Dim RevCloud As SldWorks.RevisionCloud
 Dim RevCloudAnno As SldWorks.Annotation
 Dim boolstatus As Boolean
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     boolstatus = Part.ActivateView("Drawing View1")

     ' Create a revision cloud with an elliptical shape
     Set RevCloud = Part.InsertRevisionCloud(swRevisionCloudShape_Ellipse)
     If Not RevCloud Is Nothing Then
        Set RevCloudAnno = RevCloud.GetAnnotation()
        If Not RevCloudAnno Is Nothing Then
           ' Position the center of the elliptical revision cloud
           boolstatus = RevCloudAnno.SetPosition(0.270847371964905, 0.553263328912467, 0)
           RevCloud.ArcRadius = 0.00508
           ' Create a path point on the corner of an ellipse-inscribed rectangle
           boolstatus = RevCloud.SetPathPointAtIndex(-1, 0.378419710263212, 0.511051398694144, 0)
           ' Close the revision cloud path
           boolstatus = RevCloud.Finalize()
        End If
     End If

End Sub
```
