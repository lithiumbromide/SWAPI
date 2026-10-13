---
title: "GetLineCount2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetLineCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetLineCount2.html"
---

# GetLineCount2 Method (ISketch)

Gets the number of lines in the sketch with an option to exclude or include crosshatch lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineCount2( _
   ByVal CrossHatchOption As System.Short _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim CrossHatchOption As System.Short
Dim value As System.Integer

value = instance.GetLineCount2(CrossHatchOption)
```

### C#

```csharp
System.int GetLineCount2(
   System.short CrossHatchOption
)
```

### C++/CLI

```cpp
System.int GetLineCount2(
   System.short CrossHatchOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`: Crosshatch option as defined in [swCrossHatchFilter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)

### Return Value

Number of lines

## VBA Syntax

See [Sketch::GetLineCount2](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetLineCount2.html).

## Examples

[Get Lines in Sketch (VBA)](Get_Lines_in_Sketch_Example_VB.htm)
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before calling [ISketch::IGetLines2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetLines2.html) to determine the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
