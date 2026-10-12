---
title: "IGetArrowHeadAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "IGetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadAtIndex.html"
---

# IGetArrowHeadAtIndex Method (ISFSymbol)

Gets information on the specified arrow head in this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetArrowHeadAtIndex(Index)
```

### C#

```csharp
System.double IGetArrowHeadAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetArrowHeadAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the arrow head where the index begins at 0

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[ISFSymbol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadAtIndex.html)
[ISFSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadInfo.html)
[ISFSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadInfo.html)
