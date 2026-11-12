---
title: "Run SOLIDWORKS Commands and Synthesize Mouse Events Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm"
---

# Run SOLIDWORKS Commands and Synthesize Mouse Events Example (C#)

This example shows how to run SOLIDWORKS commands and synthesize mouse events.

```
//-----------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document to open exists.
// 2. Click Tools > Options and click to clear the Stop VSTA debugger
//    on macro exit check box, if it is selected.
// 3. In the IDE, right-click the project name in the Project Explorer,
//    click Add Reference, browse install_dir\api\redist, click
//    SolidWorks.Interop.swcommands.dll, and click OK.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Fits the model to the graphics area.
// 3. Moves the mouse.
// 4. Changes the view orientation to *Front.
// 5. Select an edge on the model.
// 6. Left-click anywhere outside the model in the graphics area.
// 7. Examine the Immediate window.
// 8. Click Stop Debugging in the IDE.
// 9. Click Tools > Options and click to select the Stop VSTA debugger
//    on macro exit check box, if it is clear.
//-----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swcommands;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MouseCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public Mouse msMouse;

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            ModelView swModelView = default(ModelView);
            Mouse TheMouse = default(Mouse);
            int i = 0;
            double x = 0;
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            bool status = false;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swModelView = (ModelView)swModel.GetFirstModelView();
            TheMouse = (Mouse)swModelView.GetMouse();

            //Set up events
            msMouse = (Mouse)TheMouse;
            AttachEventHandlers();

            x = 0;

            Debug.Print("Fit model to graphics area");
            swModelDocExt.RunCommand((int)swCommands_e.swCommands_ZoomToFit, "");

            //Move the mouse
            status = TheMouse.Move(50, 150, (int)swMouse_e.swMouse_Absolute + (int)swMouse_e.swMouse_MouseMove + (int)swMouse_e.swMouse_LeftDown);
            Debug.Print("First call to Move: " + status);
            Debug.Print("Calls to Move within loop:");
            for (i = 1; i <= 5; i++)
            {
                status = TheMouse.Move(5, 5, (int)swMouse_e.swMouse_MouseMove);
                Debug.Print("  Call " + i + " to Move: " + status);
            }
            status = TheMouse.Move(0, 0, (int)swMouse_e.swMouse_LeftUp);
            Debug.Print("Last call to Move: " + status);

            status = TheMouse.MoveXYZ(0.03720615681732, 0.0316583060694, 0.04991700841805, (int)swMouse_e.swMouse_LeftDown);
            Debug.Print("Call to MoveXYZ: " + status);
            Debug.Print("Calls to Move within next loop:");
            for (i = 1; i <= 5; i++)
            {
                status = TheMouse.Move(5, 5, (int)swMouse_e.swMouse_MouseMove);
                Debug.Print("  Call " + (i + 1).ToString() + " to Move: " + status);
            }

            status = TheMouse.Move(10, 10, (int)swMouse_e.swMouse_LeftUp);
            Debug.Print("Last call to Move: " + status);

            Debug.Print("Change view to *Front");
            swModelDocExt.RunCommand((int)swCommands_e.swCommands_Front, "");

        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {

            msMouse.MouseSelectNotify += this.ms_MouseSelectNotify;
            msMouse.MouseLBtnDownNotify += this.ms_MouseLBtnDownNotify;

        }

        private int ms_MouseSelectNotify(int Ix, int Iy, double x, double y, double z)
        {
            Debug.Print("Selection made:");
            Debug.Print(" Mouse location:");
            Debug.Print("   Window space coordinates:");
            Debug.Print("     " + Ix);
            Debug.Print("     " + Iy);
            Debug.Print("   World space coordinates:");
            Debug.Print("     " + x);
            Debug.Print("     " + y);
            Debug.Print("     " + z);

            return 1;
        }

        private int ms_MouseLBtnDownNotify(int x, int y, int WParam)
        {
            Debug.Print("Left-mouse button pressed.");

            return 1;
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
