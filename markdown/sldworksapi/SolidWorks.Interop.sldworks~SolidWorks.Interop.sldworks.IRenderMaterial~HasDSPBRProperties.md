---
title: "HasDSPBRProperties Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "HasDSPBRProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HasDSPBRProperties.html"
---

# HasDSPBRProperties Property (IRenderMaterial)

Gets whether this appearance has DSPBR properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasDSPBRProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

value = instance.HasDSPBRProperties
```

### C#

```csharp
System.bool HasDSPBRProperties {get;}
```

### C++/CLI

```cpp
property System.bool HasDSPBRProperties {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this appearance has DSPBR properties, false if not

## VBA Syntax

See [RenderMaterial::HasDSPBRProperties](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~HasDSPBRProperties.html).

## Remarks

If this property is true, use [IRenderMaterial::GetDSPBRMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetDSPBRMaterial.html) to obtain the DSPBRMaterial object.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
