---
title: "SetCoordinates Method (ISketchText)"
project: "SOLIDWORKS API Help"
interface: "ISketchText"
member: "SetCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetCoordinates.html"
---

# SetCoordinates Method (ISketchText)

Sets the position of this sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoordinates( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchText
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SetCoordinates(X, Y, Z)
```

### C#

```csharp
System.bool SetCoordinates(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetCoordinates(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of the sketch text position
- `Y`: Y coordinate of the sketch text position
- `Z`: Z coordinate of the sketch text position

### Return Value

True if the sketch text position is successfully set, false if not

## VBA Syntax

See [SketchText::SetCoordinates](ms-its:sldworksapivb6.chm::/sldworks~SketchText~SetCoordinates.html).

## Remarks

To set the sketch text position, you must be editing the sketch. See [IModelDoc2::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditSketch.html) or [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html).

To get the position of this sketch text, use [ISketchText::GetCoordinates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~GetCoordinates.html) and [ISketchText::IGetCoordinates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText~IGetCoordinates.html).

## See Also

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.html)
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
