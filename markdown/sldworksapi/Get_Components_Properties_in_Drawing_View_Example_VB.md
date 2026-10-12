---
title: "Get Components Properties in Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_Properties_in_Drawing_View_Example_VB.htm"
---

# Get Components Properties in Drawing View Example (VBA)

## Get Components' Properties in Drawing View Example (VBA)

This example shows how to get the components in a drawing view.

```vb
'----------------------------------------------
'
' Preconditions:
'          (1) Drawing document of an assembly is open.
'          (2) Drawing view is selected.
'
' Postconditions: None
'
'----------------------------------------------

Option Explicit
Public Enum swLineWeights_e
    swLW_NONE = -1
    swLW_THIN = 0
    swLW_NORMAL = 1
    swLW_THICK = 2
    swLW_THICK2 = 3
    swLW_THICK3 = 4
    swLW_THICK4 = 5
    swLW_THICK5 = 6
    swLW_THICK6 = 7
    swLW_NUMBER = 8
    swLW_LAYER = 9
End Enum

Public Enum swLineStyles_e
    swLineCONTINUOUS = 0
    swLineHIDDEN = 1
    swLinePHANTOM = 2
    swLineCHAIN = 3
    swLineCENTER = 4
    swLineSTITCH = 5
    swLineCHAINTHICK = 6
    swLineDEFAULT = 7
End Enum

'  The different types of drawing views
Public Enum swDrawingViewTypes_e
    swDrawingSheet = 1
    swDrawingSectionView = 2
    swDrawingDetailView = 3
    swDrawingProjectedView = 4
    swDrawingAuxiliaryView = 5
    swDrawingStandardView = 6
    swDrawingNamedView = 7
    swDrawingRelativeView = 8
End Enum

Sub ProcessDrawingComponent _
( _
    swDrawComp As SldWorks.DrawingComponent, _
    sPadStr As String _
)
    Dim vDrawCompChildArr           As Variant
    Dim vDrawCompChild              As Variant
    Dim swDrawCompChild             As SldWorks.DrawingComponent

    ' Returns empty strings for root component
    Debug.Print sPadStr & "Name             = " & swDrawComp.component.Name2
    Debug.Print sPadStr & "  File           = " & swDrawComp.component.GetPathName

    Debug.Print sPadStr & "  IsRoot         = " & swDrawComp.IsRoot
    Debug.Print sPadStr & "  Layer          = " & swDrawComp.Layer
    Debug.Print sPadStr & "  LayerOverride  = " & swDrawComp.LayerOverride
    Debug.Print sPadStr & "  Style          = " & swDrawComp.Style
    Debug.Print sPadStr & "  Visible        = " & swDrawComp.Visible
    Debug.Print sPadStr & "  Width          = " & swDrawComp.Width
    Debug.Print ""

    vDrawCompChildArr = swDrawComp.GetChildren
    If Not IsEmpty(vDrawCompChildArr) Then
        For Each vDrawCompChild In vDrawCompChildArr
            Set swDrawCompChild = vDrawCompChild

            ProcessDrawingComponent swDrawCompChild, sPadStr + "  "
        Next
    End If
End Sub
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swView                      As SldWorks.View
    Dim swDrawComp                  As SldWorks.DrawingComponent
    Dim bRet                        As Boolean
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject5(1)
    Set swDrawComp = swView.RootDrawingComponent

    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swView.Name & "  [" & swView.Type & "]"

    ProcessDrawingComponent swDrawComp, "    "
End Sub
'---------------------------------------
```
