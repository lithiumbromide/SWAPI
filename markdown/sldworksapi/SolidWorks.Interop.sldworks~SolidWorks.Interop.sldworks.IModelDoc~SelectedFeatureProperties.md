---
title: "SelectedFeatureProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectedFeatureProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectedFeatureProperties.html"
---

# SelectedFeatureProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectedFeatureProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectedFeatureProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectedFeatureProperties( _
   ByVal RgbColor As System.Integer, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Shininess As System.Double, _
   ByVal Transparency As System.Double, _
   ByVal Emission As System.Double, _
   ByVal UsePartProps As System.Boolean, _
   ByVal Suppressed As System.Boolean, _
   ByVal FeatureName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim RgbColor As System.Integer
Dim Ambient As System.Double
Dim Diffuse As System.Double
Dim Specular As System.Double
Dim Shininess As System.Double
Dim Transparency As System.Double
Dim Emission As System.Double
Dim UsePartProps As System.Boolean
Dim Suppressed As System.Boolean
Dim FeatureName As System.String
Dim value As System.Boolean

value = instance.SelectedFeatureProperties(RgbColor, Ambient, Diffuse, Specular, Shininess, Transparency, Emission, UsePartProps, Suppressed, FeatureName)
```

### C#

```csharp
System.bool SelectedFeatureProperties(
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.bool Suppressed,
   System.string FeatureName
)
```

### C++/CLI

```cpp
System.bool SelectedFeatureProperties(
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.bool Suppressed,
   System.String^ FeatureName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RgbColor`:
- `Ambient`:
- `Diffuse`:
- `Specular`:
- `Shininess`:
- `Transparency`:
- `Emission`:
- `UsePartProps`:
- `Suppressed`:
- `FeatureName`:

## VBA Syntax

See [ModelDoc::SelectedFeatureProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectedFeatureProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
