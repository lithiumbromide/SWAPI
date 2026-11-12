---
title: "MaterialID Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "MaterialID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MaterialID.html"
---

# MaterialID Property (IRenderMaterial)

Not supported in SOLIDWORKS 2011 and later. Superseded by [IRenderMaterial::GetMaterialIds](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetMaterialIds.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MaterialID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

value = instance.MaterialID
```

### C#

```csharp
System.int MaterialID {get;}
```

### C++/CLI

```cpp
property System.int MaterialID {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Appearance ID

## VBA Syntax

See [RenderMaterial::MaterialID](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~MaterialID.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
