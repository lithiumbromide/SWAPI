---
title: "Move Freeze Bar Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Freeze_Bar_Example_VB.htm"
---

# Move Freeze Bar Example (VBA)

This example shows how to move the freeze bar to another location in the
FeatureManager design tree.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\FreezeBarNeedsRebuild2.sldprt.
 ' 2. Inspect the FeatureManager design tree:
 '    * The rebuild indicator is displayed in the FeatureManager design tree.
 '    * The freeze bar is below Boss-Extrude1 in the FeatureManager design tree.
 '    * Boss-Extrude1 is frozen in the FeatureManager design tree.
 '    * Boss-Extrude2 is unfrozen in the FeatureManager design tree.
 '    * Boss-Extrude1 has freeze updates pending.
 '    * Boss-Extrude2 has no freeze updates pending.
 '    * The model needs to be rebuilt.
 '
 ' Postconditions:
 ' 1. Removes the rebuild indicator from the part.
 ' 2. Inspect the Immediate window to see which features have hidden locks.
 ' 3. Press F5 to continue.
 '    * Freeze bar moved to the top of the FeatureManager design tree.
 '    * Boss-Extrude1 is unfrozen.
 ' 4. Press F5 to continue.
 '    * Freeze bar moved to the bottom of the FeatureManager design tree.
 '    * Boss-Extrude1 and Boss-Extrude2 are frozen.
 ' 5. Press F5 to continue.
 '    * Freeze bar moved to after Boss-Extrude2.
 '    * Boss-Extrude1 and Boss-Extrude2 are frozen.
 ' 6. Press F5 to continue.
 '    * Freeze bar moved to the top of the FeatureManager design tree.
 '    * Boss-Extrude1 and Boss-Extrude2 are unfrozen.
 ' 7. Press F5 to continue.
 '    * The model does not need to be rebuilt.
 '    * Boss-Extrude1 and Boss-Extrude2 have no freeze updates pending.
 ' 8. Press F5 to close the model.
 ' 9. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 ' ---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModDocExt As SldWorks.ModelDocExtension
 Dim lRet As Long
 Dim featMgr As SldWorks.FeatureManager
 Dim selMgr As SldWorks.SelectionMgr
 Dim featFrozen As SldWorks.Feature
 Dim featUnFrozen As SldWorks.Feature
 Dim feat As SldWorks.Feature
 Dim boolstatus As Boolean
 Dim bRetVal As Boolean
 Dim vfeats As Variant
 Dim vfeat As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModDocExt = swModel.Extension
     Set featMgr = swModel.FeatureManager
     Set selMgr = swModel.SelectionManager
    swApp.SetUserPreferenceToggle swUserEnableFreezeBar, True
     swModDocExt.ShowPartRebuildIndicators = False
    Debug.Print "Number of Features is " & swModel.GetFeatureCount

    vfeats = featMgr.GetFeatures(True)

    For Each vfeat In vfeats
         Set feat = vfeat
         Debug.Print "Feature name from FeatureManager design tree is " & feat.Name
         Debug.Print feat.Name & " has a hidden lock? " & feat.IsHiddenLock
     Next

    boolstatus = swModDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     boolstatus = swModDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, True, 0, Nothing, 0)

    Set feat = featMgr.GetFreezeLocation
     If Not feat Is Nothing Then
         Debug.Print ""
         Debug.Print "Freeze bar location is after " & feat.Name
         Debug.Print feat.Name & " is frozen? " & feat.IsFrozen
     End If

    lRet = swModDocExt.NeedsRebuild2
     Debug.Print "Needs rebuild? " & lRet

    Set featFrozen = selMgr.GetSelectedObject6(1, -1)
     Debug.Print "Feature " & featFrozen.Name & " has freeze updates pending? " & featFrozen.HasFrozenUpdatePending
     Set featUnFrozen = selMgr.GetSelectedObject6(2, -1)
     Debug.Print "Feature " & featUnFrozen.Name & " has freeze updates pending? " & featUnFrozen.HasFrozenUpdatePending
     Debug.Print ""

    swModel.ClearSelection2 True

    Stop

    If (featFrozen.HasFrozenUpdatePending) Then
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToBeforeFeature, featFrozen.Name, True, True)
         Debug.Print "Freeze bar moved to the top of the FeatureManager design tree. Press F5."
         Stop
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToEnd, "", True, True)
         Debug.Print "Freeze bar moved to the bottom of the FeatureManager design tree. Press F5."
         Stop
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToAfterFeature, featUnFrozen.Name, True, True)
         Debug.Print "Freeze bar moved to after Boss-Extrude2. Press F5."
         Stop
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToTop, "", True, True)
         Debug.Print "Freeze bar moved to the top of the FeatureManager design tree. Press F5."
         Stop
     Else
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToBeforeFeature, featFrozen.Name, True, True)
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToEnd, "", True, True)
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToBeforeFeature, featUnFrozen.Name, True, True)
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToAfterFeature, featUnFrozen.Name, True, True)
         lRet = featMgr.EditFreeze2(swMoveFreezeBarToTop, "", True, True)
     End If

    Debug.Print ""
     lRet = swModDocExt.NeedsRebuild2
     Debug.Print "Needs rebuild? " & lRet

    Debug.Print "Feature " & featFrozen.Name & " has freeze updates pending? " & featFrozen.HasFrozenUpdatePending
     Debug.Print "Feature " & featUnFrozen.Name & " has freeze updates pending? " & featUnFrozen.HasFrozenUpdatePending

    Set feat = featMgr.GetFreezeLocation ' feat = Nothing if freeze bar is at the top of FeatureManager design tree
     If Not feat Is Nothing Then
         Debug.Print feat.Name & " is frozen?" & feat.IsFrozen
     End If

    Debug.Print "Press F5 to close the model."
     Stop

    swApp.CloseDoc ("")
End Sub
```
