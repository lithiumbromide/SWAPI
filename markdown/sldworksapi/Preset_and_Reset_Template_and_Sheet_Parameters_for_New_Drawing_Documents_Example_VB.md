---
title: "Preset and Reset Template and Sheet Parameters for New Drawing Documents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Preset_and_Reset_Template_and_Sheet_Parameters_for_New_Drawing_Documents_Example_VB.htm"
---

# Preset and Reset Template and Sheet Parameters for New Drawing Documents Example (VBA)

This example shows how to preset the template and sheet parameters for a new drawing document so that the Sheet Format/Size dialog is not displayed when opening a new drawing document. This example also shows how to reset the template and sheet parameters back to the defaults.

```
'------------------------------------------------------------
' Preconditions: Verify that the specified drawing document
' template exists.
'
' Postconditions:
' 1. Presets the drawing document template and sheet parameters so that
'    the Sheet Format/Size dialog is not displayed.
' 2. Click File > New > Drawing > OK to open a new drawing document
'    to verify step 1.
' 3. Press F5.
' 4. Resets the drawing template and sheet parameters so that
'    Sheet Format/Size dialog is displayed when opening a
'    new drawing document.
' 5. Open another new drawing document to verify step 4.
' 6. Close both drawings without saving them.
'------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Preset new drawing template and sheet parameters
    swApp.PresetNewDrawingParameters "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sheetformat\a - portrait.slddrt", True, 0, 0
```

```
    Stop
    ' Interactively open a new drawing document
    ' Sheet Format/Size dialog is not displayed
    ' Press F5
```

```
    ' Reset the drawing template and sheet parameters
    ' to display the Sheet Format/Size dialog the next
    ' time a drawing document is opened
```

```
    swApp.ResetPresetDrawingParameters
```

```
End Sub
```
