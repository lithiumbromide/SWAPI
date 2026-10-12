---
title: "Rotate and Copy 3D Sketch About Coordinates Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm"
---

# Rotate and Copy 3D Sketch About Coordinates Example (C#)

This example shows how to rotate and copy 3D sketches.

```
//-----------------------------------------------------------
// Preconditions:
// 1. Open or create a part document with two 3D sketches
//    named 3DSketch1 and 3DSketch2.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Copies and rotates 3DSketch2 around
//    the center point of 3DSketch1's arc.
// 2. Rotates 3DSketch1 around the center point of
//    its arc.
// 3. Examine the FeatureManager design tree and the
//    Immediate window.
//----------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace RotateOrCopy3DAboutXYZCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectData swSelData = default(SelectData);
            SketchManager swSketchMgr = default(SketchManager);
            Sketch swSketch = default(Sketch);
            SketchSegment swSketchSegment = default(SketchSegment);
            bool boolStatus = false;
            object[] varSketchSegments = null;
            int i = 0;

            // If SOLIDWORKS Design is not running, then exit macro
            if (swApp == null)
                return;

            // Document with two 3D sketches, named 3DSketch2 and
            // 3DSketch1, is open and active
            swModel = (ModelDoc2)swApp.ActiveDoc;
            if (swModel == null)
            {
                MessageBox.Show("Failed to open document.");
                return;
            }

            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelMgr.CreateSelectData();
            swSketchMgr = (SketchManager)swModel.SketchManager;

            // Select 3DSketch2
            boolStatus = swModelDocExt.SelectByID2("3DSketch2", "SKETCH", 0, 0, 0, false, 0, null, 0);
            if (boolStatus == false)
            {
                MessageBox.Show("Failed to select 3DSketch2.");
                return;
            }

            // Open 3DSketch2 in edit mode
            swModel.EditSketch();
            swSketch = (Sketch)swSketchMgr.ActiveSketch;
            if (swSketch == null)
            {
                MessageBox.Show("Failed to get pointer to 3DSketch2.");
                return;
            }

            // Select all sketch segments in 3DSketch2
            varSketchSegments = (object[])swSketch.GetSketchSegments();
            for (i = 0; i < varSketchSegments.Length; i++)
            {
                swSketchSegment = (SketchSegment)varSketchSegments[i];
                boolStatus = swSketchSegment.Select4(true, swSelData);
                if (boolStatus == false)
                    MessageBox.Show("Failed to select sketch segment instance." + i + ".");
            }

            // Copy and rotate 3DSketch2 about center
            // point of 3DSketch1's arc
            Debug.Print("Rotating and copying 3DSketch2 about the center point of 3DSketch1's arc? " + swSketchMgr.RotateOrCopy3DAboutXYZ(true, 1, true, -0.09925811702374, 0.004131001848179, 0, 1.5707963267949, 0, 0));
            swModel.ClearSelection2(true);

            // Exit 3DSketch2
            swSketchMgr.InsertSketch(true);

            // Select 3DSketch1
            boolStatus = swModelDocExt.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            if (boolStatus == false)
            {
                MessageBox.Show("Failed to select 3DSketch1.");
                return;
            }

            // Edit 3DSketch1
            swModel.EditSketch();
            swSketch = (Sketch)swModel.GetActiveSketch2();
            if (swSketch == null)
            {
                MessageBox.Show("Failed to get pointer to 3DSketch1.");
                return;
            }

            // Select all sketch segments in 3DSketch1
            varSketchSegments = (object[])swSketch.GetSketchSegments();
            for (i = 0; i < varSketchSegments.Length; i++)
            {
                swSketchSegment = (SketchSegment)varSketchSegments[i];
                boolStatus = swSketchSegment.Select4(true, swSelData);
                if (boolStatus == false)
                {
                    MessageBox.Show("Failed to select sketch segment instance." + i + ".");
                    return;
                }
            }

            // Rotate 3DSketch1 about the
            // center point of its arc
            Debug.Print("Rotating 3DSketch1 about the center point of its arc? " + swSketchMgr.RotateOrCopy3DAboutXYZ(false, 1, true, -0.09925811702374, 0.004131001848179, 0, 1.5707963267949, 0, 0));
            swModel.ClearSelection2(true);

            // Exit 3DSketch1
            swSketchMgr.InsertSketch(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
