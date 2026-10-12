---
title: "Delete OLE Objects from Drawing Sheet and Template Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_OLE_Objects_from_Drawing_Sheet_and_Template_Example_VB.htm"
---

# Delete OLE Objects from Drawing Sheet and Template Example (VBA)

This example shows how to delete any OLE objects from the current drawing sheet and template.

```
'---------------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains one or more
'    OLE objects in the drawing sheet or template.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Deletes all OLE objects in drawing sheet
'    and template.
' 2. Examine the graphics area and Immediate window.
'--------------------------------------------------------
```

```vb
Option Explicit
Sub DeleteAllOleItemsInSheet _
( _
    swApp As SldWorks.SldWorks, _
    swModel As SldWorks.ModelDoc2, _
    swSheet As SldWorks.Sheet _
)
    Dim nOleCnt                     As Long
    Dim i                           As Long
    Dim nSize                       As Long
    Dim nAspect                     As Long
    Dim skArray()                   As Variant
    Dim bRet                        As Boolean
    nOleCnt = swSheet.GetOLEObjectCount: If 0 = nOleCnt Then Exit Sub
    ReDim skArray(nOleCnt - 1)

    ' Get location of each OLE item
    For i = 0 To nOleCnt - 1
        skArray(i) = swSheet.GetOLEObjectSettings(i, nSize, nAspect)
    Next i

    ' Delete each OLE items
    For i = 0 To nOleCnt - 1
        bRet = swModel.SelectByID("", "OLEITEM",0.5 * (skArray(i)(0) + skArray(i)(3)), 0.5 * (skArray(i)(1) + skArray(i)(4)), 0.5 * (skArray(i)(2) + skArray(i)(5)))
        bRet = swModel.DeleteSelection(False)
         Debug.Print ("OLE item " & i & " deleted? " & bRet)
    Next i
End Sub

Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swSheet                     As Object

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSheet = swDraw.GetCurrentSheet

    DeleteAllOleItemsInSheet swApp, swModel, swSheet

    ' Switch to template and delete OLE objects
    swDraw.EditTemplate
    Set swSheet = swDraw.GetCurrentSheet
    DeleteAllOleItemsInSheet swApp, swModel, swSheet

    swDraw.EditSheet

    ' Switch back to sheet and make sure all OLE objects are deleted
    Set swSheet = swDraw.GetCurrentSheet

End Sub
```
