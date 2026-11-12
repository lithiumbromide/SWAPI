---
title: "GetD2AxisType Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "GetD2AxisType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD2AxisType.html"
---

# GetD2AxisType Method (ILinearPatternFeatureData)

Gets the type of geometry used to determine Direction 2 of this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetD2AxisType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Integer

value = instance.GetD2AxisType()
```

### C#

```csharp
System.int GetD2AxisType()
```

### C++/CLI

```cpp
System.int GetD2AxisType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Geometry type used to create the linear pattern in Direction 2:

- 0 = axis or ref axis
- 1 = edge
- 2 = dimension
- 3 = sketch segment

## VBA Syntax

See [LinearPatternFeatureData::GetD2AxisType](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~GetD2AxisType.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::D2PatternSeedOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2PatternSeedOnly.html)
[ILinearPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2ReverseDirection.html)
[ILinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Spacing.html)
[ILinearPatternFeatureData::D2TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2TotalInstances.html)
[ILinearPatternFeatureData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD1AxisType.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
