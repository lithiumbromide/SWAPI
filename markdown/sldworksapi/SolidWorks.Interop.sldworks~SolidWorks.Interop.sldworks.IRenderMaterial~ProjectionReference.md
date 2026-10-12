---
title: "ProjectionReference Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "ProjectionReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ProjectionReference.html"
---

# ProjectionReference Property (IRenderMaterial)

Gets or sets the projection direction for mapping the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProjectionReference As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.ProjectionReference = value

value = instance.ProjectionReference
```

### C#

```csharp
System.int ProjectionReference {get; set;}
```

### C++/CLI

```cpp
property System.int ProjectionReference {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- 0 = XY

1 = ZX

2 = YZ

3 = Current View

4 = Selected Reference

## VBA Syntax

See [RenderMaterial::ProjectionReference](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~ProjectionReference.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
