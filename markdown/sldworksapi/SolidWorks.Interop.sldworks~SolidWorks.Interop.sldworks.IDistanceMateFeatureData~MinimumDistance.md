---
title: "MinimumDistance Property (IDistanceMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDistanceMateFeatureData"
member: "MinimumDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MinimumDistance.html"
---

# MinimumDistance Property (IDistanceMateFeatureData)

Gets or sets the minimum distance of this limit distance mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinimumDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDistanceMateFeatureData
Dim value As System.Double

instance.MinimumDistance = value

value = instance.MinimumDistance
```

### C#

```csharp
System.double MinimumDistance {get; set;}
```

### C++/CLI

```cpp
property System.double MinimumDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum distance

## VBA Syntax

See [DistanceMateFeatureData::MinimumDistance](ms-its:sldworksapivb6.chm::/sldworks~DistanceMateFeatureData~MinimumDistance.html).

## Examples

See the [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html) examples.

## Remarks

This property is valid only if [IDistanceMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~IsAdvancedMate.html) is set to true.

## See Also

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html)
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.html)
[IDistanceMateFeatureData::Distance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~Distance.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
