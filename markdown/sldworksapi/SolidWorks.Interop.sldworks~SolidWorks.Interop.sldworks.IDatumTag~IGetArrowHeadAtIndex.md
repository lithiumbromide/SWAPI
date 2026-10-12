---
title: "IGetArrowHeadAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "IGetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetArrowHeadAtIndex.html"
---

# IGetArrowHeadAtIndex Method (IDatumTag)

Gets information for the specified arrow head in this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
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

- `Index`: Index of the arrow head; index begins at 0

### Return Value

Pointer to an array of doubles (see **Remarks**)

## VBA Syntax

See [DatumTag::IGetArrowHeadAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~IGetArrowHeadAtIndex.html).

## Remarks

The return value is the following array of doubles :

**[** `arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle` **]**

where:

| arrowHeadPt[3] | XYZ arrow head tip location |
| --- | --- |
| arrowHeadDir[3] | XYZ arrow head direction |
| arrowHeadWidth | Arrow head width where the width is measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in swArrowStyle_e |

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArrowHeadAtIndex.html)
[IDatumTag::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArrowHeadCount.html)
