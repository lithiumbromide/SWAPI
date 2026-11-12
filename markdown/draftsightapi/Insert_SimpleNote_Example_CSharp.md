---
title: "Insert SimpleNote Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_SimpleNote_Example_CSharp.htm"
---

# Insert SimpleNote Example (C#)

This example shows how to insert and change a SimpleNote in a drawing document.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System, System.Runtime.InteropServices,
//    and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Start debugging the project.
//
// Postconditions:
// 1. A message box pops up when a SimpleNote is
//    inserted in the drawing.
// 2. The selection filter is set to select SimpleNotes only and
//    is activated.
// 3. The SimpleNote is selected and its text changed. Examine
//    the drawing to verify.
//----------------------------------------------------------------
```

```
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
```

```
static class Module1
{
    public static void Main()
	{
	DraftSight.Interop.dsAutomation.Application dsApp;
```

```
	Document dsDoc = default(Document);
	Model dsModel = default(Model);
	SketchManager dsSketchManager = default(SketchManager);
	SimpleNote dsSimpleNote = default(SimpleNote);
	double startX = 0;
	double startY = 0;
	double startZ = 0;
        string noteValue;
        double angle = 0;
        double height;
```

```
	//Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
	dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

	//Get active document
	dsDoc = dsApp.GetActiveDocument();
	if ((dsDoc != null)) {
		//Get model space
		dsModel = dsDoc.GetModel();
```

```
		//Get Sketch Manager
		dsSketchManager = dsModel.GetSketchManager();
```

```
        	//SimpleNote parameters (angle value should be passed in radians)
        	startX = 0.0;
        	startY = 0.0;
        	startZ = 0.0;
        	noteValue = "Sample text";
        	height = 1.0;
        	angle = Math.PI / 4; //45 degrees in radians
```

```
        	//Add a SimpleNote
        	dsSimpleNote = dsSketchManager.InsertSimpleNote(startX, startY, startZ, height, angle, noteValue);
		if ((dsSimpleNote != null)) {
			MessageBox.Show("A SimpleNote was inserted in the drawing.");
			}
			} else {
				MessageBox.Show("There are no open documents in DraftSight.");
			}
```

```
        	//Change SimpleNote text
       	 	ChangeSimpleNotesText(dsDoc, dsSketchManager);
```

```
	}
    private static void ChangeSimpleNotesText(Document dsDoc, SketchManager dsSketchManager)
        {
            //Get Selection Manager
            SelectionManager dsSelectionMgr = dsDoc.GetSelectionManager();
```

```
            //Get selection filter
            SelectionFilter dsSelectioFilter = dsSelectionMgr.GetSelectionFilter();
```

```
            //Clear selection filter
            dsSelectioFilter.Clear();
```

```
            //Add filter to get only SimpleNotes
            dsSelectioFilter.AddEntityType(dsObjectType_e.dsSimpleNoteType);
```

```
            //Activate selection filter
            dsSelectioFilter.Active = true;
```

```
            //Get all Layers in drawing
            string[] layerNames = GetLayerNames(dsDoc);
```

```
            //Get SimpleNote entities
            object entityObjects;
            object entityTypes;
            dsSketchManager.GetEntities(dsSelectioFilter, layerNames, out entityTypes, out entityObjects);
            if (null != entityObjects && null != entityTypes)
            {
                object[] dsEntityArray = (object[])entityObjects;
```

```
                const string newNoteValue = "New sample text";
```

```
                //Iterate through all SimpleNote entities
                for (int index = 0; index < dsEntityArray.Length; ++index)
                {
                    //Cast the selected object to SimpleNote
                    SimpleNote dsSimpleNote = dsEntityArray[index] as SimpleNote;
```

```
                    //Get SimpleNote text
                    string noteValue = dsSimpleNote.Contents;
```

```
                    //Set new text for SimpleNote
                    dsSimpleNote.Contents = newNoteValue;
                }
            }
        }
```

```
    private static string[] GetLayerNames(Document dsDoc)
        {
            string[] layerNames = null;
```

```
            LayerManager dsLayerManager = dsDoc.GetLayerManager();
```

```
            object[] dsLayers = (object[])dsLayerManager.GetLayers();
            if (null != dsLayers)
            {
                layerNames = new string[dsLayers.Length];
```

```
                for (int index = 0; index < dsLayers.Length; ++index)
                {
                    Layer dsLayer = dsLayers[index] as Layer;
                    layerNames[index] = dsLayer.Name;
                }
            }
```

```
            return layerNames;
        }
```

```
}
```
