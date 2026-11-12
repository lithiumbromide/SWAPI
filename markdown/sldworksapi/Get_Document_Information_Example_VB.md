---
title: "Get Document Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Document_Information_Example_VB.htm"
---

# Get Document Information Example (VBA)

This example shows how to get the title and document type of the active document.

```vb
'---------------------------------------------
Sub ModelInfo( )

' Define variable used to hold the SldWorks object
Dim swApp As Object

' Define variable used to hold the ModelDoc object
Dim Model As Object
Dim TopName As String

' Constant enumerators
Const swDocPART = 1
Const swDocASSEMBLY = 2
Const swDocDRAWING = 3

' Create or attach to SOLIDWORKS Design session. Because you are grabbing the active document, this example requires that SOLIDWORKS Design be running and have a document already loaded.
Set swApp = CreateObject("SldWorks.Application")

' Grab the currently active document
Set Model = swApp.ActiveDoc

' Check to see if a document is loaded
If Model Is Nothing Then
' If no model is currently loaded, then exit
Exit Sub
End if

' Determine the document type. If the document is a drawing, then send a message to the user.
If (Model.GetType <> swDocDRAWING) Then
swApp.SendMsgToUser ("This is not a drawing")
Else
' Get the document title
Let TopName = Model.GetTitle
End If

End Sub
```
