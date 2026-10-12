---
title: "Get IDs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Persistent_IDs_Example_VBNET.htm"
---

# Get IDs Example (VB.NET)

## Get Sheet IDs Example (VB.NET)

This example shows how to get the IDs of drawing sheets.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API
 '    Help Getting Started topic and ensure that
 '    the required DLLs are registered.
 ' 2. Open SOLIDWORKS and copy the code below to a VB.NET macro.
 ' 3. Convert the drawing document specified
 '    in sDocFileName to the latest supported
 '    version by opening and saving it to another name
 '    in SOLIDWORKS.
 '
 '    NOTE:  Because this document is used elsewhere, do not
 '    save any changes when closing it.
 '
 ' 4. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 '    interop assembly is loaded in the project. (Right-click
 '    the project in Project Explorer, click Add Reference,
 '    click the interop assembly in the .NET tab, or browse
 '    for the DLL in install_dir\api\redist.)
 ' 5. Substitute your license key for your_license_key in the code.
 '
 ' Postconditions: Inspect the Immediate Window for the sheet IDs.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdocumentmgr
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Sub main()
        Dim swClassFact As SwDMClassFactory
        Dim swDocMgr As SwDMApplication
        Dim swDoc As SwDMDocument14
        Dim sDocFileName As String
        Dim nDocType As SwDmDocumentType
        Dim nRetVal As SwDmDocumentOpenError
        Dim sLicenseKey As String

        ' Specify your license key
        sLicenseKey = "your_license_key"

        ' If this drawing document doesn't exist on your system,
        ' then substitute the name of drawing document that does
        sDocFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        nDocType = SwDmDocumentType.swDmDocumentDrawing
        swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
        swDocMgr = swClassFact.GetApplication(sLicenseKey)
        swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)
        If (swDoc Is Nothing) Then
            MsgBox("Unable to open document. Correct path to file or register Document Manager DLL.")
        End If
        Dim Sheet As SwDMSheet3
        Dim Sheets As Object
        Dim i As Integer
        Sheets = swDoc.GetSheets
        For i = 0 To UBound(Sheets)
            Sheet = Sheets(i)
            Debug.Print(Sheet.Name & " ID: " & Sheet.GetID)
        Next
        swDoc.CloseDoc()
    End Sub
    Public swApp As SldWorks
End Class
```
