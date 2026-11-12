---
title: "IsSafe Property (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "IsSafe"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IsSafe.html"
---

# IsSafe Property (IEntity)

Gets whether this [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object survived a rebuild.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsSafe As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim value As System.Boolean

value = instance.IsSafe
```

### C#

```csharp
System.bool IsSafe {get;}
```

### C++/CLI

```cpp
property System.bool IsSafe {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object survived the rebuild, false if not

## VBA Syntax

See [Entity::IsSafe](ms-its:sldworksapivb6.chm::/sldworks~Entity~IsSafe.html).

## Remarks

The IEntity::IsSafe property is read-only and does not persist from session to session. To make an entity safe, use [IEntity::GetSafeEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~GetSafeEntity.html).

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
