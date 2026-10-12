---
title: "Apply and Remove Texture By Body Display State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Body_Display_State_Example_CSharp.htm"
---

# Apply and Remove Texture By Body Display State Example (C#)

## Apply and Remove Texture By Body Display State (C#)

This example shows how to apply and remove texture to and from a body by a display state.

```
//--------------------------------------------------
// Preconditions: Verify that the specified part to open
// and texture exist.
//
// Postconditions:
// 1. Opens the specified part and applies texture to the
//    selected body.
// 2. In the IDE, click the Continue button
//    at System.Diagnostics.Debugger.Break().
// 3. Removes texture from selected body.
// 4. To verify, click the Stop Debugging button in the
//    IDE to stop execution of the macro and click anywhere
//    in the graphics area.
//    - or -
//    If the Stop Debugging button is grayed out, click
//    anywhere in the graphics area.
//----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace SetRemoveTextureByDisplayStateBodyCSharp.csproj
```

```vb
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Body2 body = default(Body2);
            Texture texture = default(Texture);
            ModelView modelview = default(ModelView);
            bool status = false;
            string displayState = null;
            int errors = 0;
            int warnings = 0;
            string namStr = null;

            // Open document and select a body
            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_bridge.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            body = (Body2)swSelMgr.GetSelectedObject6(1, -1);

            // Set texture on selected body in the
            // specified display state
            displayState = "<Default>_Display State 1";
            namStr = "<SystemTexture>\\images\\textures\\pattern\\checker2.jpg";
            texture = (Texture)swModelDocExt.CreateTexture(namStr, 5, 45, false);
            status = body.SetTextureByDisplayState(displayState, texture);

            // Redraw the window view
            modelview = (ModelView)swModel.ActiveView;
            modelview.GraphicsRedraw(null);

            // Examine the selected body to verify
            // that the specified texture was set
            // In the IDE, click the Continue button to resume
            // running macro
            System.Diagnostics.Debugger.Break();

            // Remove texture from body by display state
            status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
            body = (Body2)swSelMgr.GetSelectedObject6(1, -1);
            status = body.RemoveTextureByDisplayState(displayState);
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
