---
title: "Next Method (IEnumBodies2)"
project: "SOLIDWORKS API Help"
interface: "IEnumBodies2"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Next.html"
---

# Next Method (IEnumBodies2)

Gets the next body in the bodies enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Body2, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumBodies2
Dim Celt As System.Integer
Dim Rgelt As Body2
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Body2 Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Body2^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of bodies for the bodies enumeration
- `Rgelt`: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of size Celt
- `PceltFetched`: Pointer to the number of bodies returned from the list; this value can be less than Celt if you request more bodies than exist, or it can be NULL if no more bodies exist

## VBA Syntax

See [EnumBodies2::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumBodies2~Next.html).

## Examples

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumBodies2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.html)
[IEnumBodies2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
