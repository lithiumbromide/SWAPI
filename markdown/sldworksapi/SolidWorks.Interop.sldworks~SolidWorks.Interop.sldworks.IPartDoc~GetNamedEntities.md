---
title: "GetNamedEntities Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetNamedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html"
---

# GetNamedEntities Method (IPartDoc)

Gets an array of names of named entities (face, edge, vertex, and so on) in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNamedEntities() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Object

value = instance.GetNamedEntities()
```

### C#

```csharp
System.object GetNamedEntities()
```

### C++/CLI

```cpp
System.Object^ GetNamedEntities();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of named [entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

## VBA Syntax

See [PartDoc::GetNamedEntities](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetNamedEntities.html).

## Examples

[Get Named Entities (VBA)](Get_Named_Entities_Example_VB.htm)

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::GetNamedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html)
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html)
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html)
[IPartDoc::SetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
