---
title: "Next Method (IEnumDrSections)"
project: "SOLIDWORKS API Help"
interface: "IEnumDrSections"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections~Next.html"
---

# Next Method (IEnumDrSections)

Gets the next section view in the section views enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As DrSection, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDrSections
Dim Celt As System.Integer
Dim Rgelt As DrSection
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out DrSection Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] DrSection^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of section views for the section views enumeration
- `Rgelt`: Pointer to an array of [section views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) of size Celt
- `PceltFetched`: Pointer to the number of drawing sections returned from the list; this value can be less than Celt if you ask for more drawing sections than exist, or it can be NULL if no more drawing sections exist

## VBA Syntax

See [EnumDrSections::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumDrSections~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDrSections Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.html)
[IEnumDrSections Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections_members.html)
