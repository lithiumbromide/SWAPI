---
title: "GetEntityByName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetEntityByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html"
---

# GetEntityByName Method (IPartDoc)

Gets an entity (face, edge, vertex) by name.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityByName( _
   ByVal Name As System.String, _
   ByVal EntityType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Name As System.String
Dim EntityType As System.Integer
Dim value As System.Object

value = instance.GetEntityByName(Name, EntityType)
```

### C#

```csharp
System.object GetEntityByName(
   System.string Name,
   System.int EntityType
)
```

### C++/CLI

```cpp
System.Object^ GetEntityByName(
   System.String^ Name,
   System.int EntityType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of entity
- `EntityType`: Entity type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (see **Remarks**)

### Return Value

[Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

## VBA Syntax

See [PartDoc::GetEntityByName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetEntityByName.html).

## Examples

[Get Entity By Name (VBA)](Get_Entity_By_Name_Example.htm)

## Remarks

Valid entityType types:

- swSelFACES
- swSelEDGES
- swSelVERTICES

Another way to obtain an [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object based on its name is to traverse the body topology (for example, use [IBody2::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFirstFace.html) or [IBody2::IGetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetFirstFace.html) and so on) and use [IModelDoc2::GetEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetEntityName.html) or [IModelDoc2::IGetEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetEntityName.html) to determine when you have located the desired entity.

Because the names of entities are stored with the part document, this method resides on the [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) object.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html)
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IPartDoc::GetNamedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html)
[IPartDoc::SetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.html)
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)
