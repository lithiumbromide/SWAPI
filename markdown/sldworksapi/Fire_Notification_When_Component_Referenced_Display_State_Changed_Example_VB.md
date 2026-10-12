---
title: "Fire Notification When Component Referenced Display State Changed Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Component_Referenced_Display_State_Changed_Example_VB.htm"
---

# Fire Notification When Component Referenced Display State Changed Example VB

## Fire Notification When Component Referenced Display State Changes Example (VBA)

This example shows how to fire a notification when a component's referenced display state is changed in an assembly.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Copy and paste this code in the main module.
' 2. Click Insert > Class Module and copy and paste this code
'    in the class module.
' 3. Open an assembly document that has
'    a component with multiple referenced
'    display states.
' 4. Run this macro (press F5)
' 5. Change the referenced display state of
'    a component (right-click the component, click the
'    Component Properties button, select a different
'    referenced display state, and click OK).
'
' Postconditions:
' 1. Displays a message box informing you that the referenced
'    display state of a component has changed.
' 2. Click OK to close the message box.
'---------------------------------------------------------------
'Main module
```

```
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

###### 'Class module

```vb
Option Explicit

Public WithEvents swAssem As SldWorks.AssemblyDoc

'Send message after user changes referenced display state of a component in an assembly
Private Function swAssem_ComponentReferredDisplayStateChangeNotify(ByVal componentModel As Object, ByVal compName As String, ByVal oldDSId As Long, ByVal oldDSName As String, ByVal newDSID As Long, ByVal newDSName As String) As Long
    MsgBox "The component's referenced display state has changed."
End Function
```
