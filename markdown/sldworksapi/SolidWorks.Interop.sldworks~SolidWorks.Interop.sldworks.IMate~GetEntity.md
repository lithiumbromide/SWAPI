---
title: "GetEntity Method (IMate)"
project: "SOLIDWORKS API Help"
interface: "IMate"
member: "GetEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate~GetEntity.html"
---

# GetEntity Method (IMate)

Obsolete. Superseded by [IMate2::MateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~MateEntity.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntity( _
   ByVal WhichOne As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMate
Dim WhichOne As System.Integer
Dim value As System.Object

value = instance.GetEntity(WhichOne)
```

### C#

```csharp
System.object GetEntity(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.Object^ GetEntity(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`:

## VBA Syntax

See [Mate::GetEntity](ms-its:sldworksapivb6.chm::/sldworks~Mate~GetEntity.html).

## See Also

[IMate Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate.html)
[IMate Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate_members.html)
