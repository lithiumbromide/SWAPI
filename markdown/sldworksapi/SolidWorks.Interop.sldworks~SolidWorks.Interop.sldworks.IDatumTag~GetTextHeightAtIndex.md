---
title: "GetTextHeightAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetTextHeightAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextHeightAtIndex.html"
---

# GetTextHeightAtIndex Method (IDatumTag)

Gets the height of the specified text in this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextHeightAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetTextHeightAtIndex(Index)
```

### C#

```csharp
System.double GetTextHeightAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetTextHeightAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text; index begins at 0

### Return Value

Height of the specified text in meters

## VBA Syntax

See [DatumTag::GetTextHeightAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetTextHeightAtIndex.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAngleAtIndex.html)
[IDatumTag::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAtIndex.html)
[IDatumTag::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextCount.html)
[IDatumTag::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextInvertAtIndex.html)
[IDatumTag::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextPositionAtIndex.html)
[IDatumTag::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextRefPositionAtIndex.html)
[IDatumTag::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTextPositionAtIndex.html)
