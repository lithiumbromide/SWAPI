---
title: "Determine if Document is Dirty Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_if_Document_is_Dirty_Example_VB.htm"
---

# Determine if Document is Dirty Example (VBA)

This example shows how to determine if a document is dirty (i.e., modified since opening it) and needs to be saved.

```
'-----------------------------------------------
' Preconditions:
' 1. Open multiple model documents.
' 2. Modify one of the model documents.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the open model documents and checks
'    to see if they're dirty.
' 2. Examine the Immediate window.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.GetFirstDocument
```

```
    Do While Not swModel Is Nothing
        Debug.Print swModel.GetPathName
        Debug.Print "  Dirty? " & swModel.GetSaveFlag
        Set swModel = swModel.GetNext
    Loop
```

```
End Sub
```
