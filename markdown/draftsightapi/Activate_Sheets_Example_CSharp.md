---
title: "Activate Sheets Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Activate_Sheets_Example_CSharp.htm"
---

# Activate Sheets Example (C#)

This example shows how to activate each Sheet in a drawing.

```
//--------------------------------------------------------------
//Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document with multiple Sheets.
// 6. Start debugging the project.
//
//Postconditions:
// 1. Pops up a message box when a Sheet is activated.
// 2. Click OK to close each message box.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Windows.Forms;
using System.Runtime.InteropServices;
static class Module1
{

    public static void Main()
    {
        DraftSight.Interop.dsAutomation.Application dsApp;
        Document dsDoc = default(Document);

        //Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

        //Abort any command currently running in
        //DraftSight to avoid nested commands
        dsApp.AbortRunningCommand();

        //Get active document
        dsDoc = dsApp.GetActiveDocument();
        if (dsDoc != null)
        {
            //Activate each Sheet, one by one
            SwitchSheets(dsDoc);
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
    public static void SwitchSheets(Document dsDoc)
    {
        Sheet dsSheet = default(Sheet);
        object[] dsVarSheets = null;
        int index = 0;
        string sheetName = null;
        //Get all Sheets
        dsVarSheets = (object[])dsDoc.GetSheets2();

        if (dsVarSheets != null)
        {
            for (index = dsVarSheets.GetLowerBound(0); index <= dsVarSheets.GetUpperBound(0); index++)
            {
                dsSheet = (Sheet)dsVarSheets[index];
                //Get Sheet name
                sheetName = dsSheet.Name;
                    //Activate Sheet
                    dsSheet.Activate();
                    //Verify if the Sheet was activated
                    if (dsSheet.IsActive())
                    {
                        MessageBox.Show(sheetName + " was activated.");
                    }
            }
        }

    }

}
```
