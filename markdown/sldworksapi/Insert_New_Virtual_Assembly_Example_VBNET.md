---
title: "Insert New Virtual Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Assembly_Example_VBNET.htm"
---

# Insert New Virtual Assembly Example (VB.NET)

This example shows how to insert an assembly as a virtual component into the main assembly or selected sub-assembly.

```vb
'-------------------------------------------------------------------------
' Preconditions: Open an assembly document.
'
' Postconditions: A new virtual component displays in the
' FeatureManager design tree.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Dim swDoc As ModelDoc2
    Dim swADoc As AssemblyDoc
    Dim swComp As Component2
    Dim status As Long
    Sub main()
        swDoc = swApp.ActiveDoc
        swADoc = swDoc
        swComp = Nothing
        status = swADoc.InsertNewVirtualAssembly(swComp)
        If (swComp Is Nothing) Then
            MsgBox("Virtual component did not get created.")
        Else
            Debug.Print("New virtual component:  " & swComp.Name2)
            Debug.Print("Is virtual: " & swComp.IsVirtual)
        End If
    End Sub

    Public swApp As SldWorks
End Class
```
