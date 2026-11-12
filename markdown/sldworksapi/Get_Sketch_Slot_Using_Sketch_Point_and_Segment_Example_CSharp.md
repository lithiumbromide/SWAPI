---
title: "Get Sketch Slot Using Sketch Point and Segment Example(C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_CSharp.htm"
---

# Get Sketch Slot Using Sketch Point and Segment Example(C#)

## Get Sketch Slot Using Sketch Point and Segment Example (C#)

This example shows how to get a sketch slot using a sketch point and a sketch segment.

```
//--------------------------------------------------------
//Preconditions:
// 1. Open a new part document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a sketch slot.
// 2. Gets the length of the sketch slot.
// 3. Selects a sketch point on the sketch slot
//    and accesses the sketch slot using that
//    sketch point.
// 4. Gets the length of the sketch slot.
// 5. Selects a sketch segment on the sketch slot
//    and accesses the sketch slot using that
//    sketch segment.
// 6. Gets the length of the sketch slot.
// 7. Examine the Immediate window.
//-------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
```

```
namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelDocExtension swExt;
        SelectionMgr swSelMgr;
        bool boolstatus;
        SketchManager swSketchManager;
        SketchSlot swSketchSlot;
        SketchPoint swSketchPoint;
        SketchSegment swSketchSegment;
        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSketchManager = (SketchManager)swModel.SketchManager;
```

```
            //Select a plane and open a sketch
            boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager.InsertSketch(true);
```

```
            // Create a sketch slot
            swSketchSlot = (SketchSlot)swSketchManager.CreateSketchSlot((int)swSketchSlotCreationType_e.swSketchSlotCreationType_line, (int)swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter,
                0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, false);
            Debug.Print("Length: " + swSketchSlot.Length);
            Debug.Print("  ");
            swSketchManager.InsertSketch(true);
```

```
            // Get a sketch point on the sketch slot
            boolstatus = swExt.SelectByID2("Point1@Sketch1", "EXTSKETCHPOINT", 0.05, 0.025, 0, false, 0, null, 0);
            swSketchPoint = (SketchPoint)swSelMgr.GetSelectedObject6(1, -1);
            // Get sketch slot
            swSketchSlot = (SketchSlot)swSketchPoint.GetSketchSlot();
            Debug.Print("Length: " + swSketchSlot.Length);
            Debug.Print(" ");
```

```
            // Get a sketch segment on the sketch slot
            boolstatus = swExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.03969355327396, -0.025, 0, false, 0, null, 0);
            swSketchSegment = (SketchSegment)swSelMgr.GetSelectedObject6(1, -1);
            // Get sketch slot
            swSketchSlot = (SketchSlot)swSketchSegment.GetSketchSlot();
            Debug.Print("Length: " + swSketchSlot.Length);
            Debug.Print(" ");
```

```
        }
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
