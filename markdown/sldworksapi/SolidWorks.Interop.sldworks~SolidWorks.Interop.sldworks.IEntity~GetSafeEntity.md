---
title: "GetSafeEntity Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "GetSafeEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity.html"
---

# GetSafeEntity Method (IEntity)

Gets a safe entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSafeEntity() As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim value As Entity

value = instance.GetSafeEntity()
```

### C#

```csharp
Entity GetSafeEntity()
```

### C++/CLI

```cpp
Entity^ GetSafeEntity();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object

## VBA Syntax

See [Entity::GetSafeEntity](ms-its:sldworksapivb6.chm::/sldworks~Entity~GetSafeEntity.html).

## Examples

[Get Faces Affected By Scale Feature (VBA)](Get_Faces_Affected_by_Scale_Feature_Example_VB.htm)
[Use Safe Entity (VBA)](Use_Safe_Entity_Example_VB.htm)

## Remarks

A safe entity is an entity that continues to be valid after rebuilds until the pointer becomes invalid if the entity object to which it points is deleted.

To determine if an entity is safe, use the [IEntity::IsSafe](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~IsSafe.html) property. This property is read-only and does not persist from session to session.

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
[IBody2::GetSafeBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSafeBody.html)
[IBody2::IsSafe Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSafe.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
