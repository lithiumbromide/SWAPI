---
title: "Fire Notification When Inserting a Table in an Assembly Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_CSharp.htm"
---

# Fire Notification When Inserting a Table in an Assembly Document Example (C#)

This example shows how to fire a notification when a table is inserted in an assembly document.

//---------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document.
// 2. Verify that the **Tools > Options > System Options >**
// **Stop VSTA debugger on macro exit** check box is not selected.
// 3. Run this macro (press F5).
// 4. Click **Insert > Tables > Bill of Materials**.
// 5. Click **OK** in the Bill of Materials PropertyManager page and
// click **OK** again.
//
// Postconditions:
// 1. Displays a message box informing you that a table will be
// inserted in the assembly.
// NOTE: Check the taskbar for the message box if you don't
// see it.
// 2. Click **OK** to close the message box.
// 3. Click to place the table.
//---------------------------------------------------------------

```vb
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
             swAssemblyDoc.InsertTableNotify +=  this.swAssemblyDoc_InsertTableNotify;
         }

         private int  swAssemblyDoc_InsertTableNotify(TableAnnotation TableAnnotation, string TableType, string TemplatePath)
         {
             MessageBox.Show("A table will be inserted. Title: " + TableAnnotation.Title + ", Type: " + TableType + ", and Template path: " + TemplatePath);
             return 0;
         }

         public SldWorks swApp;

     }
 }
```
