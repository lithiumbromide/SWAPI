---
title: "Fire Events When PropertyManager Page Opened and Canceled Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm"
---

# Fire Events When PropertyManager Page Opened and Canceled Example (VB.NET)

This example shows how to get the SOLIDWORKS command ID, PropertyManager title, and whether the user interface is active. Events are fired before the PropertyManager page is opened and when it is canceled.

'------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Add a reference to **SolidWorks.Interop.swcommands.dll**.
' 3. Open the Immediate window.
' 4. Clear **Tools > Options > Stop VSTA debugger on
' macro exit**, if it's selected.
'
' Postconditions:
' 1. Opens the part.
' 2. Fires the CommandOpenPreNotify event; click **OK**
' to close the message box.
' 3. Opens the Fillet PropertyManager page.
' 4. Gets the title of the PropertyManager page, whether the
' user interface is active, and whether the command ID
' is a fillet.
' 5. Click **X** on the Fillet PropertyManager page
' to cancel it.
' 6. Fires the CommandCloseNotify event; click **OK** to close
' the message box.
' 7. Examine the Immediate window.
' 8. Click **Stop Debugging** in the IDE.
' 9. Select **Tools > Options > Stop VSTA debugger on
' macro exit**, if you cleared it in Preconditions
' step 4.
'--------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports SolidWorks.Interop.swcommands

Partial Class SolidWorksMacro

Public WithEvents swAppSW As SldWorks

Public Sub Main()

Dim swModel As ModelDoc2
Dim swModelDocExt As ModelDocExtension
Dim modelName As String
Dim errors As Integer
Dim warnings As Integer
Dim commandID As Integer
Dim pmpTitle As String = ""
Dim isUIActive As Boolean

' Set up event
swAppSW = swApp
AttachEventHandlers()

' Open the model
modelName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
swModel = swApp.**OpenDoc6**(modelName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
swModelDocExt = swModel.**Extension**

' Open the Fillet PropertyManager Page,
' which causes the CommandOpenPreNotify event
' to fire
swModelDocExt.**RunCommand**(swCommands_e.swCommands_Fillet, "Fillet")

' Get the command ID if the command is a fillet,
' get the PropertyManager page title if one is active,
' and get whether the user interface is active
swApp.**GetRunningCommandInfo**(commandID, pmpTitle, isUIActive)
If pmpTitle <> "" Then Debug.Print("Title of PropertyManager page: " & pmpTitle)
Debug.Print("Is user interface active? " & isUIActive)
If (commandID = 9) Then
Debug.Print("Command ID: " & "swCommands_Fillet")
Else
Debug.Print("Command ID: " & "Not a fillet.")
End If

End Sub

Sub AttachEventHandlers()
AttachSWEvents()
End Sub
Sub AttachSWEvents()
AddHandler swAppSW.CommandOpenPreNotify, AddressOf Me.swAppSW_CommandOpenPreNotify
AddHandler swAppSW.CommandCloseNotify, AddressOf Me.swAppSW_CommandCloseNotify
End Sub
Private Function **swAppSW_CommandOpenPreNotify**(ByVal command As Integer, ByVal userCommand As Integer) As Integer
'Send message when the Fillet PropertyManager page is about to open
If (command = swCommands_e.swCommands_Fillet) Then MsgBox("Fillet PropertyManager page is about to open.")
End Function
Private Function **swAppSW_CommandCloseNotify**(ByVal command As Integer, ByVal reason As Integer) As Integer
'Send message when the Fillet PropertyManager page was canceled by clicking the X button
MsgBox("Fillet PropertyManager page was canceled.")
End Function

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
