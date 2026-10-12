---
title: "Next Method (IEnumSketchPoints)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchPoints"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints~Next.html"
---

# Next Method (IEnumSketchPoints)

Gets the next sketch point in the sketch points enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As SketchPoint, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchPoints
Dim Celt As System.Integer
Dim Rgelt As SketchPoint
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out SketchPoint Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] SketchPoint^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of sketch points for the sketch points enumeration
- `Rgelt`: Pointer to an array of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) of size Celt
- `PceltFetched`: Pointer to the number of sketch points returned from the list; this value can be less than celt if you ask for more sketch points than exist, or it can be NULL if no more sketch points exist

## VBA Syntax

See [EnumSketchPoints::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchPoints~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.html)
[IEnumSketchPoints Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
