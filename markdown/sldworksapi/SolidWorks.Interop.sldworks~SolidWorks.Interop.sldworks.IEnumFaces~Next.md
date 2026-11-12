---
title: "Next Method (IEnumFaces)"
project: "SOLIDWORKS API Help"
interface: "IEnumFaces"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces~Next.html"
---

# Next Method (IEnumFaces)

Obsolete. Superseded by [IEnumFaces2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumFaces2~Next.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Face, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumFaces
Dim Celt As System.Integer
Dim Rgelt As Face
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Face Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Face^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`:
- `Rgelt`:
- `PceltFetched`:

## VBA Syntax

See [EnumFaces::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumFaces~Next.html).

## See Also

[IEnumFaces Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces.html)
[IEnumFaces Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces_members.html)
