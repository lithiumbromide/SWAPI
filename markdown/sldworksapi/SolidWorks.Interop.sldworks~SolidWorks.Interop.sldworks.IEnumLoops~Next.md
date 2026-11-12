---
title: "Next Method (IEnumLoops)"
project: "SOLIDWORKS API Help"
interface: "IEnumLoops"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops~Next.html"
---

# Next Method (IEnumLoops)

Obsolete. Superseded by [IEnumLoops2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumLoops2~Next.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Loop, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumLoops
Dim Celt As System.Integer
Dim Rgelt As Loop
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Loop Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Loop^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`:
- `Rgelt`:
- `PceltFetched`:

## VBA Syntax

See [EnumLoops::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumLoops~Next.html).

## See Also

[IEnumLoops Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops.html)
[IEnumLoops Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops_members.html)
