---
title: "Disable Wait Cursor While Model View Redrawn (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/Disable_Wait_Cursor_While_Model_View_Redrawn_VB.htm"
---

# Disable Wait Cursor While Model View Redrawn (VBA)

## Disable Wait Cursor When Model View Redrawn (VBA)

This example shows how to suppress the wait cursor (also called the hourglass) when a model view is redrawn.

'---------------------------------------------

Option Explicit

Sub main()

Dim swApp As Object

Dim Part As SldWorks.ModelDoc2

Dim modelView As SldWorks.modelView

Set swApp = Application.SldWorks

Set Part = swApp.ActiveDoc

Set modelView = Part.ActiveView

modelView.SuppressWaitCursorDuringRedraw = False

End Sub
