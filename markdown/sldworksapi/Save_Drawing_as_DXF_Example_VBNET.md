---
title: "Save Drawing as DXF Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Drawing_as_DXF_Example_VBNET.htm"
---

# Save Drawing as DXF Example (VB.NET)

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
	Imports SolidWorks.Interop.sldworks
	Imports SolidWorks.Interop.swconst
	Imports System.Runtime.InteropServices
	Imports System
	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2
	    Dim sPathName As String
	    Dim nErrors As Integer
	    Dim nWarnings As Integer
	    Dim nRetval As Integer
	    Dim bShowMap As Boolean
	    Dim bRet As Boolean

	    Sub main()

	        swModel = swApp.ActiveDoc
	        ' Strip off SOLIDWORKS Design drawing file extension (.slddrw)
	        ' and add DXF file extension (.dxf)
	        sPathName = swModel.GetPathName
	        sPathName = Left(sPathName, Len(sPathName) - 6)
	        sPathName = sPathName + "dxf"

	        ' Show current settings

	        Debug.Print("DxfMapping = " & swApp.GetUserPreferenceToggle(swUserPreferenceToggle_e.swDxfMapping))
	        Debug.Print("DXFDontShowMap = " & swApp.GetUserPreferenceToggle(swUserPreferenceToggle_e.swDXFDontShowMap))
	        Debug.Print("DxfVersion = " & swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swDxfVersion))
	        Debug.Print("DxfOutputFonts = " & swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swDxfOutputFonts))
	        Debug.Print("DxfMappingFileIndex = " & swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swDxfMappingFileIndex))
	        Debug.Print("DxfOutputLineStyles = " & swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swDxfOutputLineStyles))
	        Debug.Print("DxfOutputNoScale = " & swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swDxfOutputNoScale))
	        Debug.Print("DxfMappingFiles = " & swApp.GetUserPreferenceStringListValue(swUserPreferenceStringListValue_e.swDxfMappingFiles))
	        Debug.Print("DxfOutputScaleFactor = " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swDxfOutputScaleFactor))
	        Debug.Print("")

	        ' Turn off showing of map
	        bShowMap = swApp.GetUserPreferenceToggle(swUserPreferenceToggle_e.swDXFDontShowMap)
	        Debug.Print("bShowMap = " & bShowMap)

	        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDXFDontShowMap, False)

	        bRet = swModel.SaveAs4(sPathName, swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, nErrors, nWarnings)

	        If bRet = False Then
	            nRetval = swApp.SendMsgToUser2("Problems saving file.", swMessageBoxIcon_e.swMbWarning, swMessageBoxBtn_e.swMbOk)
	        End If

	        ' Restore showing of map
	        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDXFDontShowMap, bShowMap)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
