---
title: "GetArrowHeadAtIndex2 Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetArrowHeadAtIndex2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadAtIndex2.html"
---

# GetArrowHeadAtIndex2 Method (IDisplayData)

Gets information on the specified arrow head.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadAtIndex2( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetArrowHeadAtIndex2(Index)
```

### C#

```csharp
System.object GetArrowHeadAtIndex2(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetArrowHeadAtIndex2(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired arrow head where the index begins at zero

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DisplayData::GetArrowHeadAtIndex2](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetArrowHeadAtIndex2.html).

## Remarks

The return value is the following array of doubles:

**[** `arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle, arrowHeadNormal[3]` **]**

where:

| Array member... | Contains... |
| --- | --- |
| arrowHeadPt[3] | XYZ coordinates of arrow head tip location |
| arrowHeadDir[3] | XYZ coordinates of arrow head direction |
| arrowHeadWidth | Arrow head width measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in swArrowStyle_e |
| arrowHeadNormal[3] | XYZ coordinates of normal to the plane of the arrow head |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetArrowHeadCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
