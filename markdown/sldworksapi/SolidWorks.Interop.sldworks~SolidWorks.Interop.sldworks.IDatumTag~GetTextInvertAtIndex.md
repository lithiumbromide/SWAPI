---
title: "GetTextInvertAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetTextInvertAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextInvertAtIndex.html"
---

# GetTextInvertAtIndex Method (IDatumTag)

Gets the specified text item's invert flag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextInvertAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetTextInvertAtIndex(Index)
```

### C#

```csharp
System.int GetTextInvertAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetTextInvertAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text; index begins at 0

### Return Value

Text item's invert flag

## VBA Syntax

See [DatumTag::GetTextInvertAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetTextInvertAtIndex.html).

## Remarks

The invert flag specifies whether the text was mirrored (reflected) about the X axis. Any reflection is applied after text rotation.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAngleAtIndex.html)
[IDatumTag::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAtIndex.html)
[IDatumTag::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextCount.html)
[IDatumTag::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextHeightAtIndex.html)
[IDatumTag::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextPositionAtIndex.html)
[IDatumTag::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextRefPositionAtIndex.html)
[IDatumTag::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTextPositionAtIndex.html)
