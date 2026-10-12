---
title: "AddVariablePitchHelixSegment Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "AddVariablePitchHelixSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment.html"
---

# AddVariablePitchHelixSegment Method (IFeatureManager)

Adds a segment to a variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddVariablePitchHelixSegment( _
   ByVal Height As System.Double, _
   ByVal Diameter As System.Double, _
   ByVal Pitch As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Height As System.Double
Dim Diameter As System.Double
Dim Pitch As System.Double
Dim value As System.Boolean

value = instance.AddVariablePitchHelixSegment(Height, Diameter, Pitch)
```

### C#

```csharp
System.bool AddVariablePitchHelixSegment(
   System.double Height,
   System.double Diameter,
   System.double Pitch
)
```

### C++/CLI

```cpp
System.bool AddVariablePitchHelixSegment(
   System.double Height,
   System.double Diameter,
   System.double Pitch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Height`: Helix segment revolution; 1.0 = 360 degrees
- `Diameter`: Diameter, which determines how far the variable-pitch helix segment extends
- `Pitch`: Pitch, which determines the width of one complete helix turn, measured parallel to the axis of the helix

### Return Value

True if the variable-pitch helix segment is added, false if not

## VBA Syntax

See [FeatureManager::AddVariablePitchHelixSegment](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~AddVariablePitchHelixSegment.html).

## Examples

[Create Variable-pitch Helix (C#)](Create_Variable_Pitch_Helix_Example_CSharp.htm)
[Create Variable-pitch Helix (VB.NET)](Create_Variable_Pitch_Helix_Example_VBNET.htm)
[Create Variable-pitch Helix (VBA)](Create_Variable_Pitch_Helix_Example_VB.htm)
[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## Remarks

To create and insert a variable-pitch helix, call:

1. [IFeatureManager::InsertVariablePitchHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.html) to create it.
2. [IFeatureManager::AddVariablePitchHelixFirstPitchAndDiameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.html) to add the first segment.
3. IFeatureManager::AddVariablePitchHelixSegment one or more times to add the remaining segments.
4. [IFeatureManager::EndVariablePitchHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.html) to insert it.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
