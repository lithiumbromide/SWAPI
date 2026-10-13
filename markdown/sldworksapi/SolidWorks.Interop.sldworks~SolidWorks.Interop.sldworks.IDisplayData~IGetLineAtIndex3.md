---
title: "IGetLineAtIndex3 Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetLineAtIndex3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex3.html"
---

# IGetLineAtIndex3 Method (IDisplayData)

Gets information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLineAtIndex3( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetLineAtIndex3(Index)
```

### C#

```csharp
System.double IGetLineAtIndex3(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetLineAtIndex3(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired line where the index begins at 0

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IDisplayData::GetLineAtIndex3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineAtIndex3.html)
[IDisplayData::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineCount.html)

## Availability

SOLIDWORKS 2008 SP3, Revision Number 16.3
