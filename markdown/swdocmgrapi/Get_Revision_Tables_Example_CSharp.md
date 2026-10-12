---
title: "Get Revision Tables Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Revision_Tables_Example_CSharp.htm"
---

# Get Revision Tables Example (C#)

This example shows how to get a revision table in a drawing document, add a revision row, get revision row information, and update the revision row and column data.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
  // 1. Read the SOLIDWORKS Document Manager API
 //    Getting Started topic and ensure that
 //    the required DLLs have been registered.
 // 2. Copy and paste this module into a C#
 //    console application in Microsoft Visual Studio.
 // 3. Add the SolidWorks.Interop.swdocumentmgr.dll
 //    reference to the project.
 // 4. Substitute your_license_code with your SOLIDWORKS
 //    Document Manager license key.
 // 5. Ensure the specified document exists.
 // 6. Compile and run this program in Debug mode.
 //
 // Postconditions:
 // 1. Prints to the Immediate window:
 //    * Path and filename
 //    * Last saved date
 //    * For each revision table:
 //      * Name
 //      * Sheet name
 //      * Latest revision
 //      * Revision information
 //      * Revision table style
 //      * Whether a placeholder row exists
 // 2. In the revision table of sheet 1:
 //    a. Adds a revision row.
 //    b. Updates the revision column data.
 //    c. Updates the revision row data.
 //
 // NOTE: Do not save changes to the document, as it is used elsewhere.
 //---------------------------------------------------------------------------

 using SolidWorks.Interop.swdocumentmgr;
 using System;
 using System.Diagnostics;

 namespace ConsoleApplication2
 {
     class Module1
     {
         static void Main()
         {
             SwDMClassFactory dmClassFact = default(SwDMClassFactory);
             SwDMApplication3 dmDocMgr = default(SwDMApplication3);
             ISwDMDocument15 dmDoc = default(ISwDMDocument15);
             ISwDMTable6 dmTable = default(ISwDMTable6);
             ISwDMSheet4 dmSheet = default(ISwDMSheet4);
             SwDmDocumentOpenError dmError = default(SwDmDocumentOpenError);
             string nameDrawing = "";

             dmClassFact = new SwDMClassFactory();
             dmDocMgr = (SwDMApplication3)dmClassFact.GetApplication("your_license_key"); //Do not distribute
             nameDrawing = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\advdrawings\\foodprocessor.slddrw";

             //Get the SOLIDWORKS drawing document
             dmDoc = (ISwDMDocument15)dmDocMgr.GetDocument(nameDrawing, SwDmDocumentType.swDmDocumentDrawing, false, out dmError);
             Debug.Print("Document's full name: " + dmDoc.FullName);
             Debug.Print("Date document last saved: " + dmDoc.LastSavedDate);

             //Get the names of the revision tables in the document
             string[] tableNames = null;
             tableNames = (string[])dmDoc.GetTableNames(SwDmTableType.swDmTableTypeRevision);
             int i = 0;
             if ((tableNames != null))
             {
                 for (i = 0; i <= tableNames.Length - 1; i++)
                 {
                     dmTable = (SwDMTable6)dmDoc.GetTable(tableNames[i]);
                     Debug.Print(" Revision table name: " + dmTable.Name);

                     dmSheet = (SwDMSheet4)dmTable.Sheet;
                     if (dmSheet != null)
                     {
                         Debug.Print("   On sheet: " + dmSheet.Name);
                     }

                 }
             }
         }
     }
 }
```
