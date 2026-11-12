---
title: "Create Linear Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Linear_Pattern_Example_VB.htm"
---

# Create Linear Pattern Example (VBA)

This example shows how to create a linear-pattern feature using an offset reference.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\varyinstance.sldprt.
 '
 ' Postconditions: Creates LPattern1 in the FeatureManager design tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myFeature As SldWorks.Feature
 Dim boolstatus As Boolean
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    ' Select feature to pattern
     boolstatus = Part.Extension.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, swSelectOptionDefault)

    ' Select Direction 1 reference
     boolstatus = Part.Extension.SelectByID2("", "EDGE", -1.43804142453519E-04, 6.90197499537817E-02, 3.70101655861568E-02, True, 1, Nothing, swSelectOptionDefault)

    ' Select Direction 2 reference
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 8.50674319963218E-06, -5.07775663234327E-02, 0.14947002782122, True, 2, Nothing, swSelectOptionDefault)

    ' Select face from which to offset the pattern's furthest instance in Direction 1
     boolstatus = Part.Extension.SelectByID2("", "FACE", 7.99245561853468E-03, -3.29718247828055E-02, -4.91565136701766E-02, True, 2097152, Nothing, swSelectOptionDefault)

    ' Select seed instance edge with which to measure distances between pattern instances
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 1.14738185224041E-02, 1.04517477574007E-03, -3.34013867415592E-02, True, 8388608, Nothing, swSelectOptionDefault)

    ' Create linear-pattern feature calling IFeatureManager::FeatureLinearPattern4
     ' with the following parameter information:
     '
     ' * 3 (Num1)
     ' * Spacing1 (not used)
     ' * 4 (Num2)
     ' * 0.02 (Spacing2 in mm)
     ' * True (FlipDir1)
     ' * True (FlipDir2)
     ' * DName1 (not used)
     ' * DName2 (not used)
     ' * False (GeometryPattern)
     ' * False (VaryInstance)
     ' * True (hasOffset1)
     ' * HasOffset2 (not used)
     ' * True (CtrlByNum1; control pattern instance spacing in Direction 1
     '         using number of instances instead of spacing)
     ' * CtrlByNum2(not used)
     ' * False (FromCentroid1; measure distances between pattern instances in
     '          Direction 1 using the selected pattern seed edge marked with
     '          8388608)
     ' * FromCentroid2 (not used)
     ' * False (RevOffset1; do not reverse Offset1)
     ' * False (RevOffset2; do not reverse Offset2)
     ' * 0.l9 (Offset1; furthest instance in Direction 1 is offset by 190 mm
     '         from the selected face marked with 2097152)
     ' * Offset2 (not used)
     '
     Set myFeature = Part.FeatureManager.FeatureLinearPattern4( _
     3, _
     0.0029375, _
     4, _
     0.02, _
     True, _
     True, _
     "", _
     "", _
     False, _
     False, _
     True, _
     False, _
     True, _
     False, _
     False, _
     True, _
     False, _
     False, _
     0.19, _
     0.01 _
     )
End Sub
```
