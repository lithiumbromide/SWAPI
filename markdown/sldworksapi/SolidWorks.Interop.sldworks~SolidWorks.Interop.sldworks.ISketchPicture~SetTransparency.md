---
title: "SetTransparency Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "SetTransparency"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetTransparency.html"
---

# SetTransparency Method (ISketchPicture)

Sets the transparency parameters of this picture on the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTransparency( _
   ByVal Style As System.Integer, _
   ByVal Transparency As System.Double, _
   ByVal MatchingColor As System.Integer, _
   ByVal MatchingTolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim Style As System.Integer
Dim Transparency As System.Double
Dim MatchingColor As System.Integer
Dim MatchingTolerance As System.Double
Dim value As System.Boolean

value = instance.SetTransparency(Style, Transparency, MatchingColor, MatchingTolerance)
```

### C#

```csharp
System.bool SetTransparency(
   System.int Style,
   System.double Transparency,
   System.int MatchingColor,
   System.double MatchingTolerance
)
```

### C++/CLI

```cpp
System.bool SetTransparency(
   System.int Style,
   System.double Transparency,
   System.int MatchingColor,
   System.double MatchingTolerance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Style as defined by [swSketchPictureTransparencyStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchPictureTransparencyStyle_e.html)
- `Transparency`: - 0 = opaque
  - 1 = transparent

  describing the relative transparency depending on the value of Style
- `MatchingColor`: RGB color used as the transparent color when Style is swSketchPictureTransparencyUserDefined
- `MatchingTolerance`: - 0 = exact match
  - 1 = less exact match

  indicating how closely MatchingColor must be to be considered a transparent color when Style is swSketchPictureTransparencyUserDefined

### Return Value

True if transparency is set, false if not

## VBA Syntax

See [SketchPicture::SetTransparency](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~SetTransparency.html).

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::GetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
