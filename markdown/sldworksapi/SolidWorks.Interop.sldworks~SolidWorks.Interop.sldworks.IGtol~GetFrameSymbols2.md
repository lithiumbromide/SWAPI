---
title: "GetFrameSymbols2 Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFrameSymbols2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.html"
---

# GetFrameSymbols2 Method (IGtol)

Obsolete. Superseded by [IGtol::GetFrameSymbols3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameSymbols2( _
   ByVal FrameNumber As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim value As System.Object

value = instance.GetFrameSymbols2(FrameNumber)
```

### C#

```csharp
System.object GetFrameSymbols2(
   System.short FrameNumber
)
```

### C++/CLI

```cpp
System.Object^ GetFrameSymbols2(
   System.short FrameNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Frame number to examine (1 or 2)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetFrameSymbols2](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFrameSymbols2.html).

## Remarks

The return array is an array of six strings in the following format:

`retval`[0] = Geometric tolerance symbol

`retval`[1] = Material condition symbol for first tolerance value

`retval`[2] = Material condition symbol for second tolerance value

`retval`[3] = Material condition symbol for datum1

`retval`[4] = Material condition symbol for datum2

`retval`[5] = Material condition symbol for datum3

The character strings returned in the array correspond to symbols defined in **C:\ProgramData\SolidWorks\SolidWorks** **20**`nn`**\lang\english\gtol.sym**. The format of each string is <`LibraryName-SymbolName`> (for example, **<GTOL-ANGULAR>,** which is the angularity symbol from the ASME Geometric Tolerancing Symbols library).

Use this method with [IGtol::GetFrameDiameterSymbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetFrameDiameterSymbols.html), which determines whether diameter symbols are displayed.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFrameCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.html)
[IGtol::GetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.html)
[IGtol::GetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.html)
[IGtol::IGetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.html)
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.html)
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.html)
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html)
[IGtol::SetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.html)

## Availability

SOLIDWORKS 99, datecode 1999207
