---
title: "Set and Get System Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_and_Get_System_Files_Example_VBNET.htm"
---

# Set and Get System Files Example (VB.NET)

This example shows how to set and get the paths of some DraftSight system files.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
 ' 4. Start DraftSight.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Sets the paths to the DraftSight support and font files.
 ' 2. Prints the current DraftSight system files and paths to the
 '    Immediate window.
 '---------------------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation

 Module Module1

     Sub Main()

         Dim dsApp As Application
         Dim dsSystemFiles As SystemFiles
         Dim setFontPaths(1) As String
         Dim setSupportPaths(2) As String
         Dim getFontPaths As Object
         Dim getSupportPaths As Object
         Dim getDrawingBorderPaths As Object
         Dim getTitleBlockPaths As Object

         Dim i As Integer
         Dim arraySizeFonts As Long
         Dim arraySizeSupport As Long

         'Connect to DraftSight
         dsApp = GetObject(, "DraftSight.Application")

         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand()

         'Get system files
         dsSystemFiles = dsApp.GetSystemFiles

         'Set system files
         setFontPaths(0) = "C:\Program Files\Dassault Systemes\DraftSight\Fonts"
         arraySizeFonts = UBound(setFontPaths)
         dsSystemFiles.FontsPaths = setFontPaths

         setSupportPaths(0) = "C:\Program Files\Dassault Systemes\DraftSight\Default Files\Support"
         arraySizeSupport = UBound(setSupportPaths)
         dsSystemFiles.supportPaths = setSupportPaths

         Debug.Print("System files:")
         Debug.Print("  Help file:                            " & dsSystemFiles.HelpFile)
         Debug.Print("  Logfile path:                         " & dsSystemFiles.LogFilePath)
         Debug.Print("  Dictionary file for SpellCheck:       " & dsSystemFiles.MainDictionaryFile)
         Debug.Print("  Custom dictionary file:               " & dsSystemFiles.CustomDictionaryFile)
         Debug.Print("  Location for temporary drawing files: " & dsSystemFiles.TempPath)

         getFontPaths = dsSystemFiles.FontsPaths
         Debug.Print("  Font paths: ")
         For i = 0 To arraySizeFonts
             Debug.Print("                                        " & getFontPaths(i))
         Next i

         getSupportPaths = dsSystemFiles.supportPaths
         Debug.Print("  Support paths: ")
         For i = 0 To arraySizeSupport
             Debug.Print("                                        " & getSupportPaths(i))
         Next i
        getDrawingBorderPaths = dsSystemFiles.DrawingBorderPaths
         Debug.Print("  Drawing border paths: ")
         For i = 0 To UBound(getDrawingBorderPaths)
             Debug.Print("                                        " & getDrawingBorderPaths(i))
         Next i

         getTitleBlockPaths = dsSystemFiles.TitleBlockPaths
         Debug.Print("  Title block paths: ")
         For i = 0 To UBound(getTitleBlockPaths)
             Debug.Print("                                        " & getTitleBlockPaths(i))
         Next i

     End Sub

 End Module
```
