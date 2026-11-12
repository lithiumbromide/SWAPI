---
title: "Insert New Virtual Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Assembly_Example_VB.htm"
---

# Insert New Virtual Assembly Example (VBA)

This example shows how to insert an assembly as a virtual component into the main assembly or selected sub-assembly.

```vb
'-------------------------------------------------------------------------
' Preconditions: Open an assembly document.
'
' Postconditions: A new virtual component displays in the
' FeatureManager design tree.
'---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim swDoc As SldWorks.ModelDoc2
Dim swADoc As SldWorks.AssemblyDoc
Dim swComp As SldWorks.Component2
Dim status As Long
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
    Set swDoc = swApp.ActiveDoc
    Set swADoc = swDoc
    Set swComp = Nothing
    status = swADoc.InsertNewVirtualAssembly(swComp)
    If (swComp Is Nothing) Then
        MsgBox ("Virtual component did not get created.")
    Else
        Debug.Print ("New virtual component:  " & swComp.Name2)
        Debug.Print ("Is virtual: " & swComp.IsVirtual)
    End If
End Sub
```
