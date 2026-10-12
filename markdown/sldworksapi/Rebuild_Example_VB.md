---
title: "Rebuild Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_Example_VB.htm"
---

# Rebuild Model Example (VBA)

The example shows how to rebuild an assembly by using IModelDoc2::EditRebuild3 and IModelDoc2::ForceRebuild3.

```
'---------------------------------------------
' Preconditions: Open an assembly document.
'
' Preconditions:
' 1. Attempts to rebuild only those features in the
'    assembly that need to be rebuilt and attempts
'    to force a rebuild of all of the features
'    in the assembly regardless if they need to be rebuilt.
' 2. Read each message box and click OK to close it.
'---------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim boolstatus As Boolean
    Dim topOnly As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    If swModel.EditRebuild3() Then
        MsgBox "Rebuild successful."
    Else
        MsgBox "This model has rebuild errors."
    End If
```

```
    topOnly = True
    If swModel.ForceRebuild3(topOnly) Then
        MsgBox "Forced rebuild successful."
    Else
        MsgBox "This model has rebuild errors."
    End If
```

```
End Sub
```
