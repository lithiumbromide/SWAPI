---
title: "GetLineAtIndex Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetLineAtIndex.html"
---

# GetLineAtIndex Method (IDatumTargetSym)

Gets information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
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

- `Index`: Index of the line; index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DatumTargetSym::GetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetLineAtIndex.html).

## Remarks

The return value is the following array of doubles:

**[** `lineType, startPt[3], endPt[3]` **]**

where:

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt[3] | XYZ line start point |
| endPt[3] | XYZ line end point |

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetLineCount.html)
[IDatumTargetSym::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetLineAtIndex.html)
