---
title: "Get Component IDs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_IDs_Example_VBNET.htm"
---

# Get Component IDs Example (VB.NET)

This example shows how to get the component IDs of the components in an assembly and subassemblies.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document containing nested subassemblies.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the assembly and subassemblies.
' 2. Gets the name and component ID of each component in the assembly and
'    subassemblies.
' 3. Examine the Immediate window.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swConfMgr As ConfigurationManager
        Dim swConf As Configuration
        Dim swRootComp As Component2

        swModel = swApp.ActiveDoc
        swConfMgr = swModel.ConfigurationManager
        swConf = swConfMgr.ActiveConfiguration
        swRootComp = swConf.GetRootComponent3(True)
        Debug.Print("File = " & swModel.GetPathName)
        If swModel.GetType = swDocumentTypes_e.swDocASSEMBLY Then
            TraverseComponent(swRootComp, 1)
        End If

    End Sub

    Sub TraverseComponent(ByVal swComp As Component2, ByVal nLevel As Integer)
        Dim vChildComp As Object
        Dim swChildComp As Component2
        Dim sPadStr As String = ""
        Dim i As Integer

        For i = 0 To nLevel - 1
            sPadStr = sPadStr + "  "
        Next i
        vChildComp = swComp.GetChildren
        For i = 0 To UBound(vChildComp)
            swChildComp = vChildComp(i)
            Debug.Print(sPadStr & "Component name: " & swChildComp.Name2 & ", Component ID: " & swChildComp.GetID)
            TraverseComponent(swChildComp, nLevel + 1)
        Next i
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
