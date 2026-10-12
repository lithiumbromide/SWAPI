---
title: "NeedVertexNormal Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "NeedVertexNormal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedVertexNormal.html"
---

# NeedVertexNormal Property (ITessellation)

Gets or sets the need vertex normal option.

## Syntax

### Visual Basic (Declaration)

```vb
Property NeedVertexNormal As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Boolean

instance.NeedVertexNormal = value

value = instance.NeedVertexNormal
```

### C#

```csharp
System.bool NeedVertexNormal {get; set;}
```

### C++/CLI

```cpp
property System.bool NeedVertexNormal {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True generates this information, false does not

## VBA Syntax

See [Tessellation::NeedVertexNormal](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~NeedVertexNormal.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
