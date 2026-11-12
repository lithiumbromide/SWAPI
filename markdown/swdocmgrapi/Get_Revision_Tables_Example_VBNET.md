---
title: "Get Revision Tables Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Revision_Tables_Example_VBNET.htm"
---

# Get Revision Tables Example (VB.NET)

This example shows how to get a revision table in a drawing document, add a revision row, get revision row information, and update the revision row and column data.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Read the SOLIDWORKS Document Manager API
 '    Getting Started topic and ensure that the
 '    required DLLs are registered.
 ' 2. Copy and paste this module into a VB.NET
 '    console application in Microsoft Visual Studio.
 ' 3.  Add the SolidWorks.Interop.swdocumentmgr.dll
 '    reference to the project.
 ' 4. Substitute your license key for your_license_key in the code.
 ' 5. Ensure the specified document exists.
  ' 6. Compile and run this program in Debug mode.
 '
 ' Postconditions:
 ' 1. Adds a revision row.
 ' 2. Prints to the Immediate window:
 '    * Path and filename
 '    * Last saved date
 '    * For each revision table:
 '      * Name
 '      * Sheet name
 '      * Latest revision
 '      * Revision information
 '      * Revision table style
 '      * Whether a placeholder row exists
 ' 3. Updates the latest revision column data.
 ' 4. Updates the latest revision row data.
 '
 ' NOTE: Do not save changes to the document, as it is used elsewhere.
  '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr
 Imports System
 Imports System.Diagnostics

 Module Module1

     Dim dmClassFact As SwDMClassFactory
     Dim dmDocMgr As SwDMApplication3
     Dim dmDoc As ISwDMDocumen15
     Dim dmTable As ISwDMTable5
     Dim dmSheet As ISwDMSheet4
     Dim custPropView As ISwDMView
     Dim dmError As SwDmDocumentOpenError
     Dim arrviews As Array
     Dim nameDrawing As String

     Sub Main()

         dmClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         dmDocMgr = dmClassFact.GetApplication("your_license_key") 'Do not distribute
         nameDrawing = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\advdrawings\foodprocessor.slddrw"

         'Get the SOLIDWORKS drawing document
         dmDoc = dmDocMgr.GetDocument(nameDrawing, SwDmDocumentType.swDmDocumentDrawing, False, dmError)
         Debug.Print("Document's full name: " & dmDoc.FullName)
         Debug.Print("Date document last saved: " & dmDoc.LastSavedDate)

         'Get the names of the revision tables in the document
         Dim tableNames As Object
         tableNames = dmDoc.GetTableNames(SwDmTableType.swDmTableTypeRevision)
         Dim i As Integer
         If Not IsNothing(tableNames) Then
             For i = 0 To UBound(tableNames)
                 dmTable = dmDoc.GetTable(tableNames(i))
                 Debug.Print(" Revision table name: " & dmTable.Name)

                 dmSheet = dmTable.Sheet
                 If Not IsNothing(dmSheet) Then

                     Debug.Print("   On sheet: " & dmSheet.Name)

                 End If
             Next
         End If
     End Sub
 End Module
```
