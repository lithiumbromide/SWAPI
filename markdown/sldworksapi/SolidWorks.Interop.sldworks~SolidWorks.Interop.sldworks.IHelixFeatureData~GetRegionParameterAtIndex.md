---
title: "GetRegionParameterAtIndex Method (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "GetRegionParameterAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.html"
---

# GetRegionParameterAtIndex Method (IHelixFeatureData)

Gets the specified parameter value for the specified region in this variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRegionParameterAtIndex( _
   ByVal Index As System.Integer, _
   ByVal RegionParameter As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim Index As System.Integer
Dim RegionParameter As System.Integer
Dim value As System.Double

value = instance.GetRegionParameterAtIndex(Index, RegionParameter)
```

### C#

```csharp
System.double GetRegionParameterAtIndex(
   System.int Index,
   System.int RegionParameter
)
```

### C++/CLI

```cpp
System.double GetRegionParameterAtIndex(
   System.int Index,
   System.int RegionParameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the region
- `RegionParameter`: Region parameter as defined in [swVariablePitchHelixRegionParameter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVariablePitchHelixRegionParameter_e.html)

### Return Value

Region parameter value

## VBA Syntax

See [HelixFeatureData::GetRegionParameterAtIndex](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~GetRegionParameterAtIndex.html).

## Examples

[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.html)
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.html)
[IHelixFeatureData::SetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.html)
[IHelixFeatureData::InsertRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.html)
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.html)
[IHelixFeatureData::AddLastRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
