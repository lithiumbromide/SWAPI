---
title: "TranslateSurface Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "TranslateSurface"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~TranslateSurface.html"
---

# TranslateSurface Property (ISimpleHoleFeatureData2)

Gets or sets whether to translate the surface of this simple hole.

## Syntax

### Visual Basic (Declaration)

```vb
Property TranslateSurface As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Boolean

instance.TranslateSurface = value

value = instance.TranslateSurface
```

### C#

```csharp
System.bool TranslateSurface {get; set;}
```

### C++/CLI

```cpp
property System.bool TranslateSurface {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to translate the surface of this simple hole, false to not

## VBA Syntax

See [SimpleHoleFeatureData2::TranslateSurface](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~TranslateSurface.html).

## Remarks

To use a true offset, this property should be false.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::SurfaceOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SurfaceOffset.html)
[ISimpleHoleFeatureData2::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReverseOffset.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
