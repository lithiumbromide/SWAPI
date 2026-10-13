---
title: "Fire Notification When Changing a Table in a Drawing Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_a_Table_in_a_Drawing_Document_Example_CSharp.htm"
---

# Fire Notification When Changing a Table in a Drawing Document Example (C#)

This example shows how to fire a notification when a table is changed in a drawing document.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open a drawing document.
// 2. Verify that the Tools > Options > System Options >
//    Stop VSTA debugger on macro exit check box is not selected.
// 3. Select a drawing view and click Insert > Tables > Bill of Materials.
// 4. Click OK in the Bill of Materials PropertyManager page.
// 5. Run this macro (press F5).
// 6. Right-click a column in the table and select Delete > Column.
//
// Postconditions:
// 1. Displays a message box informing you that the table was modified.
//    NOTE: Check the taskbar for the message box if you don't
//    see it.
// 2. Click OK to close the message box.
// 3. Stop the debugger.
/---------------------------------------------------------------
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
			swDrawingDoc.ModifyTableNotify += this.swDrawingDoc_ModifyTableNotify;
		}

		private int swDrawingDoc_ModifyTableNotify(TableAnnotation TableAnnotation, int TableType, int reason, int RowInfo, int ColumnInfo, String DataInfo)
		{
			MessageBox.Show("A table was modified. Title: " + TableAnnotation.Title + ", Type: " + TableType + ", Reason code: " + reason 	+ ", RowInfo: " + RowInfo + ", ColumnInfo: " + ColumnInfo + ", DataInfo: " + DataInfo);
			return 0;
		}

		public SldWorks swApp;
	}
}
```
