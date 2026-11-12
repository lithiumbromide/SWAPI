---
title: "GetTransparency Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "GetTransparency"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetTransparency.html"
---

# GetTransparency Method (ISketchPicture)

Gets transparency parameters for this picture.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetTransparency( _
   ByRef Style As System.Integer, _
   ByRef Transparency As System.Double, _
   ByRef MatchingColor As System.Integer, _
   ByRef MatchingTolerance As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim Style As System.Integer
Dim Transparency As System.Double
Dim MatchingColor As System.Integer
Dim MatchingTolerance As System.Double

instance.GetTransparency(Style, Transparency, MatchingColor, MatchingTolerance)
```

### C#

```csharp
void GetTransparency(
   out System.int Style,
   out System.double Transparency,
   out System.int MatchingColor,
   out System.double MatchingTolerance
)
```

### C++/CLI

```cpp
void GetTransparency(
   [Out] System.int Style,
   [Out] System.double Transparency,
   [Out] System.int MatchingColor,
   [Out] System.double MatchingTolerance
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

## VBA Syntax

See [SketchPicture::GetTransparency](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~GetTransparency.html).

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
