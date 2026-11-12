---
title: "GetTextPositionAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetTextPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPositionAtIndex.html"
---

# GetTextPositionAtIndex Method (IDisplayData)

Gets the text item offset relative to the note text point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetTextPositionAtIndex(Index)
```

### C#

```csharp
System.object GetTextPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetTextPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the desired piece of text

### Return Value

Array of doubles (**Remarks**)

## VBA Syntax

See [DisplayData::GetTextPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetTextPositionAtIndex.html).

## Remarks

The return value is the following array of doubles:

**[** `textPtX, textPtY, textPtZ` **]**

where these text position values are actually offset values from the origin of this display data.

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
[IDisplayData::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInvertAtIndex.html)
[IDisplayData::GetTextLineSpacingAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextLineSpacingAtIndex.html)
[IDisplayData::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextRefPositionAtIndex.html)
[IDisplayData::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTextPositionAtIndex.html)
[IDisplayData::GetTextPlaneAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPlaneAtIndex.html)
