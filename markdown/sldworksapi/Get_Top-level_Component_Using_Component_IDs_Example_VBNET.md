---
title: "Get Top-level Components Using Component IDs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Top-level_Component_Using_Component_IDs_Example_VBNET.htm"
---

# Get Top-level Components Using Component IDs Example (VB.NET)

This example shows how to get the top-level components in an assembly using their component IDs.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document containing subassemblies.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the assembly.
' 2. Gets the name and component ID of each top-level component
'    in the assembly.
' 3. Adds each component ID to an array and traverses the array.
'    a. Gets each top-level component using its component ID.
'    b. Gets the name and component ID of each top-level component
'       in the assembly.
' 4. Examine the Immediate window and FeatureManager design tree.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssemblyDoc As AssemblyDoc
        Dim swConfMgr As ConfigurationManager
        Dim swConf As Configuration
        Dim swRootComp As Component2
        Dim vChildComp As Object
        Dim swChildComp As Component2
        Dim i As Integer
        Dim compID As Integer
        Dim compIDs() As Integer
        Dim nbrComp As Integer

        swModel = swApp.ActiveDoc
        swAssemblyDoc = swModel
        swConfMgr = swModel.ConfigurationManager
        swConf = swConfMgr.ActiveConfiguration
        swRootComp = swConf.GetRootComponent3(True)

        Debug.Print("Get top-level components by traversing assembly:")
        vChildComp = swRootComp.GetChildren
        nbrComp = UBound(vChildComp)
        ReDim compIDs(nbrComp)
        For i = 0 To nbrComp
            swChildComp = vChildComp(i)
            compID = swChildComp.GetID
            Debug.Print("  Component name: " & swChildComp.Name2 & ", Component ID: " & compID)
            ' Add component ID to an array
            compIDs(i) = compID
        Next i

        Debug.Print("")

        Debug.Print("Get top-level components using component IDs:")
        swChildComp = Nothing
        nbrComp = UBound(compIDs)
        For i = 0 To UBound(compIDs)
            compID = compIDs(i)
            swChildComp = swAssemblyDoc.GetComponentByID(compID)
            Debug.Print("  Component name: " & swChildComp.Name2 & ", Component ID: " & swChildComp.GetID)
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
