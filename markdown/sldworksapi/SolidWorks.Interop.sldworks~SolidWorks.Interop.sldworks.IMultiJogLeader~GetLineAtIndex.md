---
title: "GetLineAtIndex Method (IMultiJogLeader)"
project: "SOLIDWORKS API Help"
interface: "IMultiJogLeader"
member: "GetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineAtIndex.html"
---

# GetLineAtIndex Method (IMultiJogLeader)

Gets the symbol information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMultiJogLeader
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLineAtIndex(Index)
```

### C#

```csharp
System.object GetLineAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLineAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the line

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [MultiJogLeader::GetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~MultiJogLeader~GetLineAtIndex.html).

## Examples

[Get Multi-jog Leader Data (C#)](Get_Multi-jog_Leader_Data_Example_CSharp.htm)
[Get Multi-jog Leader Data (VB.NET)](Get_Multi-jog_Leader_Data_Example_VBNET.htm)
[Get Multi-jog Leader Data (VBA)](Get_Multi-jog_Leader_Data_Example_VB.htm)

## Remarks

The return value is the following array of doubles:

[ lineType, startPt[3], endPt[3] ]

where:

- lineType = line type. See [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).
- startPt[3] = XYZ line start point.
- endPt[3] = XYZ line end point.

## See Also

[IMultiJogLeader Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.html)
[IMultiJogLeader Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.html)
[IMultiJogLeader::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineCount.html)
[IMultiJogLeader::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetLineAtIndex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
