---
title: "AddVariablePitchHelixFirstPitchAndDiameter Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "AddVariablePitchHelixFirstPitchAndDiameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.html"
---

# AddVariablePitchHelixFirstPitchAndDiameter Method (IFeatureManager)

Adds the first segment to a variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddVariablePitchHelixFirstPitchAndDiameter( _
   ByVal FirstPitch As System.Double, _
   ByVal FirstDiameter As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FirstPitch As System.Double
Dim FirstDiameter As System.Double
Dim value As System.Boolean

value = instance.AddVariablePitchHelixFirstPitchAndDiameter(FirstPitch, FirstDiameter)
```

### C#

```csharp
System.bool AddVariablePitchHelixFirstPitchAndDiameter(
   System.double FirstPitch,
   System.double FirstDiameter
)
```

### C++/CLI

```cpp
System.bool AddVariablePitchHelixFirstPitchAndDiameter(
   System.double FirstPitch,
   System.double FirstDiameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstPitch`: Pitch, which determines the width of one complete helix turn, measured parallel to the axis of the helix
- `FirstDiameter`: Diameter, which determines how far the variable-pitch helix segment extends

### Return Value

True if the first segment of the helix is added, false if not

## VBA Syntax

See [FeatureManager::AddVariablePitchHelixPatchAndDiameter](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.html).

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
2. IFeatureManager::AddVariablePitchHelixFirstPitchAndDiamenter to add the first segment.
3. [IFeatureManager::AddVariablePitchHelixSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment.html) one or more times to add the remaining segments.
4. [IFeatureManager::EndVariablePitchHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.html) to insert it.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
