---
title: "XPosition Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "XPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~XPosition.html"
---

# XPosition Property (IRenderMaterial)

Gets or sets the X offset direction for the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property XPosition As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.XPosition = value

value = instance.XPosition
```

### C#

```csharp
System.double XPosition {get; set;}
```

### C++/CLI

```cpp
property System.double XPosition {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

X offset direction

## VBA Syntax

See [RenderMaterial::XPosition](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~XPosition.html).

## Remarks

This property offsets the appearance from its original position.

Call [IRenderMaterial::YPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~YPosition.html) to set the Y offset direction for the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
