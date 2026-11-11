---
title: "Insert External Reference Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_External_Reference_Example_CSharp.htm"
---

# Insert External Reference Example (C#)

This example shows how to insert an external reference to a drawing document.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a new document.
// 6. If C:\Block.dwg exists, then skip this step.
//    - or -
//    If C:\Block.dwg does not exist, then construct
//    some geometry in the drawing, save the drawing
//    as C:\Block.dwg, and open a new drawing document.
// 7. Start debugging the project.
//
// Postconditions: Message boxes pop up when a Block Instance is
// inserted in the drawing document.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
static class Module1
{
    static void Main(string[] args)
    {
        DraftSight.Interop.dsAutomation.Application dsApp;
        Document dsDoc = default(Document);
        Model dsModel = default(Model);
        SketchManager dsSketchManager = default(SketchManager);
        BlockInstance dsExtReference = default(BlockInstance);
        ExternalReference dsReference = default(ExternalReference);
        string pathName;
        double insertX = 0;
        double insertY = 0;
        double insertZ = 0;
        double scaleValue = 0;
        double rotation = 0;
        //Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
        //Get active document
        dsDoc = dsApp.GetActiveDocument();
        if (dsDoc != null)
        {
            //Get model space
            dsModel = dsDoc.GetModel();
            //Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager();
            //External reference iparameters (rotation value should be in radians)
            pathName = "C:\\Block.dwg";
            insertX = 0.0;
            insertY = 0.0;
            insertZ = 0.0;
            scaleValue = 1.0;
            rotation = 0.0;
            //Add an external reference
            dsExtReference = dsSketchManager.InsertExternalReference(pathName, insertX, insertY, insertZ, scaleValue, rotation);
            if (dsExtReference != null)
            {
                MessageBox.Show("An external reference was added to the drawing.");
                object[] references = null;
                references = dsDoc.GetExternalReferences();
                dsReference = (ExternalReference)references[0];
                if (dsReference != null)
                {
                    MessageBox.Show("Name of external reference " + dsReference.Name + ".");
                }
            }
            else
            {
                MessageBox.Show(pathName + " file was not found.");
            }
        }
        else
        {
            MessageBox.Show("There are no open documents in DraftSight.");
        }
    }
}
```
