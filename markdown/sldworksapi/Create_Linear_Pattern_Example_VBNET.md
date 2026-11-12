---
title: "Create Linear Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Linear_Pattern_Example_VBNET.htm"
---

# Create Linear Pattern Example (VB.NET)

This example shows how to create a linear-pattern feature using an offset reference.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\varyinstance.sldprt.
 '
 ' Postconditions: Creates LPattern1 in the FeatureManager design tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
```

```vb
Imports
```

SolidWorks.Interop.sldworks

```vb
Imports
```

SolidWorks.Interop.swconst

```vb
Imports
```

System.Runtime.InteropServices

```vb
Imports
```

System

```vb
Partial
```

Class

SolidWorksMacro

Dim Part As

ModelDoc2

Dim myFeature As

Feature

Dim boolstatus As Boolean

Sub

main()

```vb
Part = swApp.ActiveDoc
```

' Select feature to pattern

```vb
boolstatus = Part.Extension.SelectByID2(
```

"Cut-Extrude1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing

, swSelectOption_e.swSelectOptionDefault)

' Select Direction 1 reference

```vb
boolstatus = Part.Extension.SelectByID2(
```

"", "EDGE", -0.000143804142453519, 0.0690197499537817, 0.0370101655861568, True, 1, Nothing

, swSelectOption_e.swSelectOptionDefault)

' Select Direction 2 reference

```vb
boolstatus = Part.Extension.SelectByID2(
```

"", "EDGE", 0.00000850674319963218, -0.0507775663234327, 0.14947002782122, True, 2, Nothing

, swSelectOption_e.swSelectOptionDefault)

' Select face from which to offset the pattern's furthest instance in Direction 1

```vb
boolstatus = Part.Extension.SelectByID2(
```

"", "FACE", 0.00799245561853468, -0.0329718247828055, -0.0491565136701766, True, 2097152, Nothing

, swSelectOption_e.swSelectOptionDefault)

' Select seed instance edge with which to measure distances between pattern instances

```vb
boolstatus = Part.Extension.SelectByID2(
```

"", "EDGE", 0.0114738185224041, 0.00104517477574007, -0.0334013867415592, True, 8388608, Nothing

, swSelectOption_e.swSelectOptionDefault)

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

```vb
' * DName2 (not used)
```

' * False (GeometryPattern)

' * False (VaryInstance)

' * True (HasOffset1)

' * HasOffset2 (not used)

' * True (CtrlByNum1; control pattern instance spacing in Direction 1

' using number of instances instead of spacing)

' * CtrlByNum2(not used)

' * False (FromCentroid1; measure distances between pattern instances in

' Direction 1 using the selected pattern seed edge marked with

' 8388608)

' * FromCentroid2 (not used)

' * False (RevOffset1; do not reverse Offset1)

' * False (RevOffset2; do not reverse Offset2)

' * 0.l9 (Offset1; furthest instance in Direction 1 is offset by 190 mm

' from the selected face marked with 2097152)

' * Offset2 (not used)

'

```vb
myFeature = Part.FeatureManager.FeatureLinearPattern4( _
3, _
0.0029375, _
4, _
0.02, _
```

True

, _

True

, _

"", _

```vb
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

Public swApp As

SldWorks

```vb
End
```

Class
