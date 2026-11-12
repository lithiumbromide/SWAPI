---
title: "GetSolidHatchCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSolidHatchCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchCount.html"
---

# GetSolidHatchCount Method (IView)

Gets the number of visible solid-fill hatches in a detail, break, or crop view and the size of the array for their boundary data.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSolidHatchCount( _
   ByRef ArraySize As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Integer

value = instance.GetSolidHatchCount(ArraySize)
```

### C#

```csharp
System.int GetSolidHatchCount(
   out System.int ArraySize
)
```

### C++/CLI

```cpp
System.int GetSolidHatchCount(
   [Out] System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Number of solid-fill hatches

### Return Value

Size of the array for the solid-fill hatches boundary data

## VBA Syntax

See [View::GetSolidHatchCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetSolidHatchCount.html).

## Examples

[Get Solid-fill Hatch Information (VB.NET)](Get_Solid-fill_Hatch_Information_Example_VBNET.htm)
[Get Solid-fill Hatch Information (VBA)](Get_Solid-fill_Hatch_Information_Example_VB6.htm)
[Get Solid-fill Hatch Information (C#)](Get_Solid-fill_Hatch_Information_Example_CSharp.htm)

## Remarks

To get information about solid-fill hatches in drawing views, use [IView::GetFaceHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFaceHatchCount.html), [IView::GetFaceHatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFaceHatches.html), and [IView::IGetFaceHatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetFaceHatches.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSolidHatchInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchInfo.html)
[IView::IGetSolidHatchInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSolidHatchInfo.html)
[ISketch::GetSketchHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchHatches.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
