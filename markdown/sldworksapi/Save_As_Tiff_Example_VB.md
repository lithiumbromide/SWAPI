---
title: "Save Document as TIFF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_As_Tiff_Example_VB.htm"
---

# Save Document as TIFF Example (VBA)

## Save Document As TIFF Example (VBA)

This example shows how to:

- Set TIFF export options
- Save the active document to a **.tif** format in the same directory as the model document.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets TIFF settings.
' 2. Saves the model document as a TIFF file to the same folder as
'    the model document and overwrites any existing file of the same name
'    in that folder.
' 3. Examine the Immediate window and the folder where the TIFF file
'    was saved.
'------------------------------------------------------------------
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim sPathName As String
    Dim nRetVal As Long
    Dim nErrors As Long
    Dim nWarnings As Long
    Dim bRe As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    ' Get current TIFF settings
    Debug.Print "PrintScaleToFit        = " + Str(swApp.GetUserPreferenceToggle(swTiffPrintScaleToFit))
    Debug.Print "ScreenOrPrintCapture   = " + Str(swApp.GetUserPreferenceIntegerValue(swTiffScreenOrPrintCapture))
    Debug.Print "ImageType              = " + Str(swApp.GetUserPreferenceIntegerValue(swTiffImageType))
    Debug.Print "CompressionScheme      = " + Str(swApp.GetUserPreferenceIntegerValue(swTiffCompressionScheme))
    Debug.Print "PrintDPI               = " + Str(swApp.GetUserPreferenceIntegerValue(swTiffPrintDPI))
    Debug.Print "PrintPaperSize         = " + Str(swApp.GetUserPreferenceIntegerValue(swTiffPrintPaperSize))
    Debug.Print "PrintScaleFactor       = " + Str(swApp.GetUserPreferenceIntegerValue(swTiffPrintScaleFactor))
    Debug.Print "DrawingPaperHeight     = " + Str(swApp.GetUserPreferenceDoubleValue(swTiffPrintDrawingPaperHeight))
    Debug.Print "DrawingPaperWidth      = " + Str(swApp.GetUserPreferenceDoubleValue(swTiffPrintDrawingPaperWidth))
```

```
    ' Strip off SOLIDWORKS Design file name extension (sldprt, sldasm, or slddrw)
    ' and add TIFF extension (tif)
    sPathName = swModel.GetPathName
    sPathName = Left(sPathName, Len(sPathName) - 6)
    sPathName = sPathName + "tif"
    Debug.Print sPathName
```

```
    bRet = swModel.SaveAs4(sPathName, swSaveAsCurrentVersion, swSaveAsOptions_Silent, nErrors, nWarnings)
    If bRet = False Then
        nRetVal = swApp.SendMsgToUser2("Problems saving file.", swMbWarning, swMbOk)
    End If
```

```
End Sub
```
