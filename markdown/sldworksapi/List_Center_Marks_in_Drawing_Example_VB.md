---
title: "List Center Marks in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/List_Center_Marks_in_Drawing_Example_VB.htm"
---

# List Center Marks in Drawing Example (VBA)

This example shows how to list all of the center marks in all of the
drawing views in a drawing.

'-------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing with one or more center
marks in any view.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-------------------------------------------------------------------

Option Explicit

Public Enum swCenterMarkStyle_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCenterMark_NonAnnotation
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCenterMark_Single
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCenterMark_LinearGroup
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCenterMark_CircularGroup
= 4

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vCenterMarkArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vCenterMarkkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCenterMarkkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.CenterMark

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swDraw.GetFirstView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While Not swView Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}View
= " + swView.GetName2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCenterMark = swView.GetFirstCenterMark2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While Not swCenterMark Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vCenterMarkArr
= swView.GetCentermarks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
Not IsEmpty(vCenterMarkArr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CenterLineFontkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCenterMark.CenterLineFont

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ConnectionLineskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCenterMark.ConnectionLines

' 1 radian = 180º/ p = 57.295779513º or approximately 57.3º

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RotationAnglekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCenterMark.RotationAngle* 57.3 & " degrees"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ShowLineskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCenterMark.ShowLines

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sizekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCenterMark.Size

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Stylekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCenterMark.Style

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UseDocDisplaySettingskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCenterMark.UseDocDisplaySettings

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCenterMark = swCenterMark.GetNext

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swView.GetNextView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

End Sub
