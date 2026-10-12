---
title: "Determine if OLE Objects are Linked or Embedded Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_if_OLE_Objects_are_Linked_or_Embedded_Example_VB.htm"
---

# Determine if OLE Objects are Linked or Embedded Example (VBA)

This example shows how to determine if the OLE objects on a document are linked to external files or embedded in the document.

```
'------------------------------------------
' Preconditions:
' 1. Open a model document that contains
'    one or more OLE objects.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether each OLE object is linked
'    or embedded in the model document.
' 2. Examine the Immediate window.
'-----------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim nCount As Long
Dim ub As Long
Dim oleobjoptions As Long
Dim vOleObjs As Variant
Dim i as Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    Debug.Print "Number of OLE objects on document = " & swModelDocExt.GetOLEObjectCount(oleobjoptions)
```

```
    vOleObjs = swModelDocExt.GetOLEObjects(oleobjoptions)
    ub = UBound(vOleObjs)
    For i = 0 To ub
        Debug.Print "OLE object " & i & " linked (OLE object is embedded if False)? " & vOleObjs(0).IsLinked
    Next i
```

```
End Sub
```
