---
title: "MatchType Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "MatchType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MatchType.html"
---

# MatchType Property (ITessellation)

Gets or sets the type of Parasolid facet match for the tessellation.

## Syntax

### Visual Basic (Declaration)

```vb
Property MatchType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Integer

instance.MatchType = value

value = instance.MatchType
```

### C#

```csharp
System.int MatchType {get; set;}
```

### C++/CLI

```cpp
property System.int MatchType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of match as defined by [swTesselationMatchType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTesselationMatchType_e.html)

## VBA Syntax

See [Tessellation::MatchType](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~MatchType.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
