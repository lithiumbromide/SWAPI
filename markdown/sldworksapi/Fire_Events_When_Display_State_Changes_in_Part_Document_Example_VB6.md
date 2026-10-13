---
title: "Fire Events When Display State Changes in Part Document (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VB6.htm"
---

# Fire Events When Display State Changes in Part Document (VBA)

## Fire Events When Display State Changes in Part Document Example (VBA)

This example shows how to fire the events related to changing display states of a configuration in a part document.

- [Module](#Module)
- [Class Module](#Class)

Module

```vb
'---------------------------------------------------------------
' Preconditions:
' 1. Open a part document that has
'    a configuration with multiple display states.
' 2. Run this macro in debug mode.
' 3. Change the display state of the active configuration in SOLIDWORKS Design
'    (click the ConfigurationManager tab and double-click
'    a different display state).
'
' Postcondition: A message box is displayed informing
' you that the display state is about change. After the display state changes,
' another message box is displayed informing you that the display
' state has changed.
'---------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim swPartEvents As Class1

Sub main()
Set swApp = Application.SldWorks
Set swPart = swApp.ActiveDoc

'Set up events
Set swPartEvents = New Class1
Set swPartEvents.swPart = swApp.ActiveDoc
End Sub
```

Class Module

```vb
Option Explicit

Public WithEvents swPart As SldWorks.PartDoc

Private Function swPart_ActiveDisplayStateChangePreNotify() As Long
'Send message when user changes display state in the ConfigurationManager
    MsgBox "The active configuration's display state is about to change."
End Function

Private Function swPart_ActiveDisplayStateChangePostNotify(ByVal DisplayStateName As String) As Long
'Send message after user changes display state in the ConfigurationManager
    MsgBox "The active configuration's display state has changed."
End Function
```
