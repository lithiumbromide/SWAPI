---
title: "SetTessellationQuality Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetTessellationQuality"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetTessellationQuality.html"
---

# SetTessellationQuality Method (IModelDoc2)

Sets the shaded-display image quality number for the current document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTessellationQuality( _
   ByVal QualityNum As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim QualityNum As System.Integer

instance.SetTessellationQuality(QualityNum)
```

### C#

```csharp
void SetTessellationQuality(
   System.int QualityNum
)
```

### C++/CLI

```cpp
void SetTessellationQuality(
   System.int QualityNum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `QualityNum`: 0 < Shaded-display image quality number < 106 (see **Remarks**)

## VBA Syntax

See [ModelDoc2::SetTessellationQuality](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetTessellationQuality.html).

## Remarks

QualityNum is the degree of tessellation of curved surfaces for shaded rendering output. **Tools > Options > Document Properties > Image Quality** includes a field that sets the maximum chordal deviation. QualityNum and the maximum chordal deviation (in meters) are coupled and inversely proportional as follows:

`var` = `TessMin` + `QualityNum`*((`TessMax`-`TessMin`)/100)

`Deviation` = 0.025 * (`BodyDiameter` * 2) / `var`;

where:

- `TessMin` = 6
- `TessMax` = 166
- 0 < `QualityNum` < 106
- `BodyDiameter` is the diagonal distance across the bounds of the part box. See [IPartDoc::GetPartBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetPartBox.html) or [IPartDoc::IGetPartBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IGetPartBox.html) for more information.

There are two ways to set the image quality for assemblies using the API. You can either:

- Call this method

- or -

- Set [swUserPreferenceIntegerValue_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).swImageQualityShaded
- Set [swUserPreferenceDoubleValue_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceDoubleValue_e.html).swImageQualityShadedDeviation

Before doing either, you must set [swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swImageQualityApplyToAllReferencedPartDoc to true in order to affect the image quality of the assembly.

Call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html) after calling this method to update the part.

**NOTE:** Setting the degree of tessellation to a higher value results in:

- finer tessellation,
- increased file size,
- slower graphics performance, and
- increased memory usage.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetTessellationQuality Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetTessellationQuality.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
