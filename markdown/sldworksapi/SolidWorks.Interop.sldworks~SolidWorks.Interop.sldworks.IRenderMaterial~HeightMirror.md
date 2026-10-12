---
title: "HeightMirror Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "HeightMirror"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HeightMirror.html"
---

# HeightMirror Property (IRenderMaterial)

Gets or sets whether to flip the appearance texture about the selected direction vertically.

## Syntax

### Visual Basic (Declaration)

```vb
Property HeightMirror As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.HeightMirror = value

value = instance.HeightMirror
```

### C#

```csharp
System.bool HeightMirror {get; set;}
```

### C++/CLI

```cpp
property System.bool HeightMirror {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the appearance texture about the selected direction vertically, false to not

## VBA Syntax

See [RenderMaterial::HeightMirror](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~HeightMirror.html).

## Remarks

Call [IRenderMaterial::WidthMirror](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~WidthMirror.html) to flip the appearance texture about the selected direction horizontally.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
