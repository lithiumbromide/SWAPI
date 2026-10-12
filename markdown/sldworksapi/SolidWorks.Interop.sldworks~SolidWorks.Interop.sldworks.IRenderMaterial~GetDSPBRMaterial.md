---
title: "GetDSPBRMaterial Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetDSPBRMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetDSPBRMaterial.html"
---

# GetDSPBRMaterial Method (IRenderMaterial)

Gets the DSPBRMaterial object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDSPBRMaterial() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Object

value = instance.GetDSPBRMaterial()
```

### C#

```csharp
System.object GetDSPBRMaterial()
```

### C++/CLI

```cpp
System.Object^ GetDSPBRMaterial();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IDSPBRMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)

## VBA Syntax

See [RenderMaterial::GetDSPBRMaterial](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetDSPBRMaterial.html).

## Remarks

This method is valid only if [IRenderMaterial::HasDSPBRProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HasDSPBRProperties.html) is true.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
