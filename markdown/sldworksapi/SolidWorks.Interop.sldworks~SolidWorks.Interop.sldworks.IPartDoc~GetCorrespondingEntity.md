---
title: "GetCorrespondingEntity Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetCorrespondingEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetCorrespondingEntity.html"
---

# GetCorrespondingEntity Method (IPartDoc)

Obsolete. Superseded by [IModelDocExtension::GetCorrespondingEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorrespondingEntity( _
   ByVal Entity As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Entity As System.Object
Dim value As System.Object

value = instance.GetCorrespondingEntity(Entity)
```

### C#

```csharp
System.object GetCorrespondingEntity(
   System.object Entity
)
```

### C++/CLI

```cpp
System.Object^ GetCorrespondingEntity(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`:

## VBA Syntax

See [PartDoc::GetCorrespondingEntity](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetCorrespondingEntity.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
