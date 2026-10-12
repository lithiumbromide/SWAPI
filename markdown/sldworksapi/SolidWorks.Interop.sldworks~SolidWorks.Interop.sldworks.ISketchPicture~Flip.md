---
title: "Flip Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "Flip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Flip.html"
---

# Flip Method (ISketchPicture)

Flips the picture, in its same position, either side to side or top to bottom.

## Syntax

### Visual Basic (Declaration)

```vb
Function Flip( _
   ByVal SideToSide As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim SideToSide As System.Boolean
Dim value As System.Boolean

value = instance.Flip(SideToSide)
```

### C#

```csharp
System.bool Flip(
   System.bool SideToSide
)
```

### C++/CLI

```cpp
System.bool Flip(
   System.bool SideToSide
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SideToSide`: True to flip the picture side to side, false to flip the picture top to bottom (see **Remarks**)

### Return Value

True if the picture is flipped, false if not

## VBA Syntax

See [SketchPicture::Flip](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~Flip.html).

## Examples

See the [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html) examples.

## Remarks

| If you flip the picture... | Then the angle ... |
| --- | --- |
| side to side | remains the same and the ISketchPicture::Flipped property returns true. |
| top to bottom | increments by 180 and the ISketchPicture::Flipped property returns true. |
| side to side and top to bottom | rotates 180 and ISketchPicture::Flipped returns false. |

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
