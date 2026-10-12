---
title: "IGetMateEntities Method (IMate)"
project: "SOLIDWORKS API Help"
interface: "IMate"
member: "IGetMateEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate~IGetMateEntities.html"
---

# IGetMateEntities Method (IMate)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetMateEntities( _
   ByRef Entity1 As MateEntity, _
   ByRef Entity2 As MateEntity _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMate
Dim Entity1 As MateEntity
Dim Entity2 As MateEntity

instance.IGetMateEntities(Entity1, Entity2)
```

### C#

```csharp
void IGetMateEntities(
   out MateEntity Entity1,
   out MateEntity Entity2
)
```

### C++/CLI

```cpp
void IGetMateEntities(
   [Out] MateEntity^ Entity1,
   [Out] MateEntity^ Entity2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity1`:
- `Entity2`:

## VBA Syntax

See [Mate::IGetMateEntities](ms-its:sldworksapivb6.chm::/sldworks~Mate~IGetMateEntities.html).

## See Also

[IMate Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate.html)
[IMate Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate_members.html)
