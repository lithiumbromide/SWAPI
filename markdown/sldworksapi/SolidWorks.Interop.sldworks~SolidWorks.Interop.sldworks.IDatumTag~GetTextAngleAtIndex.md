---
title: "GetTextAngleAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetTextAngleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAngleAtIndex.html"
---

# GetTextAngleAtIndex Method (IDatumTag)

Gets the text angle for the specified text in this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextAngleAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetTextAngleAtIndex(Index)
```

### C#

```csharp
System.double GetTextAngleAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetTextAngleAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text; index begins at 0

### Return Value

Text angle for the specified piece of text in radians measured CCW from the X-axis

## VBA Syntax

See [DatumTag::GetTextAngleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetTextAngleAtIndex.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAtIndex.html)
[IDatumTag::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextCount.html)
[IDatumTag::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextHeightAtIndex.html)
[IDatumTag::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextInvertAtIndex.html)
[IDatumTag::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextPositionAtIndex.html)
[IDatumTag::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextRefPositionAtIndex.html)
[IDatumTag::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTextPositionAtIndex.html)
