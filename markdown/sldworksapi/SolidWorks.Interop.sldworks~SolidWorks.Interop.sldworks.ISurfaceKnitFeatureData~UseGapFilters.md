---
title: "UseGapFilters Property (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "UseGapFilters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters.html"
---

# UseGapFilters Property (ISurfaceKnitFeatureData)

Gets or sets whether to use gap filters for this Surface-Knit feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseGapFilters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
Dim value As System.Boolean

instance.UseGapFilters = value

value = instance.UseGapFilters
```

### C#

```csharp
System.bool UseGapFilters {get; set;}
```

### C++/CLI

```cpp
property System.bool UseGapFilters {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use gap filters, false to not

## VBA Syntax

See [SurfaceKnitFeatureData::UseGapFilters](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~UseGapFilters.html).

## Examples

[Create Knit Surface Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)
[Create Knit Surface Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)
[Create Knit Surface Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)
[ISurfaceKnitFeatureData::KnitTolerance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance.html)
[ISurfaceKnitFeatureData::MaxValueForGapRange Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MaxValueForGapRange.html)
[ISurfaceKnitFeatureData::MinValueForGapRange Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MinValueForGapRange.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
