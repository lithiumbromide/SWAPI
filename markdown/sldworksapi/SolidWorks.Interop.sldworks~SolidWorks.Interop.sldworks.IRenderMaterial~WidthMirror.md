---
title: "WidthMirror Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "WidthMirror"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~WidthMirror.html"
---

# WidthMirror Property (IRenderMaterial)

Gets or sets whether to flip the appearance texture about the selected direction horizontally.

## Syntax

### Visual Basic (Declaration)

```vb
Property WidthMirror As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.WidthMirror = value

value = instance.WidthMirror
```

### C#

```csharp
System.bool WidthMirror {get; set;}
```

### C++/CLI

```cpp
property System.bool WidthMirror {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the appearance texture about the selected direction horizontally, false to not

## VBA Syntax

See [RenderMaterial::WidthMirror](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~WidthMirror.html).

## Remarks

Call [IRenderMaterial::HeightMirror](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~HeightMirror.html) to flip the appearance texture about the selected direction vertically.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
