---
title: "DeleteEntityName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "DeleteEntityName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.html"
---

# DeleteEntityName Method (IPartDoc)

Deletes the name associated with the specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteEntityName( _
   ByVal Entity As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Entity As System.Object
Dim value As System.Boolean

value = instance.DeleteEntityName(Entity)
```

### C#

```csharp
System.bool DeleteEntityName(
   System.object Entity
)
```

### C++/CLI

```cpp
System.bool DeleteEntityName(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) whose name to remove

### Return Value

True if the name is removed successfully, false if not

## VBA Syntax

See [PartDoc::DeleteEntityName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~DeleteEntityName.html).

## Examples

[Get Entity By Name (VBA)](Get_Entity_By_Name_Example.htm)

## Remarks

Deleting an entity name can cause references to fail.

For example, if an assembly contains a mate to a part face, then a name may automatically be assigned to that face. If you delete that name, then there is no guarantee that the mate will still be valid. This method was provided because the action is available in the core product. However, you should recognize the possibility of reference failures as just described.

Entity names are kept with the part document, so this method resides on the [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) object.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IPartDoc::GetNamedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html)
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html)
[IPartDoc::SetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)

## Availability

SOLIDWORKS 99, datecode 1999207
