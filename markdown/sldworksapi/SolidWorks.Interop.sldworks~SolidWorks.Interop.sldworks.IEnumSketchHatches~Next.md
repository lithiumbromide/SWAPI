---
title: "Next Method (IEnumSketchHatches)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchHatches"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches~Next.html"
---

# Next Method (IEnumSketchHatches)

Gets the next sketch hatch in the sketch hatch enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As SketchHatch, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchHatches
Dim Celt As System.Integer
Dim Rgelt As SketchHatch
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out SketchHatch Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] SketchHatch^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of sketch hatches for this sketch hatch enumeration
- `Rgelt`: Pointer to an array of [sketch hatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch.html) of size Celt
- `PceltFetched`: Pointer to the number of sketch hatches returned from the list; this value can be less than celt if you ask for more SketchHatch objects than exist, or it can be NULL if no more SketchHatch objects exist

## VBA Syntax

See [EnumSketchHatches::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchHatches~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchHatches Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches.html)
[IEnumSketchHatches Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
