---
title: "TotalInstances Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "TotalInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances.html"
---

# TotalInstances Property (ILocalCircularPatternFeatureData)

Gets or sets the total number of instances in Direction 1 for this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Integer

instance.TotalInstances = value

value = instance.TotalInstances
```

### C#

```csharp
System.int TotalInstances {get; set;}
```

### C++/CLI

```cpp
property System.int TotalInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of instances in Direction 1

## VBA Syntax

See [LocalCircularPatternFeatureData::TotalInstances](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~TotalInstances.html).

## Examples

See the [ILocalCircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html) example.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing.html)
[ILocalCircularPatternFeatureData::TotalInstances2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances2.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
