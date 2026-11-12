---
title: "Import STEP File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import_STEP_File_Example_VB.htm"
---

# Import STEP File Example (VBA)

This example shows how to import and repair a STEP file.

```
'-------------------------------------------------------------------------------
' Preconditions: Verify that the specified SOLIDWORKS Design part document to open exists.
'
' Postconditions:
' 1. Opens the specified SOLIDWORKS Design part document.
' 2. Saves the part document as a STEP file.
' 3. Closes the part document.
' 4. Imports the STEP file created in step 2.
' 5. Runs import diagnostics on the STEP file and repairs any bad faces.
' 6. Creates Imported1 in the FeatureManager design tree.
'-------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swImportStepData As SldWorks.ImportStepData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim stepFileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open the part document to export to a STEP file
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\db9 male.sldprt"
    Set swPart = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModel = swPart
    Set swModelDocExt = swModel.Extension
```

```
    'Export the part document to a STEP file
    stepFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\db9 male.STEP"
    status = swModelDocExt.SaveAs(stepFileName, 0, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
    Set swPart = Nothing

    swApp.CloseDoc "db9 male.sldprt"
```

```
    'Get import information
    Set swImportStepData = swApp.GetImportFileData(stepFileName)
```

```
    'If ImportStepData::MapConfigurationData is not set, then default to
    'the environment setting swImportStepConfigData; otherwise, override
    'swImportStepConfigData with ImportStepData::MapConfigurationData
    swImportStepData.MapConfigurationData = True
```

```
    'Import the STEP file
    Set swPart = swApp.LoadFile4(stepFileName, "r", swImportStepData, errors)
    Set swModel = swPart
    Set swModelDocExt = swModel.Extension
```

```
    'Run diagnostics on the STEP file and repair any bad faces
    errors = swPart.ImportDiagnosis(True, False, True, 0)
```

```
End Sub
```
