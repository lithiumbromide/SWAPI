---
title: "IGetDisplayDimensions Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayDimensions.html"
---

# IGetDisplayDimensions Method (IView)

Gets all of the display dimensions on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDisplayDimensions( _
   ByVal NumDisplayDim As System.Integer _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumDisplayDim As System.Integer
Dim value As DisplayDimension

value = instance.IGetDisplayDimensions(NumDisplayDim)
```

### C#

```csharp
DisplayDimension IGetDisplayDimensions(
   System.int NumDisplayDim
)
```

### C++/CLI

```cpp
DisplayDimension^ IGetDisplayDimensions(
   System.int NumDisplayDim
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDisplayDim`: Total number of display dimensions on this drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [display dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of display dimensions all at once instead of calling [IView::GetFirstDisplayDimension5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDisplayDimension5.html) and then repeatedly calling [IDisplayDimension::GetNext5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetNext5.html) to obtain the remaining display dimensions on this drawing view.

Before calling this method, call [IView::GetDisplayDimensionCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDisplayDimensionCount.html) to get the value for numDisplayDim.

**NOTE:** Display dimensions are not the same as [actual model dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
