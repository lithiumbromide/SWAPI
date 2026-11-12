---
title: "GetLineAtIndex3 Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetLineAtIndex3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineAtIndex3.html"
---

# GetLineAtIndex3 Method (IDisplayData)

Gets information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex3( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLineAtIndex3(Index)
```

### C#

```csharp
System.object GetLineAtIndex3(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLineAtIndex3(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired line where the index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DisplayData::GetLineAtIndex3](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetLineAtIndex3.html).

## Examples

[Get Centerline Annotation Information (VBA)](Get_Centerline_Annotation_Information_Example_VB.htm)
[Get Weld Bead Symbol Data (VBA)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VB.htm)
[Get Weld Bead Symbol Data (VB.NET)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VBNET.htm)
[Get Weld Bead Symbol Data (C#)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_CSharp.htm)

## Remarks

The return value is the following array of doubles:

```vb
[ color, lineType, lineStyle, lineWeight, startPt[3], endPt[3] ]
```

where:

| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| --- | --- |
| lineType | Line type as defined in swLineTypes_e |
| lineStyle | Line style as defined in swLineStyles_e |
| lineWeight | Line thickness as defined in swLineWeights_e |
| startPt[3] | x, y, z line start point |
| endPt[3] | x, y, z line end point |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::IGetLineAtIndex3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex3.html)
[IDisplayData::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineCount.html)

## Availability

SOLIDWORKS SP3, Revision Number 16.3
