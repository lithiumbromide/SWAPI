---
title: "Apply and Remove Texture By Display State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Display_State_Example_CSharp.htm"
---

# Apply and Remove Texture By Display State Example (C#)

This example shows how to apply and remove texture to and from a face by display state.

```vb
//---------------------------------------------------------------------------
 // Preconditions: Verify that the specified part and texture exist.
 //
 // Postconditions:
 // 1. Opens the part and applies texture to the selected face.
 // 2. Examine the part.
 // 3. In the IDE, click the Continue button at
 //    System.Diagnostics.Debugger.Break().
 // 4. Removes the texture from the selected face.
 // 5. To verify, click the Stop Debugging button in the IDE
 //    to stop execution of the macro, then click anywhere
 //    in the SOLIDWORKS Design graphics area.
 //--------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace SetRemoveTextureByDisplayStateFaceCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Face2 face = default(Face2);
            Texture texture = default(Texture);
            ModelView modelview = default(ModelView);
            bool status = false;
            string displayState = null;
            int errors = 0;
            int warnings = 0;
            string namStr = null;

            // Open document and select a face
            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\api\\pplate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension) swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            face = (Face2) swSelMgr.GetSelectedObject6(1, -1);

            // Set texture on selected face in the
            // specified display state
            displayState = "<Default>_Display State 1";
            namStr = "<SystemTexture>\\images\\textures\\pattern\\checker2.jpg";
            texture = (Texture) swModelDocExt.CreateTexture(namStr, 5, 45, false);
            status = face.SetTextureByDisplayState(displayState, texture);

            // Redraw the window view
            modelview = (ModelView)swModel.ActiveView;
            modelview.GraphicsRedraw(null);

            // Examine the selected face to verify
            // that the specified texture was set
            // In the IDE, click the Continue button to resume
            // running macro
            System.Diagnostics.Debugger.Break();

            // Remove texture from face by display state
            status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, false, 0, null, 0);
            face = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            status = face.RemoveTextureByDisplayState(displayState);
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
