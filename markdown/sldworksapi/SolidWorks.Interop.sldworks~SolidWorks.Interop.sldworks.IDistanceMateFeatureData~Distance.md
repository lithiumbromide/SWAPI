---
title: "Distance Property (IDistanceMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDistanceMateFeatureData"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~Distance.html"
---

# Distance Property (IDistanceMateFeatureData)

Gets or sets the distance of this distance mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDistanceMateFeatureData
Dim value As System.Double

instance.Distance = value

value = instance.Distance
```

### C#

```csharp
System.double Distance {get; set;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between mates

## VBA Syntax

See [DistanceMateFeatureData::Distance](ms-its:sldworksapivb6.chm::/sldworks~DistanceMateFeatureData~Distance.html).

## Examples

See the [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html) examples.

## Remarks

If [IDistanceMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~IsAdvancedMate.html) is true, then this property specifies the starting distance of this mate.

## See Also

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html)
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.html)
[IDistanceMateFeatureData::MaximumDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MaximumDistance.html)
[IDistanceMateFeatureData::MinimumDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MinimumDistance.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
