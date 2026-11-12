---
title: "Fire Notification When Changing a Table in a Part Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_a_Table_in_a_Part_Document_Example_CSharp.htm"
---

# Fire Notification When Changing a Table in a Part Document Example (C#)

This example shows how to fire a notification when a table is changed in a part document.

```vb
 //---------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Verify that the Tools > Options > System Options >
 //    Stop VSTA debugger on macro exit check box is not selected.
 // 3. Click Insert > Tables > Bill of Materials.
 // 4. Click OK in the Bill of Materials PropertyManager page and
 //    click OK again.
 // 5. Run this macro (press F5).
 // 6. Right-click a column in the table and select Delete > Column.
 //
 // Postconditions:
 // 1. Displays a message box informing you that the table was modified.
 //    NOTE: Check the taskbar for the message box if it was not displayed.
 // 2. Click OK to close the message box.
 // 3. Stop the debugger.
 //---------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 using System.Collections;
 using System.Windows.Forms;
 namespace ModifyTableNotification_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public PartDoc swPartDoc;

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);

             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Set up event
             swPartDoc = (PartDoc)swModel;
             AttachEventHandlers();
         }

         public void AttachEventHandlers()
         {
             AttachSWEvents();
         }

         public void AttachSWEvents()
         {
             swPartDoc.ModifyTableNotify +=  this.swPartDoc_ModifyTableNotify;
         }

         private int swPartDoc_ModifyTableNotify(TableAnnotation TableAnnotation, int TableType, int reason, int RowInfo, int ColumnInfo, String DataInfo)
         {
             MessageBox.Show("A table was modified. Title: " + TableAnnotation.Title +  ", Type: " + TableType + ", Reason code: " + reason +  ", RowInfo: " + RowInfo + ", ColumnInfo: " + ColumnInfo + ", DataInfo: " + DataInfo);
             return 0;
         }

         public SldWorks swApp;

     }
 }
```
