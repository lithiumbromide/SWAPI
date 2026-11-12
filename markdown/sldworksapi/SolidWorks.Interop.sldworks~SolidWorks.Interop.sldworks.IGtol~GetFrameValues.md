---
title: "GetFrameValues Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFrameValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.html"
---

# GetFrameValues Method (IGtol)

Gets an array that describes the text that appears in each of the fields of the specified GTol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameValues( _
   ByVal FrameNumber As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim value As System.Object

value = instance.GetFrameValues(FrameNumber)
```

### C#

```csharp
System.object GetFrameValues(
   System.short FrameNumber
)
```

### C++/CLI

```cpp
System.Object^ GetFrameValues(
   System.short FrameNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Frame number to examine (1 or 2)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetFrameValues](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFrameValues.html).

## Examples

[Get Text Items in GTol Frame (VBA)](Get_Text_Items_in_GTol_Frame_VB.htm)
[Get Text Items in GTol Frame (VB.NET)](Get_Text_Items_in_GTol_Frame_Example_VBNET.htm)
[Get Text Items in GTol Frame (C#)](Get_Text_Items_in_GTol_Frame_Example_CSharp.htm)

## Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

Format of return array of strings is:

`retval`[0] = Tolerance 1

`retval`[1] = Tolerance 2

`retval`[2] = Datum 1

`retval`[3] = Datum 2

`retval`[4] = Datum 3

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFrameCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.html)
[IGtol::GetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.html)
[IGtol::GetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.html)
[IGtol::IGetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.html)
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.html)
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.html)
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html)
[IGtol::SetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.html)
