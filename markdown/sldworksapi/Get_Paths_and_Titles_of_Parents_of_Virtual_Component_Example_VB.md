---
title: "Get Paths and Titles of Parents of Virtual Component (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_VB.htm"
---

# Get Paths and Titles of Parents of Virtual Component (VBA)

This example shows how to get the paths and titles of the parent assembly components of a virtual component.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open:
'    public_documents\samples\tutorial\api\assem2.sldasm
' 2. Open the Immediate window.
'
' Postconditions: The paths and titles of the parent
' assembly components, up to and including the first non-virtual
' parent assembly component, are printed in the Immediate Window.
'------------------------------------------------------------
Option Explicit
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Set swApp = Application.SldWorks
```

```
    Dim doc As ModelDoc2
    Set doc = swApp.ActiveDoc
    If doc Is Nothing Then Exit Sub
    If doc.GetType <> swDocASSEMBLY Then Exit Sub
```

```
    Dim asm As AssemblyDoc
    Set asm = doc
```

```
    Dim components As Variant
    components = asm.GetComponents(False)   ' Get all components
```

```
    If IsArray(components) Then
        Debug.Print "Virtual components in this assembly:"
```

```
        Dim vComp As Variant
        For Each vComp In components
            Dim comp As Component2
            Set comp = vComp
```

```
            Dim compDoc As ModelDoc2
            Set compDoc = comp.GetModelDoc2
            If Not compDoc Is Nothing Then
                Dim bResult3 As Boolean
                Dim pathChain As Variant
                Dim titleChain As Variant
                bResult3 = compDoc.Extension.IsVirtualComponent3(pathChain, titleChain)
```

```
                If bResult3 <> False Then
                    Debug.Print "  Virtual component name: " & comp.Name2
```

```
                    Debug.Print "    " & "Paths:"
                    Dim vPath As Variant
                    For Each vPath In pathChain
                        Debug.Print "      " & vPath
                    Next
```

```
                    Debug.Print "    " & "Titles:"
                    Dim vTitle As Variant
                    For Each vTitle In titleChain
                        Debug.Print "      " & vTitle
                    Next
                End If
            Else
                Debug.Print comp.Name2 & " <<< NOT LOADED >>>"
            End If
        Next
    End If
```

```
End Sub
```
