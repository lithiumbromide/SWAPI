---
title: "Fire Notification When Inserting a Table in a Drawing Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Inserting_a_Table_in_a_Drawing_Document_Example_CSharp.htm"
---

# Fire Notification When Inserting a Table in a Drawing Document Example (C#)

This example shows how to fire a notification when a table is inserted in a drawing document.

```vb
 //---------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing document.
 // 2. Verify that the Tools > Options > System Options >
  //    Stop VSTA debugger on macro exit check box is not selected.
 // 3. Run this macro (press F5).
 // 4. Select a drawing view.
 // 5. Click Insert > Tables > Bill of Materials.
 // 6. Click OK in the Bill of Materials PropertyManager page.
 //
 // Postconditions:
 // 1. Displays a message box informing you that a table will be inserted.
 // 2. Click OK to close the message box.
  //    NOTE: Check the taskbar for the message box if you don't
 //    see it.
 // 3. Click to place the table.
 // 4. Stop the debugger.
 //---------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 using System.Collections;
 using System.Windows.Forms;
 namespace TableInsertNotification_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public DrawingDoc swDrawingDoc;

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);

             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Set up event
             swDrawingDoc = (DrawingDoc)swModel;

             AttachEventHandlers();
         }

         public void AttachEventHandlers()
         {
             AttachSWEvents();
         }

         public void AttachSWEvents()
         {
             swDrawingDoc.InsertTableNotify +=  this.swDrawingDoc_InsertTableNotify;
         }

         private int swDrawingDoc_InsertTableNotify(TableAnnotation TableAnnotation, string TableType, string TemplatePath)
         {
             MessageBox.Show("A table will be inserted. Title: " + TableAnnotation.Title + ", Type: " + TableType +  ", and Template path: " + TemplatePath);
             return 0;
         }

         public SldWorks swApp;

     }
 }
```
