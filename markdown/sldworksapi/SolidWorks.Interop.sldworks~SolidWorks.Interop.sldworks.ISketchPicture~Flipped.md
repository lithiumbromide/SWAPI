---
title: "Flipped Property (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "Flipped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Flipped.html"
---

# Flipped Property (ISketchPicture)

Gets whether the picture has been flipped in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Flipped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim value As System.Boolean

value = instance.Flipped
```

### C#

```csharp
System.bool Flipped {get;}
```

### C++/CLI

```cpp
property System.bool Flipped {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the picture has been flipped either side to side or top to bottom, false if not (see **Remarks**)

## VBA Syntax

See [SketchPicture::Flipped](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~Flipped.html).

## Examples

See the [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html) examples.

## Remarks

When a picture has not been flipped, as when you initially insert it, the bottom of the picture is defined by starting at the origin and proceeding in the direction of the [angle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~Angle.html). If a picture has been flipped, then the bottom of the picture is defined by starting at the origin and proceeding in a direction opposite the angle. In other words, the picture is mirrored or reflected, but not duplicated.

If a picture has been [flipped](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~Flip.html) both side to side and top to bottom, then this property returns false.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::GetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin.html)
[ISketchPicture::SetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetOrigin.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
