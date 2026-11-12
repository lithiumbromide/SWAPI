---
title: "Move Freeze Bar Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Freeze_Bar_Example_CSharp.htm"
---

# Move Freeze Bar Example (C#)

This example shows how to move the freeze bar to another location in the FeatureManager design tree.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\FreezeBarNeedsRebuild2.sldprt.
 // 2. Inspect the FeatureManager design tree:
 //    * The rebuild indicator is displayed in the FeatureManager design tree.
 //    * The freeze bar is below Boss-Extrude1 in the FeatureManager design tree.
 //    * Boss-Extrude1 is frozen in the FeatureManager design tree.
 //    * Boss-Extrude2 is unfrozen in the FeatureManager design tree.
 //    * Boss-Extrude1 has freeze updates pending.
 //    * Boss-Extrude2 has no freeze updates pending.
 //    * The model needs to be rebuilt.
 //
 // Postconditions:
 // 1. Removes the rebuild indicator from the part.
 // 2. Inspect the Immediate window to see which features have hidden locks.
 // 3. Press F5 to continue.
 //    * Freeze bar moved to the top of the FeatureManager design tree.
 //    * Boss-Extrude1 is unfrozen.
 // 4. Press F5 to continue.
 //    * Freeze bar moved to the bottom of the FeatureManager design tree.
 //    * Boss-Extrude1 and Boss-Extrude2 are frozen.
 // 5. Press F5 to continue.
 //    * Freeze bar moved to after Boss-Extrude2.
 //    * Boss-Extrude1 and Boss-Extrude2 are frozen.
 // 6. Press F5 to continue.
 //    * Freeze bar moved to the top of the FeatureManager design tree.
 //    * Boss-Extrude1 and Boss-Extrude2 are unfrozen.
 // 7. Press F5 to continue.
 //    * The model does not need to be rebuilt.
 //    * Boss-Extrude1 and Boss-Extrude2 have no freeze updates pending.
 // 8. Press F5 to close the model.
 // 9. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace MoveFreezeBar_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModDocExt;
         int lRet;
         FeatureManager featMgr;
         SelectionMgr selMgr;
         Feature featFrozen;
         Feature featUnFrozen;
         Feature feat;
         bool boolstatus;
         Object[] vfeats;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModDocExt = swModel.Extension;
             featMgr = swModel.FeatureManager;
             selMgr = (SelectionMgr)swModel.SelectionManager;

            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swUserEnableFreezeBar, true);
             swModDocExt.ShowPartRebuildIndicators = false;

             Debug.Print("Number of Features is " + swModel.GetFeatureCount());

             vfeats = (Object[])featMgr.GetFeatures(true);

             for (int i = 0; i < vfeats.GetLength(0); i++ )
             {
                 feat = (Feature)vfeats[i];
                 Debug.Print("Feature name from FeatureManager design tree is " + feat.Name);
                 Debug.Print(feat.Name + " has a hidden lock? " + feat.IsHiddenLock());
             }

             boolstatus = swModDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             boolstatus = swModDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, true, 0, null, 0);

             feat = featMgr.GetFreezeLocation();
             if ((feat != null))
             {
                 Debug.Print("");
                 Debug.Print("Freeze bar location is after " + feat.Name);
                 Debug.Print(feat.Name + " is frozen? " + feat.IsFrozen());
             }

             lRet = swModDocExt.NeedsRebuild2;
             Debug.Print("Needs rebuild? " + lRet);

             featFrozen = (Feature)selMgr.GetSelectedObject6(1, -1);
             Debug.Print("Feature " + featFrozen.Name +  " has frozen updates pending? " + featFrozen.HasFrozenUpdatePending());
             featUnFrozen = (Feature)selMgr.GetSelectedObject6(2, -1);
             Debug.Print("Feature " + featUnFrozen.Name +  " has frozen updates pending? " + featUnFrozen.HasFrozenUpdatePending());
             Debug.Print("");

             swModel.ClearSelection2(true);

             System.Diagnostics.Debugger.Break();

             if ((featFrozen.HasFrozenUpdatePending()))
             {
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToBeforeFeature, featFrozen.Name, true, true);
                 Debug.Print("Freeze bar moved to the top of the FeatureManager design tree. Press F5.");
                 System.Diagnostics.Debugger.Break();
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToEnd, "", true, true);
                 Debug.Print("Freeze bar moved to the bottom of the FeatureManager design tree. Press F5.");
                 System.Diagnostics.Debugger.Break();
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToAfterFeature, featUnFrozen.Name, true, true);
                 Debug.Print("Freeze bar moved to after Boss-Extrude2. Press F5.");
                 System.Diagnostics.Debugger.Break();
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToTop, "", true, true);
                 Debug.Print("Freeze bar moved to the top of the FeatureManager design tree. Press F5.");
                 System.Diagnostics.Debugger.Break();
             }
             else
             {
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToBeforeFeature, featFrozen.Name, true, true);
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToEnd, "", true, true);
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToBeforeFeature, featUnFrozen.Name, true, true);
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToAfterFeature, featUnFrozen.Name, true, true);
                 lRet = featMgr.EditFreeze2((int)swMoveFreezeBarTo_e.swMoveFreezeBarToTop, "", true, true);
             }

             lRet = swModDocExt.NeedsRebuild2;
             Debug.Print("Needs rebuild? " + lRet);

             Debug.Print("Feature " + featFrozen.Name +  " has frozen updates pending? " + featFrozen.HasFrozenUpdatePending());
             Debug.Print("Feature " + featUnFrozen.Name +  " has frozen updates pending? " + featUnFrozen.HasFrozenUpdatePending());

             feat = featMgr.GetFreezeLocation();
             // feat = Null if freeze bar is at the top of FeatureManager design tree
             if ((feat != null))
             {
                 Debug.Print(feat.Name + " is frozen? " + feat.IsFrozen());
             }

             Debug.Print("Press F5 to close the model.");
             System.Diagnostics.Debugger.Break();

             swApp.CloseDoc("");

         }

         public SldWorks swApp;

     }
 }
```
