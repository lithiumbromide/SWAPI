---
title: "IGetEntityName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetEntityName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html"
---

# IGetEntityName Method (IPartDoc)

Gets the name of the specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntityName( _
   ByVal Entity As Entity _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Entity As Entity
Dim value As System.String

value = instance.IGetEntityName(Entity)
```

### C#

```csharp
System.string IGetEntityName(
   Entity Entity
)
```

### C++/CLI

```cpp
System.String^ IGetEntityName(
   Entity^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

### Return Value

Name of entity

## VBA Syntax

See [PartDoc::IGetEntityName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IGetEntityName.html).

## Examples

[Get Edge Data By Name (C++)](Get_Edge_Data_By_Name_Example_CPlusPlus_COM.htm)

## Remarks

Valid for faces, edges, and vertices only.

SOLIDWORKS suggests that you use the more comprehensive method [IModelDoc2::GetEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetEntityName.html) or [IModelDoc2::IGetEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetEntityName.html) instead of this method.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IPartDoc::GetNamedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html)
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html)
[IPartDoc::SetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
