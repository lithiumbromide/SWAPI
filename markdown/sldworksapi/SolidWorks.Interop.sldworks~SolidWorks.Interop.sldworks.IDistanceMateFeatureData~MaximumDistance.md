---
title: "MaximumDistance Property (IDistanceMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDistanceMateFeatureData"
member: "MaximumDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MaximumDistance.html"
---

# MaximumDistance Property (IDistanceMateFeatureData)

Gets or sets the maximum distance of this limit distance mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaximumDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDistanceMateFeatureData
Dim value As System.Double

instance.MaximumDistance = value

value = instance.MaximumDistance
```

### C#

```csharp
System.double MaximumDistance {get; set;}
```

### C++/CLI

```cpp
property System.double MaximumDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum distance

## VBA Syntax

See [DistanceMateFeatureData::MaximumDistance](ms-its:sldworksapivb6.chm::/sldworks~DistanceMateFeatureData~MaximumDistance.html).

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
