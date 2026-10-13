---
title: "GetTessellationQuality Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetTessellationQuality"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetTessellationQuality.html"
---

# GetTessellationQuality Method (IModelDoc2)

Gets the shaded-display image quality number for the current document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessellationQuality() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetTessellationQuality()
```

### C#

```csharp
System.int GetTessellationQuality()
```

### C++/CLI

```cpp
System.int GetTessellationQuality();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

0 < Shaded-display image quality number < 106 (see **Remarks**)

## VBA Syntax

See [ModelDoc2::GetTessellationQuality](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetTessellationQuality.html).

## Remarks

This method returns a number (`QualityNum`) that corresponds to the degree of tessellation of curved surfaces for shaded rendering output. **Tools > Options > Document Properties > Image Quality** includes a field that sets the maximum chordal deviation. `QualityNum` and the maximum chordal deviation (in meters) are coupled and inversely proportional as follows:

`var` = `TessMin` + `QualityNum`*((`TessMax`-`TessMin`)/100)

`Deviation` = 0.025 * (`BodyDiameter` * 2) / `var`;

where:

- `TessMin` = 6
- `TessMax` = 166
- 0 < `QualityNum` (returned by this method) < 106
- `BodyDiameter` is the diagonal distance across the bounds of the part box. See [IPartDoc::GetPartBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetPartBox.html) or [IPartDoc::IGetPartBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IGetPartBox.html) for more information.

You can also get the maximum chordal deviation using [swUserPreferencesDouble_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceDoubleValue_e.html).swImageQualityShadedDeviation.

To get the image quality number, use [swUserPreferenceInteger_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).swImageQualityShaded.

**NOTE:** [Setting the degree of tessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetTessellationQuality.html) to a higher value results in:

- finer tessellation,
- increased file size,
- slower graphics performance, and
- increased memory usage.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
