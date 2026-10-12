---
title: "ImprovedQuality Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "ImprovedQuality"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~ImprovedQuality.html"
---

# ImprovedQuality Property (ITessellation)

Gets or sets whether to return higher-quality data.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImprovedQuality As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Boolean

instance.ImprovedQuality = value

value = instance.ImprovedQuality
```

### C#

```csharp
System.bool ImprovedQuality {get; set;}
```

### C++/CLI

```cpp
property System.bool ImprovedQuality {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to return higher-quality tessellation analysis data; false to return tessellation rendering data

## VBA Syntax

See [Tessellation::ImprovedQuality](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~ImprovedQuality.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## Remarks

If this property is not set, tessellation rendering data is returned by default.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
