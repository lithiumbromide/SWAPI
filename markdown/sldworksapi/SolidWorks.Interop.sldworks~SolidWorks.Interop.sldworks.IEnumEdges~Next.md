---
title: "Next Method (IEnumEdges)"
project: "SOLIDWORKS API Help"
interface: "IEnumEdges"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges~Next.html"
---

# Next Method (IEnumEdges)

Gets the next edge in the edges enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Edge, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumEdges
Dim Celt As System.Integer
Dim Rgelt As Edge
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Edge Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Edge^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number edges for the edges enumeration
- `Rgelt`: Pointer to an array of edges of size Celt
- `PceltFetched`: Pointer to the number of edges returned from the list; this value can be less than Celt if you ask for more edges than exist, or it can be NULL if no more edges exist.

## VBA Syntax

See [EnumEdges::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumEdges~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.html)
[IEnumEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges_members.html)
