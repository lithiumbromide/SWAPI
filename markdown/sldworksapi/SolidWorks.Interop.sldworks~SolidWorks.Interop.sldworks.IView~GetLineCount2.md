---
title: "GetLineCount2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetLineCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLineCount2.html"
---

# GetLineCount2 Method (IView)

Gets the number of lines in this view with an option to include or exclude crosshatch lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineCount2( _
   ByVal CrossHatchOption As System.Short _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
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

See [View::GetLineCount2](ms-its:sldworksapivb6.chm::/sldworks~View~GetLineCount2.html).

## Examples

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetLines4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetLines4.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetLines4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLines4.html)
[IView::IGetLines4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
