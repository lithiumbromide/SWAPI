---
title: "SelectedFeatureProperties Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectedFeatureProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFeatureProperties.html"
---

# SelectedFeatureProperties Method (IModelDoc2)

Sets the property values of the selected feature.

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
Dim instance As IModelDoc2
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

- `RgbColor`: Color of feature (see **Remarks**)
- `Ambient`: 0.0 <= Ambient value <= 1.0
- `Diffuse`: 0.0 < Diffuse value <= 1.0
- `Specular`: 0.0 < Specular value <= 1.0
- `Shininess`: 0.0 < Shininess value <= 1.0
- `Transparency`: 0.0 <= Transparency value <= 1.0
- `Emission`: 0.0 <= Emission value <= 1.0
- `UsePartProps`: True if the feature inherits the properties from the part, false if not
- `Suppressed`: True if the feature is suppressed, false if not
- `FeatureName`: Name of the feature

### Return Value

True if feature's properties are successfully set, false if not

## VBA Syntax

See [ModelDoc2::SelectedFeatureProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectedFeatureProperties.html).

## Examples

[Create Thicken Feature (VBA)](Create_Thicken_Feature_Example_VB.htm)

## Remarks

To see a color change, you must:

1. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
2. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
3. Refresh the graphics area after calling this method.

This method is different from [IModelDodc2::SelectedEdgeProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectedEdgeProperties.html) and [IModelDoc2::SelectedFaceProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectedFaceProperties.html) in that it allows you to change the name of this feature. All features have names; however, a face or edge typically has a name only if it is being referenced. Because it is dangerous to change the name of a referenced object, you cannot programmatically change the names of faces or edges. See [IFeature::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Name.html) and [IPartDoc::SetEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SetEntityName.html) for additional information.

This method requires that the feature to be selected. To select the feature programmatically, you can use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and pass in the feature name and the appropriate object type (for example, "BODYFEATURE", "ATTRIBUTE", "PLANE", "SKETCH", and so on) and the selection coordinates 0,0,0. To determine the feature name and object type, use the [IFeature::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Name.html) and [IFeature::GetTypeName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName.html) methods, respectively.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
