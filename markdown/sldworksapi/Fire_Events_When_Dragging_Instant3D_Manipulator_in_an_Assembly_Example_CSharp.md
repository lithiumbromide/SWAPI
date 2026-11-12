---
title: "Fire Events When Dragging Instant3D Manipulator in an Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_CSharp.htm"
---

# Fire Events When Dragging Instant3D Manipulator in an Assembly Example (C#)

This example shows how to fire events when dragging an Instant3D manipulator in an assembly document.

```vb
//------------------------------------
 // Preconditions:
 // 1. Open an assembly document.
 // 2. Open the Immediate window.
 //
 // NOTE: Instant3D is enabled by the macro.
 //
 // Postconditions:
 // 1. Select an Instant3D manipulator in the
 //    open assembly by right-clicking a floating
 //    assembly component, clicking the down arrows
 //    at the bottom of the shortcut menu, and selecting
 //    Move with Triad.
 // 2. Drag the Instant3D handle to move the assembly component.
 // 3. Writes a debug statement to the Immediate window
 //    informing you that dragging of an Instant3D manipulator
 //    has started.
 // 4. Stop dragging the manipulator.
 // 5. Writes a debug statement to the Immediate
 //    window informing you that dragging of
 //    an Instant3D manipulator has stopped.
 // 6. Examine the Immediate window.
 //----------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Collections;
 using System.Diagnostics;
 namespace DragStateChangeNotifyAssemblyCSharp.csproj
 {    partial class SolidWorksMacro
     {
         public AssemblyDoc pDoc;
         public FeatureManager swFeatMgr;
         public void Main()
         {
             ModelDoc2 swModel;
             Hashtable openAssembly;

             swModel = (ModelDoc2)swApp.ActiveDoc;

             //Enable Instant3D manipulators
             swFeatMgr = (FeatureManager)swModel.FeatureManager;
             swFeatMgr.MoveSizeFeatures = true;

             // Set up event handler
             pDoc = (AssemblyDoc)swModel;
             openAssembly = new Hashtable();
             AttachEventHandlers();
         }

         public void AttachEventHandlers()
         {
             AttachSWEvents();
         }

         public void AttachSWEvents()
         {
             if ((pDoc != null))
             {
                 pDoc.DragStateChangeNotify += this.pDoc_DragStateChangeNotify;
             }
         }

         private int pDoc_DragStateChangeNotify(bool State)
         {
             int functionReturnValue = 0;
             // Write debug statement when dragging of manipulator started and stopped
             if (State == true)
             {
                 Debug.Print("Dragging of manipulator started.");
                 functionReturnValue = 1;
             }
             else
             {
                 Debug.Print("Dragging of manipulator stopped.");
                 functionReturnValue = 0;
             }
             return functionReturnValue;
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;

     }
 }
```
