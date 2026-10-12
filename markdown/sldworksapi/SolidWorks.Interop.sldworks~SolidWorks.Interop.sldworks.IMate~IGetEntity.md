---
title: "IGetEntity Method (IMate)"
project: "SOLIDWORKS API Help"
interface: "IMate"
member: "IGetEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate~IGetEntity.html"
---

# IGetEntity Method (IMate)

Obsolete. Superseded by [IMate2::MateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~MateEntity.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntity( _
   ByVal WhichOne As System.Integer _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IMate
Dim WhichOne As System.Integer
Dim value As Entity

value = instance.IGetEntity(WhichOne)
```

### C#

```csharp
Entity IGetEntity(
   System.int WhichOne
)
```

### C++/CLI

```cpp
Entity^ IGetEntity(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`:

## VBA Syntax

See [Mate::IGetEntity](ms-its:sldworksapivb6.chm::/sldworks~Mate~IGetEntity.html).

## See Also

[IMate Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate.html)
[IMate Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate_members.html)
