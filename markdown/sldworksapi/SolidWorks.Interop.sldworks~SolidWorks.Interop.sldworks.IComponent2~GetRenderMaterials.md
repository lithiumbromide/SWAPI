---
title: "GetRenderMaterials Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetRenderMaterials"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials.html"
---

# GetRenderMaterials Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetRenderMaterials2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetRenderMaterials2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRenderMaterials() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetRenderMaterials()
```

### C#

```csharp
System.object GetRenderMaterials()
```

### C++/CLI

```cpp
System.Object^ GetRenderMaterials();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [appearances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See [Component2::GetRenderMaterials](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetRenderMaterials.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IGetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetRenderMaterials.html)
[IComponent2::GetRenderMaterialsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
