---
title: "Fire Events When Display State Changes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_Example_VB.htm"
---

# Fire Events When Display State Changes Example (VBA)

This example shows how to fire the events related to changing display states of a configuration in an assembly document.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Copy Main module into your macro's main module.
' 2. Click Insert > Class module and copy Class module into that module.
' 3. Open an assembly document that has a configuration with multiple
'    display states.
'    a. Run this macro in debug mode.
'    b. Change the display state of the active configuration in SOLIDWORKS Design
'       (click the ConfigurationManager tab and double-click
'       a different display state).
'
' Postconditions:
' 1. Displays a message box informing you that the display state is about to
'    change.
' 2. After the display state changes, displays another message informing you
'    that the display state has changed.
'
' NOTE: This example also fires these events when you change
' configurations in an assembly document.
'---------------------------------------------------------------
'Main module
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssem As SldWorks.AssemblyDoc
Dim swAssemEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    'Set up events
    Set swAssem = swModel
    Set swAssemEvents = New Class1
    Set swAssemEvents.swAssem = swApp.ActiveDoc
```

```
End Sub
```

```
Back to top
```

```
'Class module
Option Explicit
```

```
Public WithEvents swAssem As SldWorks.AssemblyDoc
```

```
'Send message when user changes display state in the ConfigurationManager
Private Function swAssem_ActiveDisplayStateChangePreNotify() As Long
    MsgBox "The active configuration's display state is about to change."
End Function
```

```
'Send message after user changes display state in the ConfigurationManager
Private Function swAssem_ActiveDisplayStateChangePostNotify(ByVal DisplayStateName As String) As Long
    MsgBox "The active configuration's display state has changed."
End Function
```
