---
title: "InsertVariablePitchHelix Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertVariablePitchHelix"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.html"
---

# InsertVariablePitchHelix Method (IFeatureManager)

Starts a variable-pitch helix using the selected sketch containing an arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertVariablePitchHelix( _
   ByVal Reversed As System.Boolean, _
   ByVal Clockwise As System.Boolean, _
   ByVal Helixdef As System.Integer, _
   ByVal Startangle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Reversed As System.Boolean
Dim Clockwise As System.Boolean
Dim Helixdef As System.Integer
Dim Startangle As System.Double
Dim value As System.Boolean

value = instance.InsertVariablePitchHelix(Reversed, Clockwise, Helixdef, Startangle)
```

### C#

```csharp
System.bool InsertVariablePitchHelix(
   System.bool Reversed,
   System.bool Clockwise,
   System.int Helixdef,
   System.double Startangle
)
```

### C++/CLI

```cpp
System.bool InsertVariablePitchHelix(
   System.bool Reversed,
   System.bool Clockwise,
   System.int Helixdef,
   System.double Startangle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reversed`: True to reverse the variable-pitch helix, false to not
- `Clockwise`: True to create the variable-pitch helix in a clockwise direction, false to create in a counter-clockwise direction
- `Helixdef`: Definition of variable-pitch helix as defined in [swHelixDefinedBy_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHelixDefinedBy_e.html); valid enumerators are:

  - swHelixDefinedByPitchAndRevolution
  - swHelixDefinedByHeightandRevolution
  - swHelixDefinedByHeightAndPitch
- `Startangle`: Angle at which to start the variable-pitch helix

### Return Value

True if the variable-pitch helix is started, false if not

## VBA Syntax

See [FeatureManager::InsertVariablePitchHelix](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertVariablePitchHelix.html).

## Examples

[Create Variable-pitch Helix (C#)](Create_Variable_Pitch_Helix_Example_CSharp.htm)
[Create Variable-pitch Helix (VB.NET)](Create_Variable_Pitch_Helix_Example_VBNET.htm)
[Create Variable-pitch Helix (VBA)](Create_Variable_Pitch_Helix_Example_VB.htm)
[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## Remarks

To create and insert a variable-pitch helix, call:

1. IFeatureManager::InsertVariablePitchHelix to create it.
2. [IFeatureManager::AddVariablePitchHelixFirstPitchAndDiamenter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.html) to add the first segment.
3. [IFeatureManager::AddVariablePitchHelixSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment.html) one or more times to add the remaining segments.
4. [IFeatureManager::EndVariablePitchHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.html) to insert it.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
