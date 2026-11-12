---
title: "IGetNamedEntities Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetNamedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html"
---

# IGetNamedEntities Method (IPartDoc)

Gets an array of names of named entities (face, edge, vertex, and so on) in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNamedEntities( _
   ByVal Count As System.Integer _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Count As System.Integer
Dim value As Entity

value = instance.IGetNamedEntities(Count)
```

### C#

```csharp
Entity IGetNamedEntities(
   System.int Count
)
```

### C++/CLI

```cpp
Entity^ IGetNamedEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of named entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of named [entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Get Named Entities (C++)](Get_Named_Entities_Example_CPlusPlus_COM.htm)

## Remarks

Call [IPartDoc::GetNamedEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html) before calling this method to get Count.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IPartDoc::GetNamedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html)
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.html)
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html)
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)
[IPartDoc::SetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.html)
