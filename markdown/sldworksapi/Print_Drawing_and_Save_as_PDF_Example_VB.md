---
title: "Print Drawing and Save as PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Print_Drawing_and_Save_as_PDF_Example_VB.htm"
---

# Print Drawing and Save as PDF Example (VBA)

This example shows how to print a drawing document to your default printer and save it as a PDF file.

```
'---------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
' 2. Verify that C:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of your default printer.
' 2. Sets the page orientation to landscape.
' 3. Prints 2012-sm.slddrw to your default printer.
' 4. Saves 2012-sm.slddrw as C:\temp\2012-sm.pdf.
' 5. Examine the Immediate window, your default printer,
'    and C:\temp.
'---------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Model As ModelDoc2
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Model = swApp.ActiveDoc
    Debug.Print Model.Printer
```

```
    Dim ps As PageSetup
    Set ps = Model.PageSetup
    ps.Orientation = 2   ' 1=Portrait  '2 = Landscape
```

```
    Dim pageArray(3) As Long
    pageArray(0) = 1
    pageArray(1) = 1
    pageArray(2) = 3
    pageArray(3) = 3
```

```
    Dim vPageArray As Variant
    vPageArray = pageArray
```

```
    Dim copies As Long
    copies = 1
    Dim collate As Boolean
    collate = True
```

```
    ' Print to default printer
    Model.Extension.PrintOut2 vPageArray, copies, collate, "", ""
```

```
    Dim e As Long
    Dim w As Long
```

```
    ' Save to PDF
    Debug.Print Model.SaveAs4("C:\temp\2012-sm.pdf", 0, 0, e, w)
```

```
End Sub
```
