---
title: "Next Method (IEnumLoops2)"
project: "SOLIDWORKS API Help"
interface: "IEnumLoops2"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2~Next.html"
---

# Next Method (IEnumLoops2)

Gets the next loop in the loops enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Loop2, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumLoops2
Dim Celt As System.Integer
Dim Rgelt As Loop2
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Loop2 Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Loop2^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of loops for the loops enumeration
- `Rgelt`: Pointer to an array of [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) of size Celt
- `PceltFetched`: Pointer to the number of loops returned from the list; this value can be less than celt if you ask for more loops than exist, or it can be NULL if no more loops exist

## VBA Syntax

See [EnumLoops2::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumLoops2~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumLoops2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2.html)
[IEnumLoops2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
