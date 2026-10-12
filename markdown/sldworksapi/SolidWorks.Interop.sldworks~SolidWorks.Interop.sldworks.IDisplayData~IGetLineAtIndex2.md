---
title: "IGetLineAtIndex2 Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetLineAtIndex2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex2.html"
---

# IGetLineAtIndex2 Method (IDisplayData)

Obsolete. Superseded by [IDisplayData::IGetLineAtIndex3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~IGetLineAtIndex3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLineAtIndex2( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetLineAtIndex2(Index)
```

### C#

```csharp
System.double IGetLineAtIndex2(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetLineAtIndex2(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired line where the index begins at zero

### Return Value

Pointer to an array of doubles (see **Remarks**)

## VBA Syntax

See [DisplayData::IGetLineAtIndex2](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~IGetLineAtIndex2.html).

## Remarks

The return value is the following array of doubles:

```vb
[ color, lineType, Unused, Unused, startPt[3], endPt[3] ]
```

where:

| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| --- | --- |
| lineType | Line type as defined in swLineTypes_e |
| startPt[3] | x, y, z line start point |
| endPt[3] | x, y, z line end point |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineCount.html)
[IDisplayData::GetLineAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineAtIndex2.html)
