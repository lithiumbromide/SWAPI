---
title: "SeedFace Property (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "SeedFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~SeedFace.html"
---

# SeedFace Property (ISurfaceKnitFeatureData)

Gets or sets the seed face for this surface knit feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SeedFace As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
Dim value As System.Object

instance.SeedFace = value

value = instance.SeedFace
```

### C#

```csharp
System.object SeedFace {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SeedFace {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Seed [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SurfaceKnitFeatureData::SeedFace](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~SeedFace.html).

## Examples

[Get Knit Surface (VBA)](Get_Knit_Surface_Data_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
