---
title: "Selectively and Transparently Section a Section View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm"
---

# Selectively and Transparently Section a Section View Example (C#)

This example shows how to selectively and transparently section a section view.

```
//-------------------------------------------------------------------------
// Preconditions: Verify that the assembly to open exists.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Selects the component for selective sectioning.
// 3. Selects the components for transparent sectioning.
// 4. Selects the planes for sectioning.
// 5. Creates the SectionViewData object.
//    a. Sets the section method to zonal.
//    b. Sets to cap the sections.
//    c. Sets to generate a graphics-only section view.
//    d. Enables selective sectioning.
//       1. Sets the component selected in step 2 for selective
//          sectioning.
//       2. Sets the intersection zone.
//       3. Sets to exclude the component set in step 5.d.1 from
//          selective sectioning.
//    e. Enables transparent sectioning.
//       1. Sets the components selected in step 3
//          for transparent sectioning.
//       2. Sets to include the sectioned components set in step 5.e.1
//          in transparent sectioning.
//       3. Sets the level of transparency.
// 6. Creates the section view.
// 7. Examine the graphics area.
// 8. Click Section View twice in the Heads-Up View toolbar and
//    examine the Section View PropertyManager page.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Component2[] selectiveArray = new Component2[1];
            Component2 selComponent = default(Component2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Component2[] transparentArray = new Component2[2];
            Component2 transComponent = default(Component2);
            Component2 transComponent2 = default(Component2);
            SectionViewData swSectionViewData = default(SectionViewData);
            ModelViewManager swModelViewManager = default(ModelViewManager);
            object transArray = new object[2];
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            object[] selArray = new object[1];

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\floxpress\\ball valve\\ball_valve.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            status = swModelDocExt.SelectByID2("Ball-1@ball_valve", "COMPONENT", 0, 0, 0, true, 8, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            selComponent = (Component2)swSelMgr.GetSelectedObject6(1, -1);
            selectiveArray[0] = selComponent;
            selArray = (object[])selectiveArray;

            status = swModelDocExt.SelectByID2("Side-1@ball_valve", "COMPONENT", 0, 0, 0, true, 32, null, 0);
            status = swModelDocExt.SelectByID2("Side-2@ball_valve", "COMPONENT", 0, 0, 0, true, 32, null, 0);
            transComponent = (Component2)swSelMgr.GetSelectedObject6(1, -1);
            transComponent2 = (Component2)swSelMgr.GetSelectedObject6(2, -1);
            transparentArray[0] = transComponent;
            transparentArray[1] = transComponent2;
            transArray = (object[])transparentArray;

            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Plane2", "PLANE", 0, 0, 0, true, 2, null, 0);
            status = swModelDocExt.SelectByID2("Plane3", "PLANE", 0, 0, 0, true, 4, null, 0);

            swModelViewManager = (ModelViewManager)swModel.ModelViewManager;
            swSectionViewData = swModelViewManager.CreateSectionViewData();

            swSectionViewData.FirstColor = 16711680;
            swSectionViewData.SecondColor = 65280;
            swSectionViewData.ThirdColor = 255;
            swSectionViewData.ShowSectionCap = true;
            swSectionViewData.KeepCapColor = true;
            swSectionViewData.GraphicsOnlySection = true;

            swSectionViewData.ZonalSection = true;

            swSectionViewData.SelectiveSection = true;
            swSectionViewData.SelectiveSectioningList = selArray;
            swSectionViewData.SectionedZones = 16; //swZonalSectionViewZones_e.swZonalSectionViewZones_swZonalSectionViewZone_5
            swSectionViewData.ExcludeSelectedItems = true;

            swSectionViewData.TransparentSection = true;
            swSectionViewData.TransparencyList = transArray;
            swSectionViewData.SectionTransparentItemsTransparent = true;
            swSectionViewData.TransparencyValue = 0.9;

            status = swModelViewManager.CreateSectionView(swSectionViewData);

            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
