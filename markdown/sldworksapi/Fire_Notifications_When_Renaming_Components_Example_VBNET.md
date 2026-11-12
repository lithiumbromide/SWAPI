---
title: "Fire Notifications When Renaming Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notifications_When_Renaming_Components_Example_VBNET.htm"
---

# Fire Notifications When Renaming Components Example (VB.NET)

This example shows how to fire notifications when you:

- are about to rename a component.
- rename a component.

```
'---------------------------------------------------
' Preconditions:
' 1. Verify that these documents exist in public_documents\samples\tutorial\api:
'    * beam_boltconnection.sldasm
'    * beam with holes.sldprt
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Open public_documents\samples\tutorial\api\beam_boltconnection.sldasm.
' 2. Fires pre-notification before appending
'    123 to each assembly component's name.
' 3. Fires notification when appending 123 to
'    each assembly component's name.
' 4. Examine the FeatureManager design tree and the
'    Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do
' not save changes.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents swAssy As AssemblyDoc

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swConfigMgr As ConfigurationManager
        Dim swConfig As Configuration
        Dim swRootComp As Component2
        Dim Children As Object
        Dim swChild As Component2
        Dim swSelMgr As SelectionMgr
        Dim swSelData As SelectData
        Dim ChildCount As Integer
        Dim oldName As String
        Dim newName As String
        Dim bOldSetting As Boolean
        Dim bRet As Boolean
        Dim i As Integer
        Dim openAssem As Hashtable

        swModel = swApp.ActiveDoc
        swAssy = swModel

        ' Set up event
        swAssy = swModel
        openAssem = New Hashtable
        AttachEventHandlers()

        swConfigMgr = swModel.ConfigurationManager
        swConfig = swConfigMgr.ActiveConfiguration
        swRootComp = swConfig.GetRootComponent3(True)
        bOldSetting = swApp.GetUserPreferenceToggle(swUserPreferenceToggle_e.swExtRefUpdateCompNames)
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swExtRefUpdateCompNames, False)
        Children = swRootComp.GetChildren
        ChildCount = UBound(Children)
        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData
        For i = 0 To ChildCount
            swChild = Children(i)
            ' Changing component name requires component to be selected
            bRet = swChild.Select4(False, swSelData, False)
            oldName = swChild.Name2
            newName = oldName & " 123"
            swChild.Name2 = newName
        Next i
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swExtRefUpdateCompNames, bOldSetting)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssy.PreRenameItemNotify, AddressOf Me.swAssy_PreRenameItemNotify
        AddHandler swAssy.RenameItemNotify, AddressOf Me.swAssy_RenameItemNotify
    End Sub

    Private Function swAssy_PreRenameItemNotify(ByVal EntityType As Integer, ByVal oldName As String, ByVal newName As String) As Integer
        Debug.Print("PRE-NOTIFICATION - about to rename component: " & oldName)
    End Function
    Private Function swAssy_RenameItemNotify(ByVal EntityType As Integer, ByVal oldName As String, ByVal newName As String) As Integer
        Debug.Print("NOTIFICATION - rename component: " & newName)
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
