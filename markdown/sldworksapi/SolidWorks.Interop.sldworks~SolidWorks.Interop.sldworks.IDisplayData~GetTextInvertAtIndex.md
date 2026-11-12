---
title: "GetTextInvertAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetTextInvertAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInvertAtIndex.html"
---

# GetTextInvertAtIndex Method (IDisplayData)

Gets the specified text's invert flag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextInvertAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
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

- `Index`: Zero-based index of the desired piece of text

### Return Value

Text item invert flag

## VBA Syntax

See [DisplayData::GetTextInvertAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetTextInvertAtIndex.html).

## Remarks

The invert flag specifies whether the text is mirrored (reflected) about the X axis. Any reflection is applied after text rotation.

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAngleAtIndex.html)
[IDisplayData::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAtIndex.html)
[IDisplayData::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextCount.html)
[IDisplayData::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextFontAtIndex.html)
[IDisplayData::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextHeightAtIndex.html)
[IDisplayData::GetTextInBoxHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxHeightAtIndex.html)
[IDisplayData::GetTextInBoxStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxStyleAtIndex.html)
[IDisplayData::GetTextInBoxWidthAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxWidthAtIndex.html)
[IDisplayData::GetTextLineSpacingAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextLineSpacingAtIndex.html)
[IDisplayData::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPositionAtIndex.html)
[IDisplayData::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextRefPositionAtIndex.html)
[IDisplayData::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTextPositionAtIndex.html)
[IDisplayData::GetTextPlaneAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPlaneAtIndex.html)
