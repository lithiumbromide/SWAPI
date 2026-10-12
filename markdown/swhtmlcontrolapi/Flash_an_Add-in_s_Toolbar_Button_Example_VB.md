---
title: "Flash an Add-in's Toolbar Button Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swhtmlcontrolapi/Flash_an_Add-in_s_Toolbar_Button_Example_VB.htm"
---

# Flash an Add-in's Toolbar Button Example (VBA)

This example shows how to flash an add-in's CommandManager-style toolbar button, similar to what you see in many of the SOLIDWORKS online tutorials.

NOTE: The first example shows how to flash an add-in's CommandManager-style toolbar button using the ISwHtmlInterface interface. The second example shows how to do this using both the ISwHtmlInterface and ISldWorks interfaces.

#### Example 1

```vb
'--------------------------------------------------------------
'
' Preconditions: SOLIDWORKS is running and
'                the Fastening Feature toolbar is visible.
'
' Postconditions: Each time you click the Continue button in the
'                Microsoft Visual Basic IDE, a different toolbar button on the
'                Fastening Feature toolbar flashes and that button's
'                tooltip is displayed.
'
'--------------------------------------------------------------

Option Explicit

Dim swApp As Object
Dim newButtonID As Long
Dim flashCommands As Long
Dim userId As Long

Sub main()

Set swApp = CreateObject("SwHtmlControl.SwHtmlInterface.14")
For userId = 40712 To 40715 'Currently bound IDs for each button on the Fastening Feature toolbar
    newButtonID = swApp.GetCommandID("{65F06ACE-ED12-47FA-AB16-DB6ADE842AB5}", userId)
    flashCommands = "" + CStr(newButtonID) + ""
    swApp.ShowBubbleTooltip newButtonID, flashCommands, 0, "", ""
   Stop
Next

End Sub
```

#### Example 2

```vb
'--------------------------------------------------------------
'
' Preconditions: SOLIDWORKS is running and
'                the Fastening Feature toolbar is visible.
'
' Postconditions: Each time you click the Continue button in the
'                Microsoft Visual Basic IDE, a different toolbar button on the
'                Fastening Feature toolbar flashes and that button's
'                tooltip is displayed.
'
'--------------------------------------------------------------
Option Explicit

Dim swHTMLInt As Object
Dim swApp As Object
Dim newButtonID As Long
Dim flashCommands As Long
Dim userId As Long

Sub main()

Set swApp = Application.SldWorks
Set swHTMLInt = CreateObject("SwHtmlControl.SwHtmlInterface.14")

For userId = 40712 To 40715 'Currently bound IDs for each button on the Fastening Feature toolbar
    newButtonID = swHTMLInt.GetCommandID("{65F06ACE-ED12-47FA-AB16-DB6ADE842AB5}", userId)
    flashCommands = "" + CStr(newButtonID) + ""
    swApp.ShowBubbleTooltip newButtonID, flashCommands, 0, "", ""
    Stop
Next
End Sub
```
