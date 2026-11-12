---
title: "IGetDimensionIds4 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDimensionIds4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionIds4.html"
---

# IGetDimensionIds4 Method (IView)

Gets the dimension names from the current drawing sheet or the current drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDimensionIds4() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

value = instance.IGetDimensionIds4()
```

### C#

```csharp
System.string IGetDimensionIds4()
```

### C++/CLI

```cpp
System.String^ IGetDimensionIds4();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings; each string represents one dimension name from the current drawing sheet or current drawing view
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The order of the dimension names returned align with the order of information returned from [IView::GetDimensionInfo6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDimensionInfo6.html) or [IView::IGetDimensionInfo6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDimensionInfo6.html). This alignment of information is valid as long as the calls to this method and IView::GetDimensionInfo6 or IView::IGetDimensionInfo6 are made consecutively.

One string is returned for each dimension in the view. See [IView::GetDimensionCount4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDimensionCount4.html) to determine the number of dimensions in the view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.html)
[GetDimensionDisplayInfoSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.html)
[IView::GetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString4.html)
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.html)
[IView::GetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.html)
[IView::GetFirstDisplayDimension5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.html)
[IView::IGetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayInfo5.html)
[IView::IGetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayString4.html)
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.html)
[IView::IGetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionString4.html)
[IView::ProjectedDimensions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.html)
