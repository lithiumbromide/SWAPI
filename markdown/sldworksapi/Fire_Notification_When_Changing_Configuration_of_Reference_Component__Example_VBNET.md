---
title: "Fire Notification When Changing Configuration of Reference Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_Configuration_of_Reference_Component__Example_VBNET.htm"
---

# Fire Notification When Changing Configuration of Reference Component Example (VB.NET)

This example shows how to fire an event when changing the configuration of a reference component in an assembly.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document that contains at least one
'    subassembly (i.e., reference component) that has multiple
'    configurations.
' 2. Make sure that the Tools > Options > Stop VSTA debugger on macro exit
'    checkbox is not selected.
' 3. Run this macro (press F5).
' 4. Right-click a subassembly and select Configure Component.
' 5. In the Configuration column on the Modify Configurations
'    dialog, select a different configuration and click OK.
'
' Postconditions:
' 1. Displays a message box informing you that the component's
'    configuration is being changed. Check the taskbar for
'    the message box.
' 2. Click OK to close the message box and
'    the Modify Configurations dialog.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents swAssemblyDoc As AssemblyDoc

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim openAssem As Hashtable

        swModel = swApp.ActiveDoc

        ' Set up event
        swAssemblyDoc = swModel
        openAssem = New Hashtable
        AttachEventHandlers()

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssemblyDoc.ComponentConfigurationChangeNotify, AddressOf Me.swAssemblyDoc_ComponentConfigurationChangeNotify
    End Sub

    Private Function swAssemblyDoc_ComponentConfigurationChangeNotify(ByVal componentName As String, ByVal oldConfigurationName As String, ByVal newConfigurationName As String) As Integer
        ' Display message when user is changing a reference component's configuration
        MsgBox("A component's configuration is being changed. Component name: " & componentName & ", old configuration name: " + oldConfigurationName & ", and new configuration name: " & newConfigurationName)
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
