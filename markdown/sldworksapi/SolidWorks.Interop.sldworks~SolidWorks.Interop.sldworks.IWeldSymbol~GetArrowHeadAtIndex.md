---
title: "GetArrowHeadAtIndex Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadAtIndex.html"
---

# GetArrowHeadAtIndex Method (IWeldSymbol)

Gets information on the specified arrowhead in this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetArrowHeadAtIndex(Index)
```

### C#

```csharp
System.object GetArrowHeadAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetArrowHeadAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the arrow head where the index begins at 0

### Return Value

Array of doubles (see Remarks)

## VBA Syntax

See [WeldSymbol::GetArrowHeadAtIndex](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetArrowHeadAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

where:

| arrowHeadPt [3] | = XYZ arrow head tip location. |
| --- | --- |
| arrowHeadDir [3] | = XYZ arrow head direction. |
| arrowHeadWidth | = arrow head width where the width is measured along the arrow head direction. |
| arrowHeadHeight | = arrow head height. |
| arrowHeadStyle | = arrow head style (that is, open, closed, and so on) as defined in swArrowStyle_e . |

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadCount.html)
[IWeldSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadInfo.html)
[IWeldSymbol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadAtIndex.html)
[IWeldSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadInfo.html)
