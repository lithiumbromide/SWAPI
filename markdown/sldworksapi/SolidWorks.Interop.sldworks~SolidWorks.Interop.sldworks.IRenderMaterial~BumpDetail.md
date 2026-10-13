---
title: "BumpDetail Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpDetail"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpDetail.html"
---

# BumpDetail Property (IRenderMaterial)

Gets or sets the level of granularity for any surface finish for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpDetail As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.BumpDetail = value

value = instance.BumpDetail
```

### C#

```csharp
System.int BumpDetail {get; set;}
```

### C++/CLI

```cpp
property System.int BumpDetail {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Level of granularity

## VBA Syntax

See [RenderMaterial::BumpDetail](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpDetail.html).

## Remarks

This property is only available when Casting, Rough, Chips, Circular or Rough/Smooth is selected for the [surface finish](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~BumpMap.html).

When set to high detail, individual surface elements appear in sharp focus; when set to low detail, surface elements appear in soft focus.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
