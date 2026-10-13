---
title: "Get Table Cell Text Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Table_Cell_Text_Example_VBNET.htm"
---

# Get Table Cell Text Example (VB.NET)

This example shows how to get all of the cell text from a BOM table using the SOLIDWORKS Document Manager API.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API Help
'    Getting Started topic and ensure that the
'    required DLLs are registered.
' 2. Open SOLIDWORKS and copy the code below to a VB.NET macro.
' 3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
'    interop assembly is loaded in the project.
'    (Right-click on the project in Project Explorer, click
'    Add Reference,  click the interop assembly in the .NET
'    tab, or browse for the DLL in install_dir\api\redist.)
' 4. In SOLIDWORKS, create a part document with a BOM table.
' 5. Save the part and close it.
' 6. Substitute your license key for your_license_key in the code.
' 7. Substitute the new file name for sFile in the code.
' 8. Uncomment the appropriate swDoc line.
'
' Postconditions: The Immediate Window displays the BOM
' table row and column count and all of the table's cell
' text in row order.
'--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdocumentmgr
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Dim classfac As SwDMClassFactory
    Dim tapp As SwDMApplication
    Dim swDoc As SwDMDocument13
    Dim swTable As SwDMTable3
    Dim e As SwDmDocumentOpenError
    Dim sFile As String
    Dim vTables As Object
    Dim vTabArr As Object
    Dim err As SwDmTableError
    Dim row As Integer, col As Integer
    Dim i As Integer, j As Integer
    Sub Main()
        classfac = CreateObject("SwDocumentMgr.SwDMClassFactory")
        tapp = classfac.GetApplication("your_license_key") 'license needed please do not distribute this
        sFile = "C:\temp\Part1.SLDPRT"

        'get the SW document file
swDoc = tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentPart, False, e)
        'Set swDoc = tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentAssembly, False, e)
        'Set swDoc = tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentDrawing, False, e)

        Debug.Print("Doc Version is " & swDoc.GetVersion)
        Debug.Print("Doc name is " & swDoc.FullName)
        vTables = swDoc.GetTableNames(SwDmTableType.swDmTableTypeBOM)
        If Not IsNothing(vTables) Then
            swTable = swDoc.GetTable(vTables(0))
            If Not swTable Is Nothing Then
                Debug.Print("Table retrieved is " & vTables(0))
                vTabArr = swTable.GetTableCellText(err, row, col)
                Debug.Print("Row count is " & row)
                Debug.Print("Column count is " & col)
                Debug.Print("Table cell text:")
                For j = 0 To UBound(vTabArr)
                    Debug.Print("   " & vTabArr(j))
                Next
            End If
        End If
        swDoc.CloseDoc()
    End Sub

    Public swApp As SldWorks
End Class
```
