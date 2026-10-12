---
title: "Fire Notification When Component Referenced Display State Changes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Component_Referenced_Display_State_Changes_Example_VBNET.htm"
---

# Fire Notification When Component Referenced Display State Changes Example (VB.NET)

This example shows how to fire a notification when a component's referenced display state is changed in assembly.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document that has
'    a component with multiple referenced
'    display states.
' 2. Make sure that Tools > Options > Stop VSTA
'    debugger on macro exit is not selected.
' 3. Run this macro (press F5)
' 4. Change the referenced display state of
'    a component (right-click the component, click the
'    Component Properties button, select a different
'    referenced display state, and click OK).
'
' Postconditions:
' 1. Displays a message box informing you that the referenced
'    display state of a component has changed. Check the
'    taskbar for the message box.
' 2. Click OK to close the message box.
'---------------------------------------------------------------
Option Explicit On

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents swAssem As AssemblyDoc

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim openAssem As Hashtable
        swModel = swApp.ActiveDoc

        'Set up events
        swAssem = swModel
        openAssem = New Hashtable
        AttachEventHandlers()

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssem.ComponentReferredDisplayStateChangeNotify, AddressOf Me.swAssem_ComponentReferredDisplayStateChangeNotify
    End Sub

    Private Function swAssem_ComponentReferredDisplayStateChangeNotify(ByVal componentModel As Object, ByVal compName As String, ByVal olDSId As Integer, ByVal oldDSName As String, ByVal newDSId As Integer, ByVal newDSName As String) As Integer
        'Send message after user changes referenced display state of a component
        MsgBox("The referenced display state of a component has changed.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
