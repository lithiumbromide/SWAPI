---
title: "GetFrameCount Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFrameCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.html"
---

# GetFrameCount Method (IGtol)

Gets the number of frames in this GTol symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameCount() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Short

value = instance.GetFrameCount()
```

### C#

```csharp
System.short GetFrameCount()
```

### C++/CLI

```cpp
System.short GetFrameCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of frames in this GTol symbol

## VBA Syntax

See [Gtol::GetFrameCount](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFrameCount.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Examples

[Get Text Items in GTol Frame (VBA)](Get_Text_Items_in_GTol_Frame_VB.htm)
[Get Text Items in GTol Frame (VB.NET)](Get_Text_Items_in_GTol_Frame_Example_VBNET.htm)
[Get Text Items in GTol Frame (C#)](Get_Text_Items_in_GTol_Frame_Example_CSharp.htm)

## Remarks

This method returns the number of frames that this symbol has stored, which may be different than the number of frames that actually appear when this frame is displayed. This is because symbols can be created, either through the user interface or the API, with empty frames or rows, which do not appear when the frame is displayed.

For example, the symbol can be displayed with three 3 frames, but upon examination, it could be that those are frames 1, 2, and 5. Frames 3 and 4 are empty. Every symbol must have at least 2 frames.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.html)
[IGtol::GetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.html)
[IGtol::GetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.html)
[IGtol::IGetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.html)
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.html)
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.html)
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html)
[IGtol::SetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
