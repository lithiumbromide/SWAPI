---
title: "GetNamedEntitiesCount Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetNamedEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html"
---

# GetNamedEntitiesCount Method (IPartDoc)

Gets the number of named entities (face, edge, vertex, and so on) in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNamedEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Integer

value = instance.GetNamedEntitiesCount()
```

### C#

```csharp
System.int GetNamedEntitiesCount()
```

### C++/CLI

```cpp
System.int GetNamedEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of named entities

## VBA Syntax

See [PartDoc::GetNamedEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetNamedEntitiesCount.html).

## Examples

[Get Named Entities (C++)](Get_Named_Entities_Example_CPlusPlus_COM.htm)
[Get Named Entities (VBA)](Get_Named_Entities_Example_VB.htm)

## Remarks

Call this method before calling [IPartDoc::IGetNamedEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IGetNamedEntities.html) to determine the size of that method's array.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html)
[IPartDoc::SetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
