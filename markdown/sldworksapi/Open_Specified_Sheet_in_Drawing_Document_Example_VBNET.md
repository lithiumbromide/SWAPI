---
title: "Open Specified Sheet in Drawing Document Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Specified_Sheet_in_Drawing_Document_Example_VBNET.htm"
---

# Open Specified Sheet in Drawing Document Example (VB.NET)

This example shows how to open a specific sheet when programmatically opening a drawing document.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified sheet in the specified drawing
'    document as view-only.
' 2. Examine the drawing and Immediate window.
'
' NOTE: Because this drawing document is used
' elsewhere, do not save changes.
'------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```
Partial Class SolidWorksMacro
```

```
    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swDocSpecification As DocumentSpecification
        Dim sName As String
        Dim longstatus As Long, longwarnings As Long
```

```
        ' Drawing document path and name
        swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw")
        sName = swDocSpecification.FileName
        ' Sheet name
        swDocSpecification.SheetName = "Sheet2"
        swDocSpecification.DocumentType = swDocumentTypes_e.swDocDRAWING
        swDocSpecification.ReadOnly = True
        swDocSpecification.Silent = False
```

```
        ' Open the specified sheet in the specified drawing document
        swModel = swApp.OpenDoc7(swDocSpecification)
        longstatus = swDocSpecification.Error
        longwarnings = swDocSpecification.Warning
```

```
        Debug.Print("Name of active sheet? " & swDocSpecification.SheetName)
        Debug.Print("Drawing read-only? " & swDocSpecification.ReadOnly)
```

```
    End Sub
```

```
    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
```

```
End Class
```
