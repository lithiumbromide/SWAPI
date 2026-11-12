---
title: "GetTextPositionAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetTextPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextPositionAtIndex.html"
---

# GetTextPositionAtIndex Method (IGtol)

Gets the text item's offset relative to note's text point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

- `Index`: 0-based index of the piece of text

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Gtol::GetTextPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetTextPositionAtIndex.html).

## Remarks

The return value is the following array of doubles:

```vb
[ textPtX, textPtY, textPtZ ]
```

where the text position values are offset values from the origin of this [IGTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html) object.

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
[IGtol::IGetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPoint.html)
[IGtol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPositionAtIndex.html)
