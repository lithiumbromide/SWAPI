---
title: "Link Projected View to Parent Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Link_Projected_View_to_Parent_Configuration_Example_VBNET.htm"
---

# Link Projected View to Parent Configuration Example (VB.NET)

This example shows how to link a projected drawing view to the parent configuration.

'-------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified file exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Links the projected view to the parent configuration.
' 2. Examine the Immediate window.
'
' NOTE: Because this drawing document is used elsewhere, do not save
' changes.
'-------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

Public swModel As ModelDoc2
Public swView As View
Public status As Boolean

Public Sub Main()

Dim swModelDocExt As ModelDocExtension
Dim swDrawing As DrawingDoc
Dim fileName As String
Dim errors As Integer
Dim warnings As Integer

' Open drawing document that has a projected view
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
swModel = swApp.**OpenDoc6**(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
swDrawing = swModel
swModelDocExt = swModel.**Extension**

' Make the projected view the active view
status = swDrawing.**ActivateView**("Drawing View2")
status = swModelDocExt.**SelectByID2**("Drawing View2", "DRAWINGVIEW", 0.4426278247583, 0.3837831481976, 0, False, 0, Nothing, 0)
swView = swDrawing.**ActiveDrawingView**

' Determine whether the projected view is linked to the
' parent configuration
Call LinkConfiguration()

' Link the projected view to the parent
' configuration
swView.**LinkParentConfiguration** = True

' Determine whether the projected view is linked to the
' parent configuration
Call LinkConfiguration()

End Sub

Public Sub LinkConfiguration()
' Print to the Immediate window whether
' the projected view is linked to the parent
' configuration
status = swView.**LinkParentConfiguration**
If status Then
Debug.Print("Projected view now linked to parent configuration.")
swModel.**EditRebuild3**()
Else
Debug.Print("Projected view not linked to parent configuration.")
End If
End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
