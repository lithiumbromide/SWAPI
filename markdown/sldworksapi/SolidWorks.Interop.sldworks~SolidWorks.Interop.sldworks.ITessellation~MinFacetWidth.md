---
title: "MinFacetWidth Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "MinFacetWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MinFacetWidth.html"
---

# MinFacetWidth Property (ITessellation)

Gets or sets the minimum facet width for this tessellation.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinFacetWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Double

instance.MinFacetWidth = value

value = instance.MinFacetWidth
```

### C#

```csharp
System.double MinFacetWidth {get; set;}
```

### C++/CLI

```cpp
property System.double MinFacetWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum tessellation width

## VBA Syntax

See [Tessellation::MinFacetWidth](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~MinFacetWidth.html).

## Remarks

The default value for the underlying modeler is used when tessellating.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::MaxFacetWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MaxFacetWidth.html)

## Availability

SolidWork s2001Plus FCS, Revision Number 10.0
