---
title: "Print Drawing Document to File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Print_Drawing_Document_to_File_Example_VB.htm"
---

# Print Drawing Document to File Example (VBA)

This example shows how to print a drawing document to a print file.

```
'---------------------------------------------
' Preconditions:
' 1. Copy public_documents\samples\tutorial\api\2012-sm.slddrw
'    and 2012-sm.sldprt to C:\temp.
' 2. Open C:\temp\2012-sm.slddrw.
' 3. Substitute the name of your printer for GoToMyPc.
'
' Postconditions:
' 1. Prints 2012-sm0.prn to C:\temp.
' 2. Examine C:\temp.
'---------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    ' Printer
    Const SWPrinter As String = "GoToMyPC"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDocExt As SldWorks.ModelDocExtension
    Dim swDraw As SldWorks.DrawingDoc
    Dim PathName As String
    Dim PrintFileName As String
    Dim nPrintSheets(1) As Long
    Dim vPrintSheets As Variant
    Dim DefPrinter As String
    Dim i  As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDocExt = swModel.Extension
    Set swDraw = swModel
```

```
    ' Strip off SOLIDWORKS Design file extension
    PathName = swModel.GetPathName
    PathName = Left(PathName, Len(PathName) - 7)
```

```
    For i = 0 To swDraw.GetSheetCount - 1
        ' Generate print file name based on number of sheets
        ' For example, because 2012-sm.slddrw contains
        ' one sheet, then the print file name is 2012-sm0.prn
        PrintFileName = PathName & Trim(Str(i)) & ".prn"
```

```
        ' Print out one sheet at a time
        nPrintSheets(0) = i + 1
        vPrintSheets = nPrintSheets
        swDocExt.PrintOut2 (vPrintSheets), 1, False, SWPrinter, PrintFileName
    Next i
```

```
End Sub
```
