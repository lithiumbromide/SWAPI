---
title: "FitWidth Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "FitWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FitWidth.html"
---

# FitWidth Property (IRenderMaterial)

Gets or sets whether to stretch the width of the appearance texture to the selected entity when mapping the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitWidth As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.FitWidth = value

value = instance.FitWidth
```

### C#

```csharp
System.bool FitWidth {get; set;}
```

### C++/CLI

```cpp
property System.bool FitWidth {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to stretch the width of the appearance texture to the selected entity, false to not

## VBA Syntax

See [RenderMaterial::FitWidth](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~FitWidth.html).

## Examples

See the "Add Decal" examples in [IRenderMaterial::FileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FileName.html).

## Remarks

Call [IRenderMaterial::FitHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FitHeight.html) to get or set whether to stretch the height of the appearance texture to the selected entity.

To stretch width and height of the appearance texture yourself, call [IRenderMaterial::Width](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Width.html) and [IRenderMaterial::Height](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Height.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
