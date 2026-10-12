---
title: "KnitTolerance Property (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "KnitTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance.html"
---

# KnitTolerance Property (ISurfaceKnitFeatureData)

Gets or sets the knit tolerance for this Surface-Knit feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property KnitTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
Dim value As System.Double

instance.KnitTolerance = value

value = instance.KnitTolerance
```

### C#

```csharp
System.double KnitTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double KnitTolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Knit tolerance (see **Remarks**)

## VBA Syntax

See [SurfaceKnitFeatureData::KnitTolerance](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~KnitTolerance.html).

## Examples

[Create Knit Surface Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)
[Create Knit Surface Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)
[Create Knit Surface Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

## Remarks

[ISurfaceKnitFeatureData::UseGapFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters.html) must be true for this property to have an effect.

A knit tolerance's:

- lower limit is 0.0001 mm
- upper limit is 0.1 mm

The knit tolerance value should be in a gap range such that:

([Minimum gap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~MinValueForGapRange.html)) <= (Knit tolerance) <= MIN(0.1 mm, [Maximum gap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~MaxValueForGapRange.html))

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
