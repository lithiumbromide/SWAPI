---
title: "MaxValueForGapRange Property (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "MaxValueForGapRange"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MaxValueForGapRange.html"
---

# MaxValueForGapRange Property (ISurfaceKnitFeatureData)

Gets or sets the maximum gap range for this Surface-Knit feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxValueForGapRange As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
Dim value As System.Double

instance.MaxValueForGapRange = value

value = instance.MaxValueForGapRange
```

### C#

```csharp
System.double MaxValueForGapRange {get; set;}
```

### C++/CLI

```cpp
property System.double MaxValueForGapRange {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum gap range; valid values are from 0.01 mm to 1 mm

## VBA Syntax

See [SurfaceKnitFeatureData::MaxValueForGapRange](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~MaxValueForGapRange.html).

## Examples

[Create Knit Surface Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)
[Create Knit Surface Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)
[Create Knit Surface Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

## Remarks

[ISurfaceKnitFeatureData::UseGapFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters.html) must be true for this property to have an effect.

Maximum gap should be in the range of [ISurfaceKnitFeatureData::KnitTolerance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance.html) to 1 mm.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)
[ISurfaceKnitFeatureData::MinValueForGapRange Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MinValueForGapRange.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
