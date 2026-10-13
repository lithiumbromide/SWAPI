---
title: "Insert Swept-cut Feature With Bidirectional Twist Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Bidirectional_Swept-cut_Feature_Example_VB.htm"
---

# Insert Swept-cut Feature With Bidirectional Twist Example (VBA)

This example shows how to create a swept-cut feature with a bidirectional twist.

```vb
 '-----------------------------------------------------------------------
 ' Preconditions: Verify that the specified part exists.
 '
 ' Postconditions:
 ' 1. Inserts a reference plane and circle sketch at a midpoint on
 '    the sweep path of the model.
 ' 2. Creates a swept-cut feature with a bidirectional twist.
 ' 3. Examine the FeatureManager design tree and graphics area.
 '
 ' Note: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSketchMgr As SldWorks.SketchManager
 Dim swSketchSegment As SldWorks.SketchSegment
 Dim swFeature As SldWorks.Feature
 Dim swPathFeat As SldWorks.Feature
 Dim swSelectionMgr As SldWorks.SelectionMgr
 Dim swSweepFeatureData As SldWorks.SweepFeatureData
 Dim swSweep As SldWorks.SweepFeatureData
 Dim swProfileObj As Object
 Dim swProfileBody As SldWorks.Body2
 Dim swPathFeature As SldWorks.Feature
 Dim myRefPlane As SldWorks.RefPlane
 Dim skSegment As SldWorks.SketchSegment
 Dim sketchLines As Variant
 Dim status As Boolean
 Dim boolstatus As Boolean
 Dim longstatus As Long
 Dim longwarnings As Long
 Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\sweepcutextrude2.SLDPRT", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "sweepcutextrude.SLDPRT", False, longstatus
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension

    boolstatus = swModel.Extension.SelectByID2("Sketch4", "SKETCH", 3.68377611840314E-02, -1.01247230141019E-02, 0, False, 1, Nothing, 0)
     boolstatus = swModel.Extension.SelectByID2("Sketch3", "SKETCH", -0.030956245593495, -0.018624786459474, 0, True, 4, Nothing, 0)

    Set swSweep = swModel.FeatureManager.CreateDefinition(swFmSweepCut)

    swSweep.Direction = 1 ' Bidirectional sweep
     swSweep.PathAlignmentType = 0
     swSweep.TwistControlType = 8
     swSweep.SetTwistAngle 31.12217 'Radians
     swSweep.D1ReverseTwistDir = False
     swSweep.SetD2TwistAngle 12.139 'Radians
     swSweep.D2ReverseTwistDir = True
     swSweep.TangentPropagation = False
     swSweep.AlignWithEndFaces = False
     swSweep.MaintainTangency = False
     swSweep.AdvancedSmoothing = False
     swSweep.StartTangencyType = 0
     swSweep.EndTangencyType = 0
     swSweep.ThinFeature = False
     swSweep.SetWallThickness True, 0#
     swSweep.SetWallThickness False, 0#
     swSweep.ThinWallType = 0
     swSweep.FeatureScope = True
     swSweep.AutoSelect = True
     swSweep.MergeSmoothFaces = True
     swSweep.AssemblyFeatureScope = True
     swSweep.AutoSelectComponents = True
     swSweep.PropagateFeatureToParts = False
     swSweep.CircularProfile = False
     swSweep.CircularProfileDiameter = 0#

    Set swPathFeat = swModel.FeatureManager.CreateFeature(swSweep)
End Sub
```
