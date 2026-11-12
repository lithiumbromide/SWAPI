---
title: "Save as De-Featured File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_As_Defeatured_File_Example_VBNET.htm"
---

# Save as De-Featured File Example (VB.NET)

This example shows how to de-feature an assembly and save it as a part.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
' 2. Verify that c:\temp exists.
'
' Postconditions:
' 1. Saves the assembly as a de-featured part.
' 2. Open c:\temp\ball_valve.sldprt to verify.
'------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
```

```vb
Partial Class SolidWorksMacro
    Dim swModel As ModelDoc2
     Dim boolstatus As Boolean
    Sub main()
        swModel = swApp.ActiveDoc
         boolstatus = swModel.Extension.SaveDeFeaturedFile("c:\temp\ball_valve.sldprt")
    End Sub
    Public swApp As SldWorks
End Class
```
