---
title: "GetDimensionDisplayString5 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDimensionDisplayString5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString5.html"
---

# GetDimensionDisplayString5 Method (IView)

Gets all of the dimension text in the current drawing sheet or the current drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimensionDisplayString5( _
   ByRef DimensionSize As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim DimensionSize As System.Integer
Dim value As System.Object

value = instance.GetDimensionDisplayString5(DimensionSize)
```

### C#

```csharp
System.object GetDimensionDisplayString5(
   out System.int DimensionSize
)
```

### C++/CLI

```cpp
System.Object^ GetDimensionDisplayString5(
   [Out] System.int DimensionSize
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `DimensionSize`: Number of strings for each dimension (see

Remarks

)

### Return Value

Array of strings (see

Remarks

)

## VBA Syntax

See

[View::GetDimensionDisplayString5](ms-its:sldworksapivb6.chm::/sldworks~View~GetDimensionDisplayString5.html)

.

## Examples

'VBA

' Open a drawing that has one or more display dimensions

'=============================================

Dim swApp As SldWorks.SldWorks

Dim swModel As ModelDoc2

Dim swDraw As DrawingDoc

Dim swView As View

Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp. ActiveDoc

Set swDraw = swModel

Dim views As Variant

views = swDraw. GetViews ()

Set swView = views(0)(0)

Dim var As Variant

Dim size As Long

var = swView. GetDimensionDisplayString5 (size)

Debug.Print "Number of strings in returned array: " & UBound(var) + 1

Debug.Print "Number of strings for each display dimension: " & size

End Sub

## Remarks

This method returns a string array of size (`DimensionSize`) x (`number_of_dimensions_in_view`).

This set of values returned for each dimension in the view:

[value1, tolMax1 tolMin1, value2, tolMax2, tolMin2, prefix, suffix, callout1, callout2, bottom]

where:

`value1`= Primary Dimension Value

`tolMax1`= Maximum Variation for`value1`

`tolMin1`= Minimum Variation for`value1`

`value2`= Dual Dimension Value

`tolMax2`= Maximum Variation for`value2`

`tolMin2`= Minimum Variation for`value2`

`prefix`= Text before`value1`

`suffix`= Text after`value1`

`callout1`= Text above`prefix`<`value1`>`suffix`

`callout2`= Text below`prefix`<`value1`>`suffix`

`bottom`= Text below`callout2`

The Dimension PropertyManager page (PMP) contains two Dimension Text boxes. Add dimension text by entering prefix, suffix, callout1, and callout2 texts in the first Dimension Text box. Enter bottom text in the second Dimension Text box.

If any of the above values are not used in the dimension, then those values are returned as empty strings in the returned array of this method.

For more information, see**SOLIDWORKS user-interface help > Detailing and Drawings > Drawings > Dimensions in Drawings > Dimension Value PropertyManager**.

NOTES:

- A previous version of this method,

  [IView::GetDimensionDisplayString2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDimensionDisplayString2.html)

  , detects and overlooks dangling dimensions. This method neither overlooks nor indicates that any dimensions are dangling. Use IView::GetDimensionDisplayString2 if you need dangling dimensions detected and overlooked.
- This method does not support

  [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html)

  .

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetDimensionDisplayInfo5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.html)

[IView::GetDimensionDisplayInfoSize2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.html)

[IView::GetDimensionIds4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.html)

[IView::GetDimensionInfo7 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo7.html)

[IView::GetDimensionString4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.html)

[IView::GetFirstDisplayDimension5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.html)

[IView::ProjectedDimensions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
