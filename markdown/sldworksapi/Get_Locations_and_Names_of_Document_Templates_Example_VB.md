---
title: "Get Locations and Names of Document Templates Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Locations_and_Names_of_Document_Templates_Example_VB.htm"
---

# Get Locations and Names of Document Templates Example (VBA)

This example shows how to get the locations and names of SOLIDWORKS Design document templates.

```vb
'------------------------------------------------
 ' Preconditions: Open the Immediate window.
 ' Postconditions: Examine the Immediate window.
 '------------------------------------------------
Option Explicit
Sub main()
    Dim swApp As SldWorks.SldWorks
     Set swApp = Application.SldWorks

    Debug.Print "FileLocationsDocumentTemplates = " & swApp.GetUserPreferenceStringValue(swFileLocationsDocumentTemplates)
     Debug.Print "FileLocationsSheetFormat       = " & swApp.GetUserPreferenceStringValue(swFileLocationsSheetFormat)
     Debug.Print "DefaultTemplatePart            = " & swApp.GetUserPreferenceStringValue(swDefaultTemplatePart)
     Debug.Print "DefaultTemplateAssembly        = " & swApp.GetUserPreferenceStringValue(swDefaultTemplateAssembly)
     Debug.Print "DefaultTemplateDrawing         = " & swApp.GetUserPreferenceStringValue(swDefaultTemplateDrawing)
     Debug.Print ""

     Debug.Print "Draw template = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperAsize, 0#, 0#)
     Debug.Print "Part template = " & swApp.GetDocumentTemplate(swDocPART, "", 0, 0#, 0#)
     Debug.Print "Assy template = " & swApp.GetDocumentTemplate(swDocASSEMBLY, "", 0, 0#, 0#)
     Debug.Print ""

     Debug.Print "Draw templates:"
     Debug.Print "  A        = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperAsize, 0#, 0#)
     Debug.Print "  A vert   = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperAsizeVertical, 0#, 0#)
     Debug.Print "  B        = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperBsize, 0#, 0#)
     Debug.Print "  C        = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperCsize, 0#, 0#)
     Debug.Print "  D        = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperDsize, 0#, 0#)
     Debug.Print "  E        = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperEsize, 0#, 0#)
     Debug.Print "  A4       = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperA4size, 0#, 0#)
     Debug.Print "  A4 vert  = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperA4sizeVertical, 0#, 0#)
     Debug.Print "  A3       = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperA3size, 0#, 0#)
     Debug.Print "  A2       = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperA2size, 0#, 0#)
     Debug.Print "  A1       = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperA1size, 0#, 0#)
     Debug.Print "  A0       = " & swApp.GetDocumentTemplate(swDocDRAWING, "", swDwgPaperA0size, 0#, 0#)

End Sub
```
