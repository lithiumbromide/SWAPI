---
title: "GetSketch Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketch.html"
---

# GetSketch Method (IView)

Gets the sketch used by this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetSketch()
```

### C#

```csharp
System.object GetSketch()
```

### C++/CLI

```cpp
System.Object^ GetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [View::GetSketch](ms-its:sldworksapivb6.chm::/sldworks~View~GetSketch.html).

## Examples

[Get Hatching Data (VBA)](Get_Hatching_Data_Example_VB.htm)
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)
[Get Sketch Point's View (VBA)](Get_Sketch_Point_s_View_Example_VB.htm)
[Insert and Position DXF File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)
[Get Area Hatch Data (VBA)](Get_Area_Hatch_Data_Example_VB.htm)
[Get Area Hatch Data (VB.NET)](Get_Area_Hatch_Data_Example_VBNET.htm)
[Get Area Hatch Data (C#)](Get_Area_Hatch_Data_Example_CSharp.htm)

## Remarks

Each drawing view contains an underlying sketch. The user can activate the sketch for a drawing view by double-clicking the view. Once the drawing view is active, you can add sketch directly to the view's sketch.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketch.html)
