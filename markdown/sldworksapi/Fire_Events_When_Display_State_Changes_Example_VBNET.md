---
title: "Fire Events When Display State Changes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_Example_VBNET.htm"
---

# Fire Events When Display State Changes Example (VB.NET)

This example shows how to fire the events related to changing display states of a configuration in an assembly document.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document that has a configuration with multiple
'    display states.
' 2. Run this macro in debug mode.
' 3. Change the display state of the active configuration in SOLIDWORKS Design
'    (click the ConfigurationManager tab and double-click
'    a different display state).
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
Option Explicit On
```

```vb
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
         AddHandler swAssem.ActiveDisplayStateChangePreNotify, AddressOf Me.swAssem_ActiveDisplayStateChangePreNotify
         AddHandler swAssem.ActiveDisplayStateChangePostNotify, AddressOf Me.swAssem_ActiveDisplayStateChangePostNotify
     End Sub

    Private Function swAssem_ActiveDisplayStateChangePreNotify() As Integer
     'Send message when user changes display state in the ConfigurationManager
         MsgBox("The active configuration's display state is about to change.")
     End Function

    Private Function swAssem_ActiveDisplayStateChangePostNotify(ByVal DisplayStateName As String) As Integer
     'Send message after user changes display state in the ConfigurationManager
         MsgBox("The active configuration's display state has changed.")
     End Function

    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks
End Class
```
