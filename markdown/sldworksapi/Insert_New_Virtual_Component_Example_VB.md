---
title: "Insert New Virtual Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Component_Example_VB.htm"
---

# Insert New Virtual Component Example (VBA)

This example shows how to insert a new part as a virtual component in an assembly and save it to an external file.

```vb
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
 Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssy As SldWorks.AssemblyDoc
Dim swComponent As SldWorks.Component2
Dim swSelMgr As SldWorks.SelectionMgr
Dim status As Long
```

```
Sub Main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
```

```
    ' Get the pre-selected planar face
    Dim swFeature  As SldWorks.Face2
    Set swSelMgr = swModel.SelectionManager
    Set swFeature = swSelMgr.GetSelectedObject6(1, 0)
```

```
    ' Create the part and insert it as a virtual component
    ' in the assembly
    status = swAssy.InsertNewVirtualPart(swFeature, swComponent)
```

```
    If status = 1 Then
```

```
        Debug.Print "Virtual component inserted!"
        Debug.Print "Name of virtual component: " & swComponent.Name2
```

```
        ' Check to see if the part is a virtual component
        Debug.Print "  Is component virtual? " & swComponent.IsVirtual
```

```
        Dim objFSO As Object
        Dim objFile As Object
        Dim compName As String
        Dim splits As Variant
```

```
        Set objFSO = CreateObject("Scripting.FileSystemObject")
        Set objFile = objFSO.GetFile(swModel.GetPathName)
```

```
        splits = Split(swComponent.Name2, "^")
        compName = objFSO.GetParentFolderName(objFile) & "\" & splits(0)
```

```
        If swComponent.GetModelDoc2.GetType = swDocPART Then
            compName = compName & ".sldprt"
        Else
            compName = compName & ".sldasm"
        End If
```

```
        Debug.Print "  Path and name of virtual component: " & compName
```

```
        Dim ret As Boolean
        ret = swComponent.SaveVirtualComponent(compName)
        If ret Then
            Debug.Print "    Virtual component saved!"
        Else
            Debug.Print "    Virtual component not saved!"
            Debug.Print "       Check the folder's attributes where to save the virtual component and check your permissions to this folder."
        End If
```

```
    Else
        Debug.Print "Error code returned when attempting to insert new part as virtual component: " & status
    End If
```

```
    swModel.ClearSelection2 (True)
```

```
End Sub
```
