---
title: "Next Method (IEnumSketchSegments)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchSegments"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments~Next.html"
---

# Next Method (IEnumSketchSegments)

Gets the next sketch segment in the sketch segments enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As SketchSegment, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchSegments
Dim Celt As System.Integer
Dim Rgelt As SketchSegment
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out SketchSegment Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] SketchSegment^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of sketch segments for the sketch segments enumeration
- `Rgelt`: Pointer to an array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) of size Celt
- `PceltFetched`: Pointer to the number of sketch segments returned from the list; this value can be less than celt if you ask for more sketch segments than exist, or it can be NULL if no more sketch segments exist

## VBA Syntax

See [EnumSketchSegments::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchSegments~Next.html).

## Examples

[Select All Sketch Segments (C++)](Select_All_Sketch_Segments_Example_CPlusPlus_COM.htm)

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchSegments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.html)
[IEnumSketchSegments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
