---
title: "IGetCorrespondingEntity Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetCorrespondingEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetCorrespondingEntity.html"
---

# IGetCorrespondingEntity Method (IPartDoc)

Obsolete. Superseded by [IModelDocExtension::GetCorrespondingEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCorrespondingEntity( _
   ByVal PEntity As Entity _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim PEntity As Entity
Dim value As Entity

value = instance.IGetCorrespondingEntity(PEntity)
```

### C#

```csharp
Entity IGetCorrespondingEntity(
   Entity PEntity
)
```

### C++/CLI

```cpp
Entity^ IGetCorrespondingEntity(
   Entity^ PEntity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PEntity`:

## VBA Syntax

See [PartDoc::IGetCorrespondingEntity](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IGetCorrespondingEntity.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
