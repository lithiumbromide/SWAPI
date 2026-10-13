---
title: "GetSketchHatches Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchHatches"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchHatches.html"
---

# GetSketchHatches Method (ISketch)

Gets an array of sketch hatches that exist in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchHatches() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchHatches()
```

### C#

```csharp
System.object GetSketchHatches()
```

### C++/CLI

```cpp
System.Object^ GetSketchHatches();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch hatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch.html)

## VBA Syntax

See [Sketch::GetSketchHatches](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchHatches.html).

## Examples

[Get Area Hatch (VBA)](Get_Area_Hatch_Data_Example_VB.htm)
[Get Hatching Data (VBA)](Get_Hatching_Data_Example_VB.htm)
[Insert Hatch (VBA)](Insert_Hatch_Example_VB.htm)

## Remarks

For information about hatches:

- in drawing views, use [IView::GetFaceHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFaceHatchCount.html), [IView::GetFaceHatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFaceHatches.html), and [IView::IGetFaceHatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetFaceHatches.html).
- detail, broken, or crop views, use [IView::GetSolidHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchCount.html), [IView::GetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchInfo.html), and [IView::IGetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSolidHatchInfo.html)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IEnumSketchHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchHatches.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
