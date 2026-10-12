---
title: "D2Spacing Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D2Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Spacing.html"
---

# D2Spacing Property (ILocalLinearPatternFeatureData)

Gets the spacing between pattern instances in Direction 2 in this bidirectional linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Double

instance.D2Spacing = value

value = instance.D2Spacing
```

### C#

```csharp
System.double D2Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double D2Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in meters between pattern instances in Direction 2

## VBA Syntax

See [LocalLinearPatternFeatureData::D2Spacing](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D2Spacing.html).

## Examples

See the [ILocalLinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html) example.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD2AxisType.html)
[ILocalLinearPatternFeatureData::D2Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Axis.html)
[ILocalLinearPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2ReverseDirection.html)
[ILocalLinearPatternFeatureData::D2TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2TotalInstances.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
