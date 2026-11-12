---
title: "AddRenderMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddRenderMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddRenderMaterial.html"
---

# AddRenderMaterial Method (IModelDocExtension)

Not supported in SOLIDWORKS 2011 and later. Superseded by [IModelDocExtension::AddDisplayStateSpecificRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.html) and [IModelDocExtension::IAddDisplayStateSpecificRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRenderMaterial( _
   ByVal PRenderMaterial As RenderMaterial, _
   ByRef PwMaterialId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PRenderMaterial As RenderMaterial
Dim PwMaterialId As System.Integer
Dim value As System.Boolean

value = instance.AddRenderMaterial(PRenderMaterial, PwMaterialId)
```

### C#

```csharp
System.bool AddRenderMaterial(
   RenderMaterial PRenderMaterial,
   out System.int PwMaterialId
)
```

### C++/CLI

```cpp
System.bool AddRenderMaterial(
   RenderMaterial^ PRenderMaterial,
   [Out] System.int PwMaterialId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PRenderMaterial`: [Appearance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) to add to the model
- `PwMaterialId`: Appearance ID

### Return Value

True if the appearance is added to the model, false if not

## VBA Syntax

See [ModelDocExtension::AddRenderMaterial](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AddRenderMaterial.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
