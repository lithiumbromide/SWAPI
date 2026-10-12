---
title: "GetTextRefPositionAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetTextRefPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextRefPositionAtIndex.html"
---

# GetTextRefPositionAtIndex Method (IDatumTag)

Gets the reference position of the specified text item in this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextRefPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetTextRefPositionAtIndex(Index)
```

### C#

```csharp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text; index begins at 0

### Return Value

Reference position of the specified text item as defined in [swTextPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextPosition_e.html)

## VBA Syntax

See [DatumTag::GetTextRefPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetTextRefPositionAtIndex.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAngleAtIndex.html)
[IDatumTag::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAtIndex.html)
[IDatumTag::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextCount.html)
[IDatumTag::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextHeightAtIndex.html)
[IDatumTag::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextInvertAtIndex.html)
[IDatumTag::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextPositionAtIndex.html)
[IDatumTag::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTextPositionAtIndex.html)
