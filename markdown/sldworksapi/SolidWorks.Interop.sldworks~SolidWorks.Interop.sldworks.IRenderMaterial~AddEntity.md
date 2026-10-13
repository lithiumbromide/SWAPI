---
title: "AddEntity Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "AddEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AddEntity.html"
---

# AddEntity Method (IRenderMaterial)

Adds the appearance to the specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddEntity( _
   ByVal Entity As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim Entity As System.Object
Dim value As System.Boolean

value = instance.AddEntity(Entity)
```

### C#

```csharp
System.bool AddEntity(
   System.object Entity
)
```

### C++/CLI

```cpp
System.bool AddEntity(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: Entity to which to add the appearance

### Return Value

True if the appearance is added to Entity, false if not

## VBA Syntax

See [RenderMaterial::AddEntity](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~AddEntity.html).

## Examples

See [IRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) examples.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntities.html)
[IRenderMaterial::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntitiesCount.html)
[IRenderMaterial::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IGetEntities.html)
[IRenderMaterial::RemoveAllEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RemoveAllEntities.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
