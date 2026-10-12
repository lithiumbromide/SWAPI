---
title: "GetNext5 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetNext5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetNext5.html"
---

# GetNext5 Method (IDisplayDimension)

Gets the next display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext5() As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As DisplayDimension

value = instance.GetNext5()
```

### C#

```csharp
DisplayDimension GetNext5()
```

### C++/CLI

```cpp
DisplayDimension^ GetNext5();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the next [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object

## VBA Syntax

See [DisplayDimension::GetNext5](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetNext5.html).

## Examples

[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)

## Remarks

A dimension can be displayed multiple times. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [IDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html) object in the SOLIDWORKS API.

Call this method after calling [IView::GetFirstDisplayDimension5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDisplayDimension5.html).

This method displays:

- dimensions on both the sheet and sheet format.
- suppressed dimensions.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IView::GetFirstDisplayDimension5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.html)
