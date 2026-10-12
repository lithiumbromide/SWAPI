---
title: "GetArrowHeadAtIndex Method (IMultiJogLeader)"
project: "SOLIDWORKS API Help"
interface: "IMultiJogLeader"
member: "GetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetArrowHeadAtIndex.html"
---

# GetArrowHeadAtIndex Method (IMultiJogLeader)

Gets information for the specified arrow head.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMultiJogLeader
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

- `Index`: Index of the arrow head

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [MultiJogLeader::GetArrowHeadAtIndex](ms-its:sldworksapivb6.chm::/sldworks~MultiJogLeader~GetArrowHeadAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

where:

- arrowHeadPt[3] = XYZ arrow head tip location.
- arrowHeadDir[3] = XYZ arrow head direction.
- arrowHeadWidth = arrow head width where the width is measured along the arrow head direction.
- arrowHeadHeight = arrow head height.
- arrowHeadStyle = arrow head style; for example, open, closed, and so on. See [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html).

## See Also

[IMultiJogLeader Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.html)
[IMultiJogLeader Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.html)
[IMultiJogLeader::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetArrowHeadCount.html)
[IMultiJogLeader::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetArrowHeadAtIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
