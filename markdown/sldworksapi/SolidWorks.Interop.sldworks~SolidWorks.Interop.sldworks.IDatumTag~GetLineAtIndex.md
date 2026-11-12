---
title: "GetLineAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetLineAtIndex.html"
---

# GetLineAtIndex Method (IDatumTag)

Gets information for the specified line in this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
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

See [DatumTag::GetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetLineAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3] ]

where:

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ line start point |
| endPt [3] | XYZ line end point |

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetLineAtIndex.html)
[IDatumTag::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetLineCount.html)
