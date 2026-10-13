---
title: "Add Buttons to Task Pane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Buttons_to_Task_Pane_Example_VBNET.htm"
---

# Add Buttons to Task Pane Example (VB.NET)

This example shows how to add standard SOLIDWORKS and custom buttons to the Task Pane.

```
'-----------------------------------------------------------------------
' 1. Copy save.png from public_documents\samples\tutorial\api to this macro's
'    SwMacro folder.
' 2. Clear the Stop VSTA debugger on macro exit check box if selected
'    in Tools > Options > System Options.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens the Task Pane and loads the My Calendar control with
'    the specified standard and custom buttons at the
'    top of the pane.
' 2. Click each button from left to right and examine the Immediate
'    window after each click.
' 3. Click the Stop Debugging button in the IDE.
' 4. Select the Stop VSTA debugger on macro exit check box in
'    Tools > Options > System Options if cleared in
'    Preconditions step 2.
'----------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Imports System.Collections

Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public WithEvents swTaskPane As TaskpaneView

    Public buttonIdx As Integer

    Public Sub Main()

        Dim result As Boolean

        Dim folder As String

        Dim bitmap As String

        Dim toolTip As String

        Dim ctrlName As String

        Dim ctrlLicKey As String

        folder = swApp.GetCurrentMacroPathFolder + "\"

        ' Use default
image for Task Pane tab

        bitmap = ""

        toolTip = "My Calendar"

        ctrlName = "My.Calendar"

        ctrlLicKey = ""

        swTaskPane = swApp.CreateTaskpaneView2(bitmap, toolTip)

        ' Add standard and custom buttons to Task
Pane

        result = swTaskPane.AddCustomButton(folder & "save.png", "Save (custom png)")

        result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_e.swTaskPaneBitmapsOptions_Next, "Next (standard)")

        result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_e.swTaskPaneBitmapsOptions_Back, "Back (standard)")

        result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_e.swTaskPaneBitmapsOptions_Ok, "OK (standard)")

        result = swTaskPane.AddStandardButton(swTaskPaneBitmapsOptions_e.swTaskPaneBitmapsOptions_Close, "Close (standard)")

        ' Add control to Task Pane for the buttons

        swTaskPane.AddControl(ctrlName, ctrlLicKey)

        ' Set up events

        AttachEventHandlers()

    End Sub

    Sub AttachEventHandlers()

        AttachSWEvents()

    End Sub

    Sub AttachSWEvents()

        AddHandler swTaskPane.TaskPaneActivateNotify, AddressOf Me.swTaskPane_TaskPaneActivateNotify

        AddHandler swTaskPane.TaskPaneDestroyNotify, AddressOf Me.swTaskPane_TaskPaneDestroyNotify

        AddHandler swTaskPane.TaskPaneToolbarButtonClicked, AddressOf Me.swTaskPane_TaskPaneToolbarButtonClicked

    End Sub

    Public Function swTaskPane_TaskPaneActivateNotify() As Integer

        If Not
(swTaskPane.GetButtonState(0)) Then

            For buttonIdx = 0 To 20

                swTaskPane.SetButtonState(buttonIdx,
True)

            Next

        Else

            For buttonIdx = 0 To 20

                swTaskPane.SetButtonState(buttonIdx,
False)

            Next

        End If

    End Function

    Public Function swTaskPane_TaskPaneDestroyNotify() As Integer

        MsgBox("Remove control from Task Pane?")

    End Function

    Public Function swTaskPane_TaskPaneToolbarButtonClicked(ByVal ButtonIndex As Integer) As Integer

        Select Case (ButtonIndex + 1)

            Case 1
                Debug.Print("Save (custom png) button clicked.")
            Case 2
                Debug.Print("Next button clicked.")
            Case 3
                Debug.Print("Back button clicked.")
            Case 4
                Debug.Print("Okay button clicked.")
            Case 5
                Debug.Print("Close button clicked and tab deleted.")
                swTaskPane.DeleteView()

        End Select

    End Function

    ''' <summary>

    ''' The SldWorks swApp variable is pre-assigned for you.

    ''' </summary>

    Public swApp As SldWorks

End Class
```
