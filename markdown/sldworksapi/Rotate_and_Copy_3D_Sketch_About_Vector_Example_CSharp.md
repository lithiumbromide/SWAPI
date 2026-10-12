---
title: "Rotate and Copy 3D Sketch About Vector Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_and_Copy_3D_Sketch_About_Vector_Example_CSharp.htm"
---

# Rotate and Copy 3D Sketch About Vector Example (C#)

This example shows how to rotate and copy 3D sketches about a vector.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a part that contains two 3D sketches,
//    3DSketch1 and 3DSketch2.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Copies and rotates the 3DSketch2 sketch around
//    the center point of the 3DSketch1 sketch's arc.
// 2. Rotates the 3DSketch1 sketch around the center
//    point of its arc.
// 3. Examine the Immediate window.
//---------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace RotateorCopy3DAboutVectorXYZ_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectData swSelData = default(SelectData);
            SketchManager swSketchMgr = default(SketchManager);
            Sketch swSketch = default(Sketch);
            bool boolStatus = false;
            object[] varSketchSegments = null;
            int i = 0;
            if (swApp == null) return;
            // Document with two 3D sketches, named 3DSketch2 and
            // 3DSketch1, is open and active
            swModel = (ModelDoc2)swApp.ActiveDoc;
            if (swModel == null)
            {
                System.Windows.Forms.MessageBox.Show("Failed to open document.");
                return;
            }
            swModelDocExt = swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelMgr.CreateSelectData();
            swSketchMgr = swModel.SketchManager;
            // Select 3DSketch2 sketch
            boolStatus = swModelDocExt.SelectByID2("3DSketch2", "SKETCH", 0, 0, 0, false, 0, null, 0);
            if (boolStatus == false)
            {
                System.Windows.Forms.MessageBox.Show("Failed to select sketch 3DSketch2.");
                return;
            }
            // Open 3DSketch2 sketch in edit mode
            swModel.EditSketch();
            swSketch = swSketchMgr.ActiveSketch;
            if (swSketch == null)
            {
                System.Windows.Forms.MessageBox.Show("Failed to get pointer to 3DSketch2 sketch.");
                return;
            }
            // Select all sketch segments in 3DSketch2 sketch
            varSketchSegments = (object[])swSketch.GetSketchSegments();
            for (i = 0; i <= varSketchSegments.GetUpperBound(0); i++)
            {
                boolStatus = ((SketchSegment)varSketchSegments[i]).Select4(true, swSelData);
                if (boolStatus == false) System.Windows.Forms.MessageBox.Show("Failed to select sketch segment instance." + i + ".");
            }
            // Copy and rotate 3DSketch2 sketch about center
            // point of 3DSketch1 sketch's arc
            Debug.Print("Rotating and copying 3DSketch2 sketch about the center point of 3DSketch1's arc? " + swSketchMgr.RotateOrCopy3DAboutVector(true, 1, true, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949
            ));
            swModel.ClearSelection2(true);
            // Exit 3DSketch2 sketch
            swSketchMgr.InsertSketch(true);
            // Select 3DSketch1 sketch
            boolStatus = swModelDocExt.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            if (boolStatus == false)
            {
                System.Windows.Forms.MessageBox.Show("Failed to select sketch 3DSketch1.");
                return;
            }
            // Edit 3DSketch1 sketch
            swModel.EditSketch();
            swSketch = (Sketch)swModel.GetActiveSketch2();
            if (swSketch == null)
            {
                System.Windows.Forms.MessageBox.Show("Failed to get pointer to sketch 3DSketch1.");
                return;
            }
            // Select all sketch segments in 3DSketch1 sketch
            varSketchSegments = (object[])swSketch.GetSketchSegments();
            for (i = 0; i <= varSketchSegments.GetUpperBound(0); i++)
            {
                boolStatus = ((SketchSegment)varSketchSegments[i]).Select4(true, swSelData);
                if (boolStatus == false)
                {
                    System.Windows.Forms.MessageBox.Show("Failed to select sketch segment instance." + i + ".");
                    return;
                }
            }
            // Rotate 3DSketch1 sketch about the
            // center point of its arc
            Debug.Print("Rotating 3DSketch1 sketch about the center point of its arc? " + swSketchMgr.RotateOrCopy3DAboutVector(false, 1, true, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949
            ));
            swModel.ClearSelection2(true);
            // Exit 3DSketch1 sketch
            swSketchMgr.InsertSketch(true);
        }
        public SldWorks swApp;
    }
}
```
