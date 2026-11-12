---
title: "CapPlanar Property (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "CapPlanar"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~CapPlanar.html"
---

# CapPlanar Property (IIntersectFeatureData)

Gets or sets whether to close the flat openings of surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Property CapPlanar As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim value As System.Boolean

instance.CapPlanar = value

value = instance.CapPlanar
```

### C#

```csharp
System.bool CapPlanar {get; set;}
```

### C++/CLI

```cpp
property System.bool CapPlanar {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to close the flat openings, false to not

## VBA Syntax

See [IntersectFeatureData::CapPlanar](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~CapPlanar.html).

## Examples

See the [IIntersectFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData.html) examples.

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
