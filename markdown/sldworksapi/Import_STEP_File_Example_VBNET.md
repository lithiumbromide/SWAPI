---
title: "Import STEP File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import_STEP_File_Example_VBNET.htm"
---

# Import STEP File Example (VB.NET)

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

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swPart As PartDoc
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swImportStepData As ImportStepData
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim stepFileName As String

        'Open the part document to export to a STEP file
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\db9 male.sldprt"
        swPart = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModel = swPart
        swModelDocExt = swModel.Extension

        'Export the part document to a STEP file
        stepFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\db9 male.STEP"
        status = swModelDocExt.SaveAs(stepFileName, 0, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
        swPart = Nothing

        swApp.CloseDoc("db9 male.sldprt")

        'Get import information
        swImportStepData = swApp.GetImportFileData(stepFileName)

        'If ImportStepData::MapConfigurationData is not set, then default to
        'the environment setting swImportStepConfigData; otherwise, override
        'swImportStepConfigData with ImportStepData::MapConfigurationData
        swImportStepData.MapConfigurationData = True

        'Import the STEP file
        swPart = swApp.LoadFile4(stepFileName, "r", swImportStepData, errors)
        swModel = swPart
        swModelDocExt = swModel.Extension

        'Run diagnostics on the STEP file and repair any bad faces
        errors = swPart.ImportDiagnosis(True, False, True, 0)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
