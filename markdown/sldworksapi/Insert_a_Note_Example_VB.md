---
title: "Insert a Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_a_Note_Example_VB.htm"
---

# Insert a Note Example (VBA)

This example shows show to insert a geometric tolerance symbol in an active drawing document.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 '
 ' Postconditions:
 ' 1. Inserts a geometric tolerance symbol at the specified position.
 ' 2. Examine the graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim Part As SldWorks.ModelDoc2
     Dim Annotation As SldWorks.Annotation
     Dim swSelobj2 As Object
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim Note As SldWorks.Note
     Dim boolstatus As Boolean
     Dim longstatus As Long

    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    Set swSelMgr = Part.SelectionManager
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.166288048468037, 0.223859686746988, -4.00000000013279E-04, False, 0, Nothing, 0)
     Set swSelobj2 = swSelMgr.GetSelectedObject6(1, -1)
    Set Note = Part.InsertNote("<MOD-CL>")
    If Not Note Is Nothing Then
        Note.Angle = 0
        boolstatus = Note.SetBalloon(0, 0)

       Set Annotation = Note.GetAnnotation()

        Dim AttEntArr(0) As Object
         Set AttEntArr(0) = swSelobj2
         Dim vAttEntArrIn As Variant
         vAttEntArrIn = AttEntArr
        boolstatus = Annotation.SetAttachedEntities(vAttEntArrIn)
       If Not Annotation Is Nothing Then
           longstatus = Annotation.SetLeader3(1, 0, True, True, False, False)
           boolstatus = Annotation.SetPosition2(0.1038962799325, 0.135343450253, 0)
        End If

    End If

    Part.ClearSelection2 True
     Part.WindowRedraw
End Sub
```
