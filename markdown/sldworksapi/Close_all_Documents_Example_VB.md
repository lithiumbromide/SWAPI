---
title: "Close All Documents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Close_all_Documents_Example_VB.htm"
---

# Close All Documents Example (VBA)

This example shows how to close all documents in a SOLIDWORKS Design session, except any modified documents.

```
'---------------------------------------
' Preconditions:
' 1. Open two or more model documents.
' 2. Modify the model in one model document.
' 3. Open the Immediate window.
' 4. Click Window in SOLIDWORKS Design to see the names of the
'    open model documents.
'
' Postconditions:
' 1. Closes all model documents, except the model document
'    that you modified.
' 2. Examine the Immediate window.
' 3. Click Window again to verify that all documents,
'    except the document that you modified, closed.
'----------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' If false, then all documents, excluding any dirty documents, are closed
    boolstatus = swApp.CloseAllDocuments(False)
    Debug.Print "All documents, excluding dirty documents, closed: " & boolstatus
```

```
    ' If true, then all documents, including any dirty documents, are closed
    'boolstatus = swApp.CloseAllDocuments(True)
    'Debug.Print "All documents, including dirty documents, closed: " & boolstatus
```

```
End Sub
```
