---
title: "D2TotalInstances Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D2TotalInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2TotalInstances.html"
---

# D2TotalInstances Property (ILocalLinearPatternFeatureData)

Gets or sets the total number of instances in Direction 2, including skipped items, in this bidirectional linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2TotalInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Integer

instance.D2TotalInstances = value

value = instance.D2TotalInstances
```

### C#

```csharp
System.int D2TotalInstances {get; set;}
```

### C++/CLI

```cpp
property System.int D2TotalInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of total instances in Direction 2

## VBA Syntax

See [LocalLinearPatternFeatureData::D2TotalInstances](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D2TotalInstances.html).

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
[ILocalLinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Spacing.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
