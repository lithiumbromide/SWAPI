---
title: "Import IGES File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import_IGES_File_Example_VB.htm"
---

# Import IGES File Example (VBA)

This example shows how to import an IGES file.

```
'----------------------------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the file specified to import exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Imports the specified file into SOLIDWORKS Design.
' 2. Examine the graphics area, FeatureManager design tree, and Immediate window.
'------------------------------------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swImportData As SldWorks.ImportIgesData
    Dim Err As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.LoadFile4("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\importexport\gasket.igs", "r", swImportData, Err)
```

```
    Debug.Print ("Error (0 = no error): " & Err)
```

```
End Sub
```
