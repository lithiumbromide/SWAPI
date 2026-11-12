---
title: "GetFrameSymbols3 Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFrameSymbols3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols3.html"
---

# GetFrameSymbols3 Method (IGtol)

Gets the symbols for the specified frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameSymbols3( _
   ByVal FrameNumber As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Integer
Dim value As System.Object

value = instance.GetFrameSymbols3(FrameNumber)
```

### C#

```csharp
System.object GetFrameSymbols3(
   System.int FrameNumber
)
```

### C++/CLI

```cpp
System.Object^ GetFrameSymbols3(
   System.int FrameNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Frame number to examine (1 or 2)

### Return Value

Array of six strings (see **Remarks**)

## VBA Syntax

See [Gtol::GetFrameSymbols3](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFrameSymbols3.html).

## Examples

[Get Text Items in GTol Frame (C#)](Get_Text_Items_in_GTol_Frame_Example_CSharp.htm)
[Get Text Items in GTol Frame (VB.NET)](Get_Text_Items_in_GTol_Frame_Example_VBNET.htm)
[Get Text Items in GTol Frame (VBA)](Get_Text_Items_in_GTol_Frame_VB.htm)

## Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

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
[IGtol::GetFrameCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.html)
[IGtol::GetFrameDiameterSymbols Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.html)
[IGtol::IGetFrameDiameterSymbols Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.html)
[IGtol::GetFrameValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.html)
[IGtol::IGetFrameValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.html)
[IGtol::SetFrameSymbols2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html)
[IGtol::SetFrameValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues2.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
