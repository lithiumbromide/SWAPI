---
title: "SetRegionParameterAtIndex Method (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "SetRegionParameterAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.html"
---

# SetRegionParameterAtIndex Method (IHelixFeatureData)

Sets the specified parameter for the specified region in this variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRegionParameterAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Parameter As System.Integer, _
   ByVal PitchValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim Index As System.Integer
Dim Parameter As System.Integer
Dim PitchValue As System.Double
Dim value As System.Integer

value = instance.SetRegionParameterAtIndex(Index, Parameter, PitchValue)
```

### C#

```csharp
System.int SetRegionParameterAtIndex(
   System.int Index,
   System.int Parameter,
   System.double PitchValue
)
```

### C++/CLI

```cpp
System.int SetRegionParameterAtIndex(
   System.int Index,
   System.int Parameter,
   System.double PitchValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the region
- `Parameter`: Region parameter as defined in [swVariablePitchHelixRegionParameter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVariablePitchHelixRegionParameter_e.html) (see **Remarks**)
- `PitchValue`: Region parameter value

### Return Value

Status of setting region parameters as defined in [swSetHelixRegionParameterStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetHelixRegionParameterStatus_e.html)

## VBA Syntax

See [HelixFeatureData::SetRegionParameterAtIndex](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~SetRegionParameterAtIndex.html).

## Examples

[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## Remarks

| If the helix is defined as... | Then you cannot change... |
| --- | --- |
| swHelixDefinedBy_e.swHelixDefinedByHeightAndPitch | Revolution value |
| swHelixDefinedBy_e.swHelixDefinedByHeightAndRevolution | Pitch value |
| swHelixDefinedBy_e.swHelixDefinedByPitchAndRevolution | Height value |

| If setting a value for... | Then you... |
| --- | --- |
| Revolution | Must specify a value greater than the previous region's revolution value and less than the next region's revolution value |
| Pitch for the first region only | Cannot change diameter, height, or revolution |

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.html)
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.html)
[IHelixFeatureData::GetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.html)
[IHelixFeatureData::InsertRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.html)
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.html)
[IHelixFeatureData::AddLastRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
