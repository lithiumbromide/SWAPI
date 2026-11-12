---
title: "Next Method (IEnumFaces2)"
project: "SOLIDWORKS API Help"
interface: "IEnumFaces2"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2~Next.html"
---

# Next Method (IEnumFaces2)

Gets the next face in the faces enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Face2, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumFaces2
Dim Celt As System.Integer
Dim Rgelt As Face2
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out Face2 Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] Face2^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of faces for the faces enumeration
- `Rgelt`: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Celt
- `PceltFetched`: Pointer to the number of faces returned from the list; this value can be less than Celt if you asked for more faces than exist, or it can be NULL if no more faces exist

## VBA Syntax

See [EnumFaces2::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumFaces2~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumFaces2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2.html)
[IEnumFaces2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
