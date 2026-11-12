---
title: "Next Method (IEnumDisplayDimensions)"
project: "SOLIDWORKS API Help"
interface: "IEnumDisplayDimensions"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions~Next.html"
---

# Next Method (IEnumDisplayDimensions)

Gets the next display dimension in the display dimensions enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As DisplayDimension, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDisplayDimensions
Dim Celt As System.Integer
Dim Rgelt As DisplayDimension
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out DisplayDimension Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] DisplayDimension^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of display dimensions for the display dimension enumeration
- `Rgelt`: Pointer to an array of [display dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) in of size Celt
- `PceltFetched`: Pointer to the number of display dimensions from the list; this value can be less than Celt if you ask for more display dimensions than exist, or it can be NULL if no more display dimensions exist

## VBA Syntax

See [EnumDisplayDimensions::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumDisplayDimensions~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDisplayDimensions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions.html)
[IEnumDisplayDimensions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions_members.html)
