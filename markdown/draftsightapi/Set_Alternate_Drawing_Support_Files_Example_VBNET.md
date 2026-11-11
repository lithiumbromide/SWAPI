---
title: "Set Alternate Drawing Support Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_Alternate_Drawing_Support_Files_Example_VBNET.htm"
---

# Set Alternate Drawing Support Files Example (VB.NET)

This example shows how to set alternate drawing support files.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Start DraftSight.
' 6. Press F5.
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

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()
        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        If dsApp Is Nothing Then
            Return
        End If

        'Abort any command currently running in DraftSight to avoid nested commands
        dsApp.b()

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Get drawing support files
        Dim dsDrawingSupportFiles As DrawingSupportFiles = dsApp.GetDrawingSupportFiles()
        If dsDrawingSupportFiles Is Nothing Then
            MessageBox.Show("There are no valid drawing support files.")
            Return
        End If

        Dim dsSysFile As SystemFiles = dsApp.GetSystemFiles()
        Dim FontsPathObj As Object() = DirectCast(dsSysFile.FontsPaths, Object())
        Dim fontPath As String = ""
        If FontsPathObj.Length > 0 Then
            fontPath = FontsPathObj(0).ToString()
        End If

        'Set alternate big font file
        Dim fontFileName As String = System.IO.Path.Combine(fontPath, "ARAGDTM.ttf")
        dsDrawingSupportFiles.AlternateBigFontFile = fontFileName
        MessageBox.Show("Alternate big font file: " + dsDrawingSupportFiles.AlternateBigFontFile)

        'Set alternate shape font file
        Dim shapeFileName As String = System.IO.Path.Combine(fontPath, "LTypeShp.shx")
        dsDrawingSupportFiles.AlternateShapeFile = shapeFileName
        MessageBox.Show("Alternate shape font file: " + dsDrawingSupportFiles.AlternateShapeFile)

        'Set alternate SHX font file
        Dim ShxFontFileName As String = System.IO.Path.Combine(fontPath, "LTypeShp.shx")
        dsDrawingSupportFiles.AlternateShxFontFile = ShxFontFileName
        MessageBox.Show("Alternate SHX font file: " + dsDrawingSupportFiles.AlternateShxFontFile)

        'Set alternate drawing template file
        Dim TemplateFilePath As String = System.IO.Path.Combine(dsApp.GetSystemFiles().GetUserDataPath(), "Template")

        Dim drawingTemplateFile As String = System.IO.Path.Combine(TemplateFilePath, "standard.dwt")
        dsDrawingSupportFiles.DrawingTemplateFilesPath = drawingTemplateFile
        MessageBox.Show("Alternate drawing template file: " + dsDrawingSupportFiles.DrawingTemplateFilesPath)

    End Sub

End Module
```
