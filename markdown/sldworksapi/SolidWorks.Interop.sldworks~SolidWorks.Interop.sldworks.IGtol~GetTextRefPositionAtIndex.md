---
title: "GetTextRefPositionAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetTextRefPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextRefPositionAtIndex.html"
---

# GetTextRefPositionAtIndex Method (IGtol)

Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextRefPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

- `Index`: 0-based index of the piece of text

### Return Value

Reference position of the specified text item as defined in [swTextPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextPosition_e.html)

## VBA Syntax

See [Gtol::GetTextRefPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetTextRefPositionAtIndex.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextAngleAtIndex.html)
[IGtol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextAtIndex.html)
[IGtol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextCount.html)
[IGtol::GetTextFont Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextFont.html)
[IGtol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextHeightAtIndex.html)
[IGtol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextInvertAtIndex.html)
[IGtol::GetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextPoint.html)
[IGtol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextPositionAtIndex.html)
[IGtol::IGetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPoint.html)
[IGtol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPositionAtIndex.html)
