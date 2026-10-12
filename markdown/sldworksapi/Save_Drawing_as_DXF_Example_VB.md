---
title: "Save Drawing as DXF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Drawing_as_DXF_Example_VB.htm"
---

# Save Drawing as DXF Example (VBA)

This example shows how to save the current drawing file as a DXF file in the same folder.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets and sets DXF-related system settings.
' 2. Saves the drawing as a DXF file in the same folder as the drawing,
'    overwriting any existing file of the same name.
' 3. Examine the Immediate window and the folder to which the DXF file
'    was saved.
'----------------------------------------------------------------------------
Option Explicit
```

```vb
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim sPathName               As String
     Dim nErrors                 As Long
     Dim nWarnings               As Long
     Dim nRetval                 As Long
     Dim bShowMap                As Boolean
     Dim bRet                    As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
    ' Strip off SOLIDWORKS Design drawing file extension (.slddrw)
     ' and add DXF file extension (.dxf)
     sPathName = swModel.GetPathName
     sPathName = Left(sPathName, Len(sPathName) - 6)
     sPathName = sPathName + "dxf"
    ' Show current settings
     Debug.Print "DxfMapping             = " & swApp.GetUserPreferenceToggle(swDxfMapping)
     Debug.Print "DXFDontShowMap         = " & swApp.GetUserPreferenceToggle(swDXFDontShowMap)
     Debug.Print "DxfVersion             = " & swApp.GetUserPreferenceIntegerValue(swDxfVersion)
     Debug.Print "DxfOutputFonts         = " & swApp.GetUserPreferenceIntegerValue(swDxfOutputFonts)
     Debug.Print "DxfMappingFileIndex    = " & swApp.GetUserPreferenceIntegerValue(swDxfMappingFileIndex)
     Debug.Print "DxfOutputLineStyles    = " & swApp.GetUserPreferenceIntegerValue(swDxfOutputLineStyles)
     Debug.Print "DxfOutputNoScale       = " & swApp.GetUserPreferenceIntegerValue(swDxfOutputNoScale)
     Debug.Print "DxfMappingFiles        = " & swApp.GetUserPreferenceStringListValue(swDxfMappingFiles)
     Debug.Print "DxfOutputScaleFactor   = " & swApp.GetUserPreferenceDoubleValue(swDxfOutputScaleFactor)
     Debug.Print ""
    ' Turn off showing of map
     bShowMap = swApp.GetUserPreferenceToggle(swDXFDontShowMap)
     Debug.Print "bShowMap = " & bShowMap
    swApp.SetUserPreferenceToggle swDXFDontShowMap, False
    bRet = swModel.SaveAs4(sPathName, swSaveAsCurrentVersion, swSaveAsOptions_Silent, nErrors, nWarnings)
    If bRet = False Then
         nRetval = swApp.SendMsgToUser2("Problems saving file.", swMbWarning, swMbOk)
     End If
    ' Restore showing of map
     swApp.SetUserPreferenceToggle swDXFDontShowMap, bShowMap
End Sub
```
