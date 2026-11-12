---
title: "IGetTextPositionAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetTextPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPositionAtIndex.html"
---

# IGetTextPositionAtIndex Method (IGtol)

Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetTextPositionAtIndex(Index)
```

### C#

```csharp
System.double IGetTextPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetTextPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the piece of text

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IGtol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextRefPositionAtIndex.html)
[IGtol::IGetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPoint.html)
