---
title: "Insert Shapes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Shapes_Example_CSharp.htm"
---

# Insert Shapes Example (C#)

This example shows how to load a shape file and insert the shapes in the loaded shape file into a drawing.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Start debugging the project.
//
// Postconditions:
// 1. Gets the Shape Manager.
// 2. Loads a shape file.
// 3. Gets the shapes in the loaded shape file.
// 4. Inserts the shapes, with an obliquing angle of 30, in the drawing.
// 5. Examine the drawing.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace ShapeCSharp
{
    class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;

        static void Main(string[] args)
        {
            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            // Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            if (null == dsApp)
            {
                return;
            }

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get the Shape Manager
            ShapeManager dsShapeMgr = dsDoc.GetShapeManager();

            //Load shape file LTypeShp.shx
            SystemFiles dsSysFile = dsApp.GetSystemFiles();
            object[] FontsPathObj = (object[])dsSysFile.FontsPaths;
            string fontPath = "";
            if (FontsPathObj.Length > 0)
                fontPath = FontsPathObj[0].ToString();

            string shapeFileName = System.IO.Path.Combine(fontPath, "LTypeShp.shx");

            dsShapeMgr.Load(shapeFileName);

            //Get shapes
            object[] shapesStrList = (object[])dsShapeMgr.GetAvailableShapes();
            int shapesCount = shapesStrList.Length;

            //Get Sketch Manager
            SketchManager dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Insert shapes
            double PositionX = 0.0, PositionY = 0.0, PositionZ = 0.0;
            for (int i = 0; i < shapesCount; ++i)
            {
                Shape dsShape = dsSketchMgr.InsertShape(shapesStrList[i].ToString(), PositionX, PositionY, PositionZ, 1, 0.0);

                //Change obliquing property
                dsShape.Obliquing = 30 * Math.PI / 180;

                double X1, Y1, Z1, X2, Y2, Z2;
                dsShape.GetBoundingBox(out X1, out Y1, out Z1, out X2, out Y2, out Z2);

                PositionX += (X2 - X1) + 5;
            }
        }

     }
}
```
