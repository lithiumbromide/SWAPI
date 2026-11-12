---
title: "Import Models as Solids Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import_Models_as_Solids_Example_VB.htm"
---

# Import Models as Solids Example (VBA)

This example shows how to set the options to import non-native-SOLIDWORKS models into SOLIDWORKS Design as solids.

NOTE: You must set the values of both swUserPreferenceIntegerValue_e.swCreateBodyFromSurfaces and swUserPreferenceIntegerValue_e.swImportUseBrep for swUserPreferenceIntegerValue_e.swImportUseBrep to have an effect.

```
'----------------------------------------------------
' Preconditions:
' 1. Substitute the file_to_import.STEP with the
'    name of the STEP file that you want to import.
' 2. Copy the STEP file to this macro's folder.
'
' Postconditions:
' 1. Loads the file into a new document
'    and forms solids, if possible, but does
'    not directly map topologies using BREP data.
' 2. Loads the file into a new document
'    and forms solids, if possible, and
'    directly maps topologies using BREP data.
' 3. Examine both documents. Switch documents
'    by clicking Window and clicking the document to view.
' 4. Examine the FeatureManager design tree and
'    the graphics area in each document.
'-----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swImportStepData As SldWorks.ImportStepData
    Dim rtn As Boolean
    Dim retval As Long
    Dim pathname As String
    Dim errors As Long
```

```
    Set swApp = Application.SldWorks
```

```
    pathname = swApp.GetCurrentMacroPathName
    pathname = Left(pathname, InStrRev(pathname, "\"))
```

```
    ' Get swImportUseBrep value
    retval = swApp.GetUserPreferenceIntegerValue(swImportUseBrep)
```

```
    ' Set swImportUseBrep value to 1 (Do not import the model
    ' by directly mapping topologies using BREP data)
    ' Let SOLIDWORKS Design attempt to knit the surfaces into solids
    rtn = swApp.SetUserPreferenceIntegerValue(swImportUseBrep, 1)
```

```
    ' Set swCreateBodyFromSurfacesOption to swGeneralImportbyBrep
    rtn = swApp.SetUserPreferenceIntegerValue(SwConst.swUserPreferenceIntegerValue_e.swCreateBodyFromSurfacesOption, SwConst.swGeneralImportByBrep)
```

```
    ' Load the STEP file
    swApp.LoadFile4 pathname + "file_to_import.STEP", "r", swImportStepData, errors
```

```
   ' Set swImportUseBrep value to 0 (Import the model by directly mapping
   ' topologies using BREP data)
   ' Attempt to import the model by directly mapping topologies
   ' using boundary representation (BREP) data.
    rtn = swApp.SetUserPreferenceIntegerValue(swImportUseBrep, 0)
```

```
    ' Get swImportUseBrep value
    retval = swApp.GetUserPreferenceIntegerValue(swImportUseBrep)
```

```
    ' Load the STEP file
    swApp.LoadFile4 pathname + "file_to_import.STEP", "r", swImportStepData, errors
```

```
End Sub
```
