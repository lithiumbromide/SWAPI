---
title: "GetEntities Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntities.html"
---

# GetEntities Method (IRenderMaterial)

Gets the entities on which this appearance is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntities() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Object

value = instance.GetEntities()
```

### C#

```csharp
System.object GetEntities()
```

### C++/CLI

```cpp
System.Object^ GetEntities();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of entities on which this appearance is applied

## VBA Syntax

See [RenderMaterial::GetEntities](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetEntities.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IGetEntities.html)
[IRenderMaterial::AddEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AddEntity.html)
[IRenderMaterial::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntitiesCount.html)
[IRenderMaterial::RemoveAllEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RemoveAllEntities.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
