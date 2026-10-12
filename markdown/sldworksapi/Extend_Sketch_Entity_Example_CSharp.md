---
title: "Extend Sketch Entity Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Extend_Sketch_Entity_Example_CSharp.htm"
---

# Extend Sketch Entity Example (C#)

This example shows how to extend a selected sketch entity (e.g., line, segment, or arc) to meet another sketch entity.

```
//-------------------------------------------------------------------
// Preconditions: Open a new part document.
//
// Postconditions:
// 1. Inserts a new sketch is inserted.
// 2. Creates two non-parallel lines.
// 3. Extends the first line to meet the second line.
// 4. Examine the graphics area.
//-------------------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace ExtendEntity_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        ModelDocExtension swModelDocExt;

	        SketchManager swSketchMgr;

	        bool boolstatus;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swModelDocExt = swModel.Extension;

	            swSketchMgr = swModel.SketchManager;

	            swSketchMgr.InsertSketch(false);

	            // Create two non-parallel
	lines

	            swSketchMgr.CreateLine(-0.5,
	0.88, 0.0, -0.21, -0.13, 0.0);

	            swSketchMgr.CreateLine(-0.75, -1.128, 0.0, 0.41, -1.128,
	0.0);
```

```vb
            swModel.ViewZoomtofit2();

             // Set the selection mode to default
             swModel.SetPickMode();

             // Select the sketch line to extend
             boolstatus = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0.0, 0.0, 0.0, false, 0, null, 0);

             // Extend the selected sketch line to meet the second line
             boolstatus = swSketchMgr.SketchExtend(0.0, 0.0, 0.0);

             swSketchMgr.InsertSketch(true);

         }

         public SldWorks swApp;

     }
 }
```
