---
title: "GetDisplayDimensions Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.html"
---

# GetDisplayDimensions Method (IView)

Gets all of the display dimension on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimensions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDisplayDimensions()
```

### C#

```csharp
System.object GetDisplayDimensions()
```

### C++/CLI

```cpp
System.Object^ GetDisplayDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [display dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [View::GetDisplayDimensions](ms-its:sldworksapivb6.chm::/sldworks~View~GetDisplayDimensions.html).

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Use this method to obtain the array of display dimensions all at once instead of calling [IView::GetFirstDisplayDimension5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDisplayDimension5.html) and then repeatedly calling [IDisplayDimension::GetNext5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetNext5.html) to obtain the remaining display dimensions on this drawing view.

**NOTE:** Display dimensions are not the same as [actual model dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayDimensionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensionCount.html)
[IView::IGetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayDimensions.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
