---
title: "Save Configuration Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Configuration_Data_Example_VBNET.htm"
---

# Save Configuration Data Example (VB.NET)

This example shows how to mark each configuration in a multi-configuration model as needing to be rebuilt and how to save its configuration data, including preview bitmaps, every time you save the model document.

```
'------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified file to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Activates each configuration in the model.
' 2. Sets each configuration's Rebuild/Save Mark to true, if it is false.
' 3. Saves each configuration's preview bitmap to disk.
' 4. Examine the Immediate window.
'
' NOTES:
' * In SOLIDWORKS 2013 and later, to mark each configuration
'   as needing to be rebuilt and to save its configuration data
'   every time you save the model:
'   1. Activate each configuration and set
'      IConfiguration::AddRebuildSaveMark to true.
'   2. Save the model.
' * Because this model is used elsewhere, do not
'   save changes.
'------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swConfig As Configuration
        Dim swConfMgr As ConfigurationManager
        Dim configNameArr As Object
        Dim configName As Object
        Dim fileName As String
        Dim bitmapName As String
        Dim bitmapPathName As String
        Dim status As Boolean
        Dim errors As Integer, warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\multiconfig-part-2.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swConfMgr = swModel.ConfigurationManager
        configNameArr = swModel.GetConfigurationNames

        Debug.Print("Checking each configuration's Add Rebuild/Save Mark setting after opening the model document:")

        For Each configName In configNameArr
            swConfig = swModel.GetConfigurationByName(configName)
            status = swModel.ShowConfiguration2(configName)
            Debug.Print("   " & configName & "'s" & " Add Rebuild/Save Mark = " & swConfig.AddRebuildSaveMark)
            If swConfig.AddRebuildSaveMark = False Then
                swConfig.AddRebuildSaveMark = True
                bitmapName = configName + ".bmp"
                Debug.Print("      Resetting " & configName & "'s" & " Add Rebuild/Save Mark = " & swConfig.AddRebuildSaveMark)
                bitmapPathName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\" + bitmapName
                status = swApp.GetPreviewBitmapFile(fileName, configName, bitmapPathName)
                If status Then
                    Debug.Print("      "  & configName & "'s " & "preview bitmap written to disk: " & bitmapPathName)
                End If
            End If
        Next

        'Save the model to save each configuration's data with the model
        'status = swModel.Save3(swSaveAsOptions_e.swSaveAsOptions_Silent, errors, warnings)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
