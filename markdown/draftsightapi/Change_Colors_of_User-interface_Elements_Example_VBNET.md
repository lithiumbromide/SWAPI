---
title: "Change Colors of User-interface Elements Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_Colors_of_User-interface_Elements_Example_VBNET.htm"
---

# Change Colors of User-interface Elements Example (VB.NET)

This example shows how to change the colors of user-interface elements.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
'
' Postconditions:
' 1. Message boxes pop up before and after the colors of
'    DraftSight user-interface elements change.
' 2. Click OK to close each message box.
' 3. Examine and experiment with the user-interface
'    elements whose colors changed:
'    * Text in command window
'    * Crosshair
'    * Background of model
' 4. Run the macro again to reset the colors of the user-interface
'    elements to their former colors.
'----------------------------------------------------------------

Imports System
Imports System.Runtime.InteropServices
Imports DraftSight.Interop.dsAutomation

Module Module1

    Sub Main(ByVal args As String())
        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        'Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        If dsApp Is Nothing Then
            Return
        End If

        Dim dsApplicationOptions As ApplicationOptions = dsApp.GetApplicationOptions()

        'Change colors of user-interface elements

        'Set color of text of command window to blue or black, dependent on current color
        Dim dsColor As Color = dsApplicationOptions.GetElementColor(dsElementColor_e.dsElementColor_CommandWindowText)
        MsgBox("Color of text command window before changing its color: " & dsColor.GetNamedColor())
        If dsColor.GetNamedColor() = dsNamedColor_e.dsNamedColor_Blue Then
            dsColor.SetRGBColor(0, 0, 0)
        Else
            dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Blue)
        End If
        dsApplicationOptions.SetElementColor(dsElementColor_e.dsElementColor_CommandWindowText, dsColor)
        MsgBox("Color of text of command window after changing its color: " & dsColor.GetNamedColor())

        'Set color of model crosshair to red or white, dependent on current color
        dsColor = dsApplicationOptions.GetElementColor(dsElementColor_e.dsElementColor_ModelCrosshair)
        MsgBox("Color of crosshair before changing its color: " & dsColor.GetNamedColor())
        If dsColor.GetNamedColor() = dsNamedColor_e.dsNamedColor_Red Then
            dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_White)
        Else
            dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Red)
        End If
        dsApplicationOptions.SetElementColor(dsElementColor_e.dsElementColor_ModelCrosshair, dsColor)
        MsgBox("Color of crosshair after changing its color: " & dsColor.GetNamedColor())

        'Set color of background of model to white or black, dependent on current color
        dsColor = dsApplicationOptions.GetElementColor(dsElementColor_e.dsElementColor_ModelBackground)
        MsgBox("Color of model background before changing its color: " & dsColor.GetNamedColor())
        If dsColor.GetNamedColor() = dsNamedColor_e.dsNamedColor_White Then
            dsColor.SetRGBColor(0, 0, 0)
        Else
            dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_White)
        End If
        dsApplicationOptions.SetElementColor(dsElementColor_e.dsElementColor_ModelBackground, dsColor)
        MsgBox("Color of model background after changing its color: " & dsColor.GetNamedColor())

    End Sub
End Module
```
