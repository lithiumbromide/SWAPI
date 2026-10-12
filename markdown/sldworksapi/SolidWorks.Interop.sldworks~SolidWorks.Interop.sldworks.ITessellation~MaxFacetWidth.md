---
title: "MaxFacetWidth Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "MaxFacetWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MaxFacetWidth.html"
---

# MaxFacetWidth Property (ITessellation)

Gets or sets the maximum width of any side of a facet.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxFacetWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Double

instance.MaxFacetWidth = value

value = instance.MaxFacetWidth
```

### C#

```csharp
System.double MaxFacetWidth {get; set;}
```

### C++/CLI

```cpp
property System.double MaxFacetWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum facet width

## VBA Syntax

See [Tessellation::MaxFacetWidth](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~MaxFacetWidth.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::MinFacetWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MinFacetWidth.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
