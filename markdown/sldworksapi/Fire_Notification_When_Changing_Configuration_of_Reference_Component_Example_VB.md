---
title: "Fire Notification When Changing Configuration of Reference Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_Configuration_of_Reference_Component_Example_VB.htm"
---

# Fire Notification When Changing Configuration of Reference Component Example (VBA)

This example shows how to fire an event when changing the configuration of a reference component in an assembly.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Copy and paste this code in the main module.
 ' 2. Click Insert > Class Module and copy and past this code
 '    the class module.
 ' 3. Open an assembly document that contains at least one
 '    subassembly (i.e., reference component) that has
 '    multiple configurations.
 ' 4. Run this macro (press F5).
 ' 5. Right-click a subassembly and select Configure Component.
 ' 6. In the Configuration column on the Modify Configurations
 '    dialog, select a different configuration and click OK.
 '
 ' Postconditions:
 ' 1. Displays a message box informing you that a component's
 '    configuration is being changed.
 ' 2. Click OK to close the message box and
 '    the Modify Configurations dialog.
 '---------------------------------------------------------------
 'Main module
Option Explicit

 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssem As SldWorks.AssemblyDoc
 Dim swAssemEvents As Class1

 Sub main()

 Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc

 'Set up events
 Set swAssem = swModel
 Set swAssemEvents = New Class1
 Set swAssemEvents.swAssem = swApp.ActiveDoc

 End Sub
```

###### 'Class module

```vb
Option Explicit

Public WithEvents swAssem As SldWorks.AssemblyDoc
'Send message when user is changing the configuration of a reference component
Private Function swAssem_ComponentConfigurationChangeNotify(ByVal componentName As String, ByVal oldConfigurationName As String, ByVal newConfigurationName As String) As Long
    MsgBox "A component's configuration is being changed: Component name: " & componentName & ", previous configuration name: " & oldConfigurationName & ", and new configuration name: " & newConfigurationName
End Function
```
