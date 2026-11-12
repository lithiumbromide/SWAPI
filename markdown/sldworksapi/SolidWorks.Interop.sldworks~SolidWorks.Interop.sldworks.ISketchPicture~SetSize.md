---
title: "SetSize Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "SetSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetSize.html"
---

# SetSize Method (ISketchPicture)

Sets the size of the picture on the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSize( _
   ByVal Width As System.Double, _
   ByVal Height As System.Double, _
   ByVal AspectRatioLocked As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim Width As System.Double
Dim Height As System.Double
Dim AspectRatioLocked As System.Boolean
Dim value As System.Boolean

value = instance.SetSize(Width, Height, AspectRatioLocked)
```

### C#

```csharp
System.bool SetSize(
   System.double Width,
   System.double Height,
   System.bool AspectRatioLocked
)
```

### C++/CLI

```cpp
System.bool SetSize(
   System.double Width,
   System.double Height,
   System.bool AspectRatioLocked
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Width of the picture in meters
- `Height`: Height of the picture in meters
- `AspectRatioLocked`: True to keep a fixed width and height aspect ratio, false to not

### Return Value

True if the size of the picture is set, false if not

## VBA Syntax

See [SketchPicture::SetSize](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~SetSize.html).

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetSize.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
