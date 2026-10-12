---
title: "Add Balloon to Stacked Balloon Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Balloon_to_Stacked_Balloon_Example_CSharp.htm"
---

# Add Balloon to Stacked Balloon Example (C#)

This example shows how to create a stacked balloon and add a balloon to the stacked balloon.

```
//------------------------------------------------------------
// Preconditions: Verify that the specified assembly
// document to open exists.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Selects a face on the Part4 component.
// 3. Creates a stacked balloon showing the item number
//    of Part4 and inserts that stacked balloon on the selected face.
// 4. Adds a balloon, which shows the number of seed and derived Part4
//    components in the the assembly, to the stacked balloon.
// 5. Click and drag the stacked balloon upward in the graphics area.
//-------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace StackedBalloonsCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            StackedBalloonOptions swStackedBalloons = default(StackedBalloonOptions);
            Note swNote = default(Note);
            BalloonStack swBalloonStack = default(BalloonStack);
            Note swNote2 = default(Note);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem2.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            swModel.ViewZoomtofit2();

            status = swModelDocExt.SelectByID2("", "FACE", -0.311973500811291, 0.0329693343254007, 0.00999999999999091, false, 0, null, 0);
            swStackedBalloons = swModelDocExt.CreateStackedBalloonOptions();
            swStackedBalloons.BalloonsPerLine = 10;
            swStackedBalloons.StackDirection = (int)swStackedBalloonDirection_e.swStackedBalloonDir_Right;
            swStackedBalloons.Style = (int)(int)swBalloonStyle_e.swBS_Circular;
            swStackedBalloons.Size = (int)swBalloonFit_e.swBF_2Chars;
            swStackedBalloons.UpperTextContent = (int)swBalloonTextContent_e.swBalloonTextItemNumber;
            swStackedBalloons.UpperText = "\"";
            swStackedBalloons.ShowQuantity = false;
            swStackedBalloons.QuantityPlacement = (int)swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Top;
            swStackedBalloons.QuantityDenotationText = "X";
            swStackedBalloons.QuantityOverride = false;
            swNote = (Note)swModelDocExt.InsertStackedBalloon2(swStackedBalloons);
            status = swModelDocExt.SelectByID2("", "FACE", -0.292957708052256, 0.0316192505406434, 0.0100000000000477, false, 0, null, 0);

            if (swNote.IsStackedBalloon())
            {
                if ((swNote != null))
                {
                    swBalloonStack = (BalloonStack)swNote.GetBalloonStack();
                    swNote2 = (Note)swBalloonStack.AddTo((int)swBalloonTextContent_e.swBalloonTextQuantity, "12", (int)swBalloonTextContent_e.swBalloonTextQuantity, "");
                }
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
