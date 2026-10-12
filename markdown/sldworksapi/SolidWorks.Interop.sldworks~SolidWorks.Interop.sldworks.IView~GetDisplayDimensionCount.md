---
title: "GetDisplayDimensionCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDisplayDimensionCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensionCount.html"
---

# GetDisplayDimensionCount Method (IView)

Gets the number of display dimensions in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimensionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetDisplayDimensionCount()
```

### C#

```csharp
System.int GetDisplayDimensionCount()
```

### C++/CLI

```cpp
System.int GetDisplayDimensionCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of display dimensions

## VBA Syntax

See [View::GetDisplayDimensionCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetDisplayDimensionCount.html).

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDisplayDimensions.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
