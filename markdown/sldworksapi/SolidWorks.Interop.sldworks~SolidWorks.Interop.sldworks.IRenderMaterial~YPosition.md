---
title: "YPosition Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "YPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~YPosition.html"
---

# YPosition Property (IRenderMaterial)

Gets or sets the Y offset direction for the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property YPosition As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.YPosition = value

value = instance.YPosition
```

### C#

```csharp
System.double YPosition {get; set;}
```

### C++/CLI

```cpp
property System.double YPosition {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Y offset direction

## VBA Syntax

See [RenderMaterial::YPosition](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~YPosition.html).

## Remarks

This property offsets the appearance from its original position.

Call [IRenderMaterial::XPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~XPosition.html) to set the X coordinate for the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
