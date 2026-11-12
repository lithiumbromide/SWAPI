---
title: "Set and Get System Files Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_and_Get_System_Files_Example_VBA.htm"
---

# Set and Get System Files Example (VBA)

This example shows how to set and get the paths of some DraftSight system files.

```vb
'----------------------------------------------------------------------------
 'Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '     install_dir\bin\dsAutomation.dll.
 ' 4. Start DraftSight.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Sets the paths to the DraftSight font and support files.
 ' 2. Prints the current DraftSight system files and paths to the
 '    Immediate window.
 '----------------------------------------------------------------------------
Option Explicit

Sub main()
     Dim dsApp As DraftSight.Application
     Dim dsSystemFiles As DraftSight.SystemFiles
     Dim setFontPaths(1) As String
     Dim setSupportPaths(2) As String
     Dim getFontPaths As Variant
     Dim getSupportPaths As Variant
     Dim getDrawingBorderPaths As Variant
     Dim getTitleBlockPaths As Variant
     Dim i As Long
     Dim arraySizeFonts As Long
     Dim arraySizeSupport As Long
     'Connect to DraftSight
     Set dsApp = GetObject(, "DraftSight.Application")
     'Abort any command currently running in DraftSight
     'to avoid nested commands
     dsApp.AbortRunningCommand
     'Get system files interface
     Set dsSystemFiles = dsApp.GetSystemFiles
     'Set system files paths
     setFontPaths(0) = "C:\Program Files\Dassault Systemes\DraftSight\Fonts"
     arraySizeFonts = UBound(setFontPaths)
     dsSystemFiles.FontsPaths = setFontPaths
     setSupportPaths(0) = "C:\Program Files\Dassault Systemes\DraftSight\Default Files\Support"
     arraySizeSupport = UBound(setSupportPaths)
     dsSystemFiles.SupportPaths = setSupportPaths
     'Get system file paths and file names
     Debug.Print "System files:"
     Debug.Print "  Help file:                            " & dsSystemFiles.HelpFile
     Debug.Print "  Logfile path:                         " & dsSystemFiles.LogFilePath
     Debug.Print "  Dictionary file for SpellCheck:       " & dsSystemFiles.MainDictionaryFile
     Debug.Print "  Custom dictionary file:               " & dsSystemFiles.CustomDictionaryFile
     Debug.Print "  Location for temporary drawing files: " & dsSystemFiles.TempPath

     getFontPaths = dsSystemFiles.FontsPaths
     Debug.Print "  Font paths: "
     For i = 0 To arraySizeFonts
         Debug.Print ("                                        " & getFontPaths(i))
     Next i
     getSupportPaths = dsSystemFiles.SupportPaths
     Debug.Print "  Support paths: "
     For i = 0 To arraySizeSupport
         Debug.Print ("                                        " & getSupportPaths(i))
     Next i

    getDrawingBorderPaths = dsSystemFiles.DrawingBorderPaths
     Debug.Print "  Drawing border paths: "
     For i = 0 To UBound(getDrawingBorderPaths)
         Debug.Print ("                                        " & getDrawingBorderPaths(i))
     Next i

    getTitleBlockPaths = dsSystemFiles.TitleBlockPaths
     Debug.Print "  Title block paths: "
     For i = 0 To UBound(getTitleBlockPaths)
         Debug.Print ("                                        " & getTitleBlockPaths(i))
     Next i

End Sub
```
