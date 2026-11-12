---
title: "Set Alternate Drawing Support Files Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_Alternate_Drawing_Support_Files_Example_VBA.htm"
---

# Set Alternate Drawing Support Files Example (VBA)

This example shows how to set alternate drawing support files.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Press F5
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets active document.
' 3. Gets instance of drawing support files.
' 4. Displays message boxes informing you that these alternate
'    font files were set:
'    a. Big font file. Click OK.
'    b. Shape font file. Click OK.
'    c. SHX font file. Click OK.
'    d. Drawing template file. Click OK.
' 5. Click Tools > Options > File Locations and expand Drawing Support.
'    a. Expand and examine Alternate Font File > SHX font, Big font,
'       and Shape file.
'    b. Expand and examine Drawing Template File Location.
' 6. Exit DraftSight.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
```

```
    'Get drawing support files
    Dim dsDrawingSupportFiles As DraftSight.DrawingSupportFiles
    Set dsDrawingSupportFiles = dsApp.GetDrawingSupportFiles
```

```
    Dim dsSysFile As DraftSight.SystemFiles
    Set dsSysFile = dsApp.GetSystemFiles
    Dim FontsPathObj As Variant
    FontsPathObj = dsSysFile.FontsPaths
    Dim fontPath As String
    If Not IsArray(FontsPathObj) Then
        MsgBox "No system files."
        Exit Sub
    Else
        fontPath = CStr(FontsPathObj(0))
    End If
```

```
    'Set alternate big font file
    Dim fontFileName As String
    fontFileName = fontPath & "ARGothE.ttf"
    dsDrawingSupportFiles.AlternateBigFontFile = fontFileName
    MsgBox "Alternate big font file: " & dsDrawingSupportFiles.AlternateBigFontFile
```

```
    'Set alternate shape font file
    Dim shapeFileName As String
    shapeFileName = fontPath & "FC-Iso.shx"
    dsDrawingSupportFiles.AlternateShapeFile = shapeFileName
    MsgBox "Alternate shape font file: " & dsDrawingSupportFiles.AlternateShapeFile
```

```
    'Set alternate SHX font file
    Dim shxFontFileName As String
    shxFontFileName = fontPath & "FC-Iso.shx"
    dsDrawingSupportFiles.AlternateShxFontFile = shxFontFileName
    MsgBox "Alternate SHX font file: " & dsDrawingSupportFiles.AlternateShxFontFile
```

```
    'Set alternate drawing template file
    Dim templateFilePath As String
    templateFilePath = dsApp.GetSystemFiles.GetUserDataPath
    Dim drawingTemplateFilePath As String
    drawingTemplateFilePath = templateFilePath + "Template\standarddin.dwt"
    dsDrawingSupportFiles.DrawingTemplateFilesPath = drawingTemplateFilePath
    MsgBox "Alternate drawing template file: " & dsDrawingSupportFiles.DrawingTemplateFilesPath
```

```
End Sub
```
