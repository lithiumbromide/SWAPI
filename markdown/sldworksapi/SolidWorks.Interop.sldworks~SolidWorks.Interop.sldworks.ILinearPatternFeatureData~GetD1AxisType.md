---
title: "GetD1AxisType Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "GetD1AxisType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD1AxisType.html"
---

# GetD1AxisType Method (ILinearPatternFeatureData)

Gets the type of geometry used to determine Direction 1 of this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetD1AxisType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Integer

value = instance.GetD1AxisType()
```

### C#

```csharp
System.int GetD1AxisType()
```

### C++/CLI

```cpp
System.int GetD1AxisType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Geometry type used to create the linear pattern in Direction 1:

- 0 = axis or ref axis
- 1 = edge
- 2 = dimension
- 3 = sketch segment

## VBA Syntax

See [LinearPatternFeatureData::GetD1AxisType](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~GetD1AxisType.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.html)
[ILinearPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.html)
[ILinearPatternFeatureData::D1TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.html)
[ILinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD2AxisType.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
