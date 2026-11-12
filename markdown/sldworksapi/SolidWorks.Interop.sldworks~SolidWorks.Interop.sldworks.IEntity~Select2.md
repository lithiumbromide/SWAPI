---
title: "Select2 Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select2.html"
---

# Select2 Method (IEntity)

Obsolete. Superseded by [IEntity::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~Select4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.Select2(Append, Mark)
```

### C#

```csharp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`:
- `Mark`:

## VBA Syntax

See [Entity::Select2](ms-its:sldworksapivb6.chm::/sldworks~Entity~Select2.html).

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
