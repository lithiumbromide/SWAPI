---
title: "IsDirection2Specified Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "IsDirection2Specified"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IsDirection2Specified.html"
---

# IsDirection2Specified Method (ILinearPatternFeatureData)

Gets whether direction 2 is specified for this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDirection2Specified() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean

value = instance.IsDirection2Specified()
```

### C#

```csharp
System.bool IsDirection2Specified()
```

### C++/CLI

```cpp
System.bool IsDirection2Specified();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if direction 2 is specified, false if not

## VBA Syntax

See [LinearPatternFeatureData::IsDirection2Specified](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~IsDirection2Specified.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD2AxisType.html)
[ILinearPatternFeatureData::D2Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Axis.html)
[ILinearPatternFeatureData::D2PatternSeedOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2PatternSeedOnly.html)
[ILinearPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2ReverseDirection.html)
[ILinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Spacing.html)
[ILinearPatternFeatureData::D2TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2TotalInstances.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
