---
title: "IGetLineAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "IGetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetLineAtIndex.html"
---

# IGetLineAtIndex Method (IDatumTag)

Gets information for the specified line in this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetLineAtIndex(Index)
```

### C#

```csharp
System.double IGetLineAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetLineAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the line; index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DatumTag::IGetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~IGetLineAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3] ]

where:

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ line start point |
| endPt [3] | XYZ line end point |

Call [IDatumTag::GetLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~GetLineCount.html) before calling this method.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetLineCount.html)
