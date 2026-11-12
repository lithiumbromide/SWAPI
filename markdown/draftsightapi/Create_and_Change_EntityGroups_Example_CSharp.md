---
title: "Create and Change EntityGroups Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Change_EntityGroups_Example_CSharp.htm"
---

# Create and Change EntityGroups Example (C#)

This example shows how to create and change EntityGroups.

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
// 1. Inserts entities, two lines and two circles, in the drawing.
// 2. Creates two EntityGroups:
//    * SampleGroup1 contains two lines, line1 and line2.
//    * SampleGroup2 contains two circles, circle1 and circle2.
// 3. Changes the color of the lines from white to red.
// 4. Removes an entity, circle1, from SampleGroup2.
// 5. Adds an entity, circle2, to SampleGroup1.
// 6. Reorders SampleGroup1.
// 7. Explodes SampleGroup2, which removes the definition
//    from the drawing; however, circle1 remains as an entity
//    in the drawing.
// 8. Renames SampleGroup1 and changes its description.
//
// NOTE: Execution of the macro stops several times. Follow the
// instructions in the macro each time execution stops.
//----------------------------------------------------------------
using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;

namespace EntityGroup
{

    static class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;
        private static Document dsDoc;

        static void Main()
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
            dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Insert entities
            SketchManager dsSketchMgr = dsApp.GetActiveDocument().GetModel().GetSketchManager();
            Line line1 = dsSketchMgr.InsertLine(0, 0, 0, 10, 10, 0);
            Line line2 = dsSketchMgr.InsertLine(5, 0, 0, 15, 10, 0);
            Circle circle1 = dsSketchMgr.InsertCircle(5, 5, 0, 10);
            Circle circle2 = dsSketchMgr.InsertCircle(10, 5, 0, 10);

            DispatchWrapper[] EntitiesArray1 = new DispatchWrapper[2];
            EntitiesArray1[0] = new DispatchWrapper(line1);
            EntitiesArray1[1] = new DispatchWrapper(line2);

            DispatchWrapper[] EntitiesArray2 = new DispatchWrapper[2];
            EntitiesArray2[0] = new DispatchWrapper(circle1);
            EntitiesArray2[1] = new DispatchWrapper(circle2);

            CreateGroups(EntitiesArray1, EntitiesArray2);

            System.Diagnostics.Debugger.Break();
            //Type GROUP at the command window
            //to verify that two EntityGroups, SampleGroup1
            //and SampleGroup2, were created
            //Press OK to close the dialog
            //Press F5 in the IDE to continue

            //Get SampleGroup2 and remove circle2
            Group dsGroup2 = dsDoc.GetGroup("SampleGroup2");
            if (dsGroup2.HasEntity(circle2))
            {
                int index = dsGroup2.GetIndex(circle2);
                dsGroup2.RemoveEntityAt(index);
            }

            //Get SampleGroup1 and add circle1 at last position
            Group dsGroup1 = dsDoc.GetGroup("SampleGroup1");
            DispatchWrapper[] EntitiesArray = new DispatchWrapper[1];
            EntitiesArray[0] = new DispatchWrapper(circle1);
            int count = dsGroup1.GetEntitiesCount();
            dsGroup1.InsertEntitiesAt(count, EntitiesArray);

            int newCount = dsGroup1.GetEntitiesCount();
            if (newCount != count + 1)
                MessageBox.Show("Circle1 was not inserted.");

            //Move circle1 to second position (index 1)
            int circleIndex = dsGroup1.GetIndex(circle1);
            if (circleIndex != count)
                MessageBox.Show("Circle1 inserted at wrong position.");

            dsGroup1.Reorder(circleIndex, 1, 1);
            circleIndex = dsGroup1.GetIndex(circle1);
            if (circleIndex != 1)
                MessageBox.Show("Circle1 inserted at wrong position.");

            //Explode SampleGroup2
            dsGroup2.Explode();

            System.Diagnostics.Debugger.Break();
            //Type GROUP at the command window
            //to verify that only SampleGroup1 exists
            //Press OK to close the dialog
            //Press F5 in the IDE to continue

            object dsGroups = null;
            dsGroups = dsDoc.GetGroups();

            object[] groupObjects = (object[])dsGroups;
            if (groupObjects.Length != 1)
                MessageBox.Show("Group2 was not exploded.");

            //Rename SampleGroup1 and change description
            dsGroup1.Rename("SampleGroup");
            dsGroup1.Description = "My sample group.";

            System.Diagnostics.Debugger.Break();
            //Type GROUP at the command window
            //to verify that SampleGroup1 was renamed
            //to SampleGroup and its description
            //changed to "My sample group"
            //Press OK to close the dialog
            //Press F5 in the IDE to continue
        }

        private static void CreateGroups(DispatchWrapper[] EntitiesArray1, DispatchWrapper[] EntitiesArray2)
        {
            //Create group
            Group dsGroup1 = dsDoc.CreateGroup("SampleGroup1", false, "This is my first sample group.", EntitiesArray1);

            object dsEntities = null;
            object dsEntityTypes = null;

            dsEntities = dsGroup1.GetEntities(out dsEntityTypes);

            object[] entityObjects = (object[])dsEntities;
            int[] dsEntityTypesArray = (int[])dsEntityTypes;

            if (null == entityObjects && null == dsEntityTypesArray)
            {
                return;
            }

            //Change color of lines from white to red
            EntityHelper dsEntityHelper = dsApp.GetEntityHelper();
            Color dsColor = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Red);

            foreach (object dsEntity in entityObjects)
            {
                if (dsEntity != null)
                {
                    dsEntityHelper.SetColor(dsEntity, dsColor);
                }
            }

            Group dsGroup2 = dsDoc.CreateGroup("SampleGroup2", false, "This is my second sample group.", EntitiesArray2);
        }
    }
}
```
