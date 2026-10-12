---
title: "IGetArrowHeadAtIndex Method (IMultiJogLeader)"
project: "SOLIDWORKS API Help"
interface: "IMultiJogLeader"
member: "IGetArrowHeadAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetArrowHeadAtIndex.html"
---

# IGetArrowHeadAtIndex Method (IMultiJogLeader)

Gets the information for the specified arrow head.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMultiJogLeader
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

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IMultiJogLeader::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetArrowHeadAtIndex.html)
[IMultiJogLeader::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetArrowHeadCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
