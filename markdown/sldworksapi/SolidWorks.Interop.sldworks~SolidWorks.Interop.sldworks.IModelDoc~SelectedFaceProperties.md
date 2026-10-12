---
title: "SelectedFaceProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectedFaceProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectedFaceProperties.html"
---

# SelectedFaceProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectedFaceProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectedFaceProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectedFaceProperties( _
   ByVal RgbColor As System.Integer, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Shininess As System.Double, _
   ByVal Transparency As System.Double, _
   ByVal Emission As System.Double, _
   ByVal UsePartProps As System.Boolean, _
   ByVal FaceName As System.String _
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
Dim FaceName As System.String
Dim value As System.Boolean

value = instance.SelectedFaceProperties(RgbColor, Ambient, Diffuse, Specular, Shininess, Transparency, Emission, UsePartProps, FaceName)
```

### C#

```csharp
System.bool SelectedFaceProperties(
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.string FaceName
)
```

### C++/CLI

```cpp
System.bool SelectedFaceProperties(
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.String^ FaceName
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
- `FaceName`:

## VBA Syntax

See [ModelDoc::SelectedFaceProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectedFaceProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
