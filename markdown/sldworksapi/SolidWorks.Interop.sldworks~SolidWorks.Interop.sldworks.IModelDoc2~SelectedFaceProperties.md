---
title: "SelectedFaceProperties Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectedFaceProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFaceProperties.html"
---

# SelectedFaceProperties Method (IModelDoc2)

Sets the material property values of the selected face.

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
Dim instance As IModelDoc2
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

- `RgbColor`: Face color (see **Remarks**)
- `Ambient`: 0.0 <= Face ambient light value <= 1.0
- `Diffuse`: 0.0 < Face diffuse value <= 1.0
- `Specular`: 0.0 < Face specular value <= 1.0
- `Shininess`: 0.0 < Face shininess value <= 1.0
- `Transparency`: 0.0 <= Face transparency value <= 1.0
- `Emission`: 0.0 <= Face emission value <= 1.0
- `UsePartProps`: True if the face inherits the Part properties, false if not
- `FaceName`: Name of the face

### Return Value

True if face properties successfully changed, false if not

## VBA Syntax

See [ModelDoc2::SelectedFaceProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectedFaceProperties.html).

## Examples

[Change Color of Face (VBA)](Change_Color_of_Face_Example_VB.htm)

## Remarks

To see a color change, you must:

1. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
2. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
3. Refresh the graphics area after calling this method.

You can use the FaceName argument to set the name for this face.

If the face has a name, then this method does not change the name and returns false. This behavior is intended to prevent a program from renaming a face that is referenced in some other location.

For example, if an assembly contains a mate to a face on a part, then a name is automatically assigned to that face. If you change that name, then there is no guarantee that the mate will still be valid. Therefore, when using entity names, you should first check to see if the entity is already named, and, if so, use the existing name. If no name exists for the face, then you can assign the face a name.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SelectedEdgeProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedEdgeProperties.html)
[IModelDoc2::SelectedFeatureProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFeatureProperties.html)
[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IModelDoc2::EntityProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EntityProperties.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
