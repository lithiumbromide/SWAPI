---
title: "Next Method (IEnumBodies)"
project: "SOLIDWORKS API Help"
interface: "IEnumBodies"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies~Next.html"
---

# Next Method (IEnumBodies)

Obsolete. Superseded by [IEnumBodies2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2~Next.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Body, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumBodies
Dim Celt As System.Integer
Dim Rgelt As Body
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Body Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Body^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`:
- `Rgelt`:
- `PceltFetched`:

## VBA Syntax

See [EnumBodies::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumBodies~Next.html).

## See Also

[IEnumBodies Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies.html)
[IEnumBodies Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies_members.html)
