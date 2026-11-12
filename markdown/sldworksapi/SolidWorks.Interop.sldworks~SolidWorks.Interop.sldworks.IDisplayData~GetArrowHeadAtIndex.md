---
title: "GetArrowHeadAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadAtIndex.html"
---

# GetArrowHeadAtIndex Method (IDisplayData)

Obsolete. Superseded by [IDisplayData::GetArrowheadAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadAtIndex2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
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

- `Index`: Index of the desired arrow head where the index begins at zero

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DisplayData::GetArrowHeadAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetArrowHeadAtIndex.html).

## Remarks

The return value is the following array of doubles:

**[** `arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle` **]**

where:

| arrowHeadPt[3] | XYZ arrow head tip location |
| --- | --- |
| arrowHeadDir[3] | XYZ arrow head direction |
| arrowHeadWidth | Arrow head width measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in swArrowStyle_e |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetArrowHeadAtIndex.html)
[IDisplayData::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadCount.html)
