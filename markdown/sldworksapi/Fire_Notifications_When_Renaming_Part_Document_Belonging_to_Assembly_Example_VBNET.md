---
title: "Fire Notifications When Renaming Part Document Belonging to Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VBNET.htm"
---

# Fire Notifications When Renaming Part Document Belonging to Assembly Example (VB.NET)

This example shows how to fire notifications when you:

- are about to rename a part document belonging to an assembly.
- rename the part document.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\EDraw\claw\center.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Renames center to centerXXX.
' 2. Fires the PreRenameItemNotify and RenameItemNotify events.
' 3. Examine the FeatureManager design tree and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents swPart As PartDoc

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim openPart As Hashtable
        Dim errors As Integer
        Dim status As Boolean

        swModel = swApp.ActiveDoc

        'Set up event
        swPart = swModel
        openPart = New Hashtable
        AttachEventHandlers()

        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("center.sldprt", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        errors = swModelDocExt.RenameDocument("centerXXX")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        If Not swPart Is Nothing Then
            AddHandler swPart.PreRenameItemNotify, AddressOf Me.swPart_PreRenameItemNotify
            AddHandler swPart.RenameItemNotify, AddressOf Me.swPart_RenameItemNotify
        End If

    End Sub

    'Fire notification when item is about to be renamed
    Public Function swPart_PreRenameItemNotify(ByVal entType As Integer, ByVal oldName As String, ByVal newName As String) As Integer
        Debug.Print("PreRenameItemNotify fired")
    End Function
    'Fire notification when item is renamed
    Public Function swPart_RenameItemNotify(ByVal entType As Integer, ByVal oldName As String, ByVal newName As String) As Integer
        Debug.Print("RenameItemNotify fired")
    End Function

End Class
```
