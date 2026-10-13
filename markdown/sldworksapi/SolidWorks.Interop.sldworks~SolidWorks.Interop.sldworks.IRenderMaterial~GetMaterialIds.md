---
title: "GetMaterialIds Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetMaterialIds"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetMaterialIds.html"
---

# GetMaterialIds Method (IRenderMaterial)

Gets the material IDs of an appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetMaterialIds( _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer

instance.GetMaterialIds(PWMaterialId1, PWMaterialId2)
```

### C#

```csharp
void GetMaterialIds(
   out System.int PWMaterialId1,
   out System.int PWMaterialId2
)
```

### C++/CLI

```cpp
void GetMaterialIds(
   [Out] System.int PWMaterialId1,
   [Out] System.int PWMaterialId2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PWMaterialId1`: First material ID
- `PWMaterialId2`: Second material ID

## VBA Syntax

See [RenderMaterial::GetMaterialIds](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetMaterialIds.html).

## Examples

See [IRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) examples.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
