---
title: "GetArrowHeadAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadAtIndex.html"
---

# GetArrowHeadAtIndex Method (ISFSymbol)

Gets information on the specified arrow head in this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
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

Array of doubles (see **Remarks**)

## VBA Syntax

See [SFSymbol::GetArrowHeadAtIndex](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetArrowHeadAtIndex.html).

## Remarks

Call [ISFSymbol::GetArrowHeadCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetArrowHeadCount.html) before calling this method to get the number of arrow heads for this surface finish symbol.

The return value is the following array of doubles :

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

where:

| arrowHeadPt [3] | = XYZ arrow head tip location |
| --- | --- |
| arrowHeadDir [3] | = XYZ arrow head direction |
| arrowHeadWidth | = Arrow head width where the width is measured along the arrow head direction |
| arrowHeadHeight | = Arrow head height |
| arrowHeadStyle | = Arrow head style (for example, open or closed) as defined in swArrowStyle_e |

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadCount.html)
[ISFSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadInfo.html)
[ISFSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadInfo.html)
