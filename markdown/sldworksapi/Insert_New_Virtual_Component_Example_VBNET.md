---
title: "Insert New Virtual Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Component_Example_VBNET.htm"
---

# Insert New Virtual Component Example (VB.NET)

This example shows how to insert a new part as a virtual component in an assembly and save it to an external file.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
' 2. Select a planar face on the assembly.
' 3. Open the Immediate window.
' 4. Step through this macro by pressing F8.
'
' Postconditions:
' 1. Inserts a new part as a virtual component in the assembly.
' 2. Attempts to save the virtual component to an external file.
' 3. Examine the Immediate window and FeatureManager design tree.
'
' NOTE: Because this assembly is used elsewhere, do not
' save changes.
'---------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swAssy As AssemblyDoc
    Dim swComponent As Component2
    Dim swSelMgr As SelectionMgr
    Dim objFSO As Object
    Dim objFile As Object
    Dim compName As String
    Dim splits As Object
    Dim status As Integer

    Sub Main()

        swModel = swApp.ActiveDoc
        swAssy = swModel

        ' Get the pre-selected planar face
        Dim swFeature As Face2
        swSelMgr = swModel.SelectionManager
        swFeature = swSelMgr.GetSelectedObject6(1, 0)

        ' Create the part and insert it as a virtual component
        ' in the assembly
        status = swAssy.InsertNewVirtualPart(swFeature, swComponent)

        If status = 1 Then
            Debug.Print("Virutal component inserted!")
            Debug.Print("Name of virtual component: " & swComponent.Name2)

            ' Check to see if the part is a virtual component
            Debug.Print("  Is component virtual? " & swComponent.IsVirtual)

            objFSO = CreateObject("Scripting.FileSystemObject")
            objFile = objFSO.GetFile(swModel.GetPathName)

            splits = Split(swComponent.Name2, "^")
            compName = objFSO.GetParentFolderName(objFile) & "\" & splits(0)

            Dim compModel As ModelDoc2
            compModel = swComponent.GetModelDoc

            If compModel.GetType = swDocumentTypes_e.swDocPART Then
                compName = compName & ".sldprt"
            Else
                compName = compName & ".sldasm"
            End If

            Debug.Print("  Path and name of virtual component: " & compName)

            Dim ret As Boolean
            ret = swComponent.SaveVirtualComponent(compName)
            If ret Then
                Debug.Print("    Virtual component saved!")
            Else
                Debug.Print("    Virtual component not saved!")
                Debug.Print("       Check the folder's attributes where to save the virtual component and check your permissions to this folder.")
            End If

        Else
            Debug.Print("Error code returned when attempting to insert new part as virtual component: " & status)
        End If

        swModel.ClearSelection2(True)

    End Sub

    Public swApp As SldWorks

End Class
```
