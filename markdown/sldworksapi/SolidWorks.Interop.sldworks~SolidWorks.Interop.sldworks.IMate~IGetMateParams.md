---
title: "IGetMateParams Method (IMate)"
project: "SOLIDWORKS API Help"
interface: "IMate"
member: "IGetMateParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate~IGetMateParams.html"
---

# IGetMateParams Method (IMate)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetMateParams( _
   ByRef MateType As System.Integer, _
   ByRef AlignFlag As System.Integer, _
   ByRef CanBeFlipped As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMate
Dim MateType As System.Integer
Dim AlignFlag As System.Integer
Dim CanBeFlipped As System.Integer

instance.IGetMateParams(MateType, AlignFlag, CanBeFlipped)
```

### C#

```csharp
void IGetMateParams(
   out System.int MateType,
   out System.int AlignFlag,
   out System.int CanBeFlipped
)
```

### C++/CLI

```cpp
void IGetMateParams(
   [Out] System.int MateType,
   [Out] System.int AlignFlag,
   [Out] System.int CanBeFlipped
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MateType`:
- `AlignFlag`:
- `CanBeFlipped`:

## VBA Syntax

See [Mate::IGetMateParams](ms-its:sldworksapivb6.chm::/sldworks~Mate~IGetMateParams.html).

## See Also

[IMate Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate.html)
[IMate Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate_members.html)
