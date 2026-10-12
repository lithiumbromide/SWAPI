---
title: "Fire Events When Dragging Instant3D Manipulator in a Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_CSharp.htm"
---

# Fire Events When Dragging Instant3D Manipulator in a Part Example (C#)

This example shows how to fire events when dragging an Instant3D manipulator in a part document.

```vb
//------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Open the Immediate window.
 //
 // NOTE: Instant3D is enabled by the macro.
 //
 // Postconditions:
 // 1. Select an Instant3D manipulator in the
 //    open part. For example,
 //    double-click an extrude feature in a part,
 //    then select one of the Instant3D manipulators
 //    and drag it.
 // 2. Writes a debug statement to the Immediate
 //    window informing you that dragging of an
 //    Instant3D manipulator has started.
 // 3. Stop dragging the manipulator.
 // 4. Writes a debug statement to the Immediate
 //    window informing you that dragging of
 //    an Instant3D manipulator has stopped.
 // 5. Examine the Immediate window.
 //----------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Collections;
 using System.Diagnostics;
 namespace DragStateChangeNotifyPartCSharp.csproj
 {
     partial class SolidWorksMacro    {
         public PartDoc pDoc;
         public FeatureManager swFeatMgr;
         public void Main()
         {
             ModelDoc2 swModel;
             Hashtable openPart;

             swModel = (ModelDoc2)swApp.ActiveDoc;

             //Enable Instant3D manipulators
             swFeatMgr = (FeatureManager)swModel.FeatureManager;
             swFeatMgr.MoveSizeFeatures = true;

             // Set up event handler
             pDoc = (PartDoc)swModel;
             openPart = new Hashtable();

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
             }            else
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
