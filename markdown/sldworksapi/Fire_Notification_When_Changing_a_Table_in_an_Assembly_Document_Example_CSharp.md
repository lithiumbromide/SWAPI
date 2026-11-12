---
title: "Fire Notification When Changing a Table in an Assembly Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_CSharp.htm"
---

# Fire Notification When Changing a Table in an Assembly Document Example (C#)

This example shows how to fire a notification when a table is changed in an assembly document.

```vb
 //---------------------------------------------------------------
 // Preconditions:
 // 1. Open an assembly document.
 // 2. Verify that the Tools > Options > System Options >
  //    Stop VSTA debugger on macro exit check box is not selected.
 // 3. Click Insert > Tables > Bill of Materials.
 // 4. Click OK in the Bill of Materials PropertyManager page and
 //    click OK again.
 // 5. Run this macro (press F5).
 // 6. Right-click on a column in the table and select Delete > Column.
 //
 // Postconditions:
 // 1. Displays a message box informing you that the table was modified.
 //    NOTE: Check the taskbar for the message box if you don't
 //    see it.
 // 2. Click OK to close the message box.
 // 3. Stop the debugger..
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

         public AssemblyDoc swAssemblyDoc;

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             Hashtable openAssem = default(Hashtable);

             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Set up event
             swAssemblyDoc = (AssemblyDoc)swModel;
             openAssem = new Hashtable();

             AttachEventHandlers();
         }

         public void AttachEventHandlers()
         {
             AttachSWEvents();
         }

         public void AttachSWEvents()
         {
             swAssemblyDoc.ModifyTableNotify +=  this.swAssemblyDoc_ModifyTableNotify;
         }

         private int swAssemblyDoc_ModifyTableNotify(TableAnnotation TableAnnotation, int TableType, int reason, int RowInfo, int ColumnInfo, String DataInfo)
         {
             MessageBox.Show("A table was modified. Title: " + TableAnnotation.Title + ", Type: " + TableType +  ", Reason code: " + reason + ", RowInfo: " + RowInfo + ", ColumnInfo: " + ColumnInfo + ", DataInfo: " + DataInfo);
             return 0;
         }

         public SldWorks swApp;

     }
 }
```
