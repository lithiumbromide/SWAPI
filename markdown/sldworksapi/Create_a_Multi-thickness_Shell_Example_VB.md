---
title: "Creating a Multi Thickness Shell Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_a_Multi-thickness_Shell_Example_VB.htm"
---

# Creating a Multi Thickness Shell Example (VBA)

## Create a Multi-thickness Shell Example (VBA)

This example shows how to create a multi-thickness shell.

```
'--------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\box.sldprt.
'
' Postconditions:
' 1. Marks the faces to remove.
' 2. Marks the face to shell.
' 3. Sets the thickness of the face to shell.
' 4. Inserts Shell1.
' 5. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim Part As SldWorks.ModelDoc2
    Dim boolstatus As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Part = swApp.ActiveDoc
    Part.ClearSelection2 True
```

```
    'Mark the faces to remove with a mark of 1
    boolstatus = Part.Extension.SelectByRay(-7.62012496738862E-03, 2.99999999999159E-02, 2.14688454421434E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 7.62535384051002E-04, 2, False, 1, 0)
    boolstatus = Part.Extension.SelectByRay(-1.46810566606064E-02, 2.48617446113713E-02, 4.60521566346301E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 7.62535384051002E-04, 2, True, 1, 0)
    'Mark the face to shell with a mark of 2
    boolstatus = Part.Extension.SelectByRay(4.38932166734958E-02, 2.08576911617797E-02, 2.73030283917137E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 7.62535384051002E-04, 2, False, 2, 0)
    'Set the thickness of the face
    Part.InsertFeatureShellAddThickness 0.05
    'Insert multi-thickness shell feature
    Part.InsertFeatureShell 0.01, False
```

```
End Sub
```
