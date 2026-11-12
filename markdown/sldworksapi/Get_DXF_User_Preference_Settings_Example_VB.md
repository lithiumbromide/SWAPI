---
title: "Get DXF User Preference Settings Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_DXF_User_Preference_Settings_Example_VB.htm"
---

# Get DXF User Preference Settings Example (VBA)

This example shows how to get DXF user-preference settings.

```vb
'---------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim DxfVersion As Integer
Dim DxfOutputFonts As Integer
Dim DxfMappingFileIndex As Integer
Dim AutoSaveInterval As Integer

Sub mian()

Set swApp = Application.SldWorks

' Get the version of DXF for exporting
DxfVersion = swApp.GetUserPreferenceIntegerValue(swDxfVersion)

' Get whether TrueType fonts are exported (1) or only standard (0)
DxfOutputFonts = swApp.GetUserPreferenceIntegerValue(swDxfOutputFonts)
Debug.Print "Output fonts: exported =1; standard = 0: "; DxfOutputFonts

' Get the index of the map file for the file used for custom DXF mapping
DxfMappingFileIndex = swApp.GetUserPreferenceIntegerValue(swDxfMappingFileIndex)
Debug.Print "Mapping file index: "; DxfMappingFileIndex

' Get the number of operations between auto-saves
AutoSaveInterval = swApp.GetUserPreferenceIntegerValue(swAutoSaveInterval)
Debug.Print "Number of autosaves: "; AutoSaveInterval
End Sub
```
