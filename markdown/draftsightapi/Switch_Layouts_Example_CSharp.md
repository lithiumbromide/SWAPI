---
title: "Switch Layouts Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Switch_Layouts_Example_CSharp.htm"
---

# Switch Layouts Example (C#)

This example shows how to switch layouts.

```
//--------------------------------------------------------------
//Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Start debugging the project.
//
//Postconditions: Message boxes pop up when a model or sheet
//is activated. Read the text in each message box before clicking
//OK to close it.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Windows.Forms;
using System.Runtime.InteropServices;
```

```
static class Module1
{
```

```
    public static void Main()
	{
```

```
        	DraftSight.Interop.dsAutomation.Application dsApp;
		Document dsDoc = default(Document);
```

```
		//Connect to DraftSight
```

```
      dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
      dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
		//Get active document
		dsDoc = dsApp.GetActiveDocument();
```

```
		if (dsDoc != null)
                {
			//Activate each layout, one by one
			SwitchLayouts(dsDoc);
```

```
		}
                else
                {
			MessageBox.Show("There are no open documents in DraftSight.");
		}
	}
    public static void SwitchLayouts(Document dsDoc)
    {
        Sheet dsSheet = default(Sheet);
        Model dsModel = default(Model);
        object[] dsVarSheets = null;
        int index = 0;
        string sheetName = null;
```

```
        //Get all sheets
        dsVarSheets = (object[])dsDoc.GetSheets();
```

```
        if (dsVarSheets != null)
        {
```

```
            for (index = dsVarSheets.GetLowerBound(0); index <= dsVarSheets.GetUpperBound(0); index++)
            {
                dsSheet = (Sheet)dsVarSheets[index];
```

```
                //Get sheet name
                sheetName = dsSheet.Name;
```

```
                //Change sheet name, if it is not a model
```

```
                if (sheetName != "Model")
                {
                    //Activate sheet
                    dsSheet.Activate();
```

```
                    //Verify if the sheet was activated
                    if (dsSheet.IsActive())
                    {
                        MessageBox.Show("The sheet " + sheetName + " was activated.");
                    }
```

```
                }
                else
                {
                    //Activate model sheet
                    dsModel = (Model)dsDoc.GetModel();
```

```
                    if (dsModel != null)
                    {
                        //Activate model sheet
                        dsModel.Activate();
```

```
                        //Verify if the sheet was activated
                        if (dsModel.IsActive())
                        {
                            MessageBox.Show("The model sheet was activated.");
                        }
```

```
                    }
```

```
                }
```

```
            }
```

```
        }
```

```
    }
```

```
}
```
