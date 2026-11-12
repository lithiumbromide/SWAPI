---
title: "D1TotalInstances Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1TotalInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1TotalInstances.html"
---

# D1TotalInstances Property (ILocalLinearPatternFeatureData)

Gets or sets the total number of instances in Direction 1, including skipped items, in this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1TotalInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Integer

instance.D1TotalInstances = value

value = instance.D1TotalInstances
```

### C#

```csharp
System.int D1TotalInstances {get; set;}
```

### C++/CLI

```cpp
property System.int D1TotalInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of total instances in Direction 1

## VBA Syntax

See [LocalLinearPatternFeatureData::D1TotalInstances](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1TotalInstances.html).

## Examples

See the [ILocalLinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html) example.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD1AxisType.html)
[ILocalLinearPatternFeatureData::D1Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Axis.html)
[ILocalLinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1ReverseDirection.html)
[ILocalLinearPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Spacing.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
