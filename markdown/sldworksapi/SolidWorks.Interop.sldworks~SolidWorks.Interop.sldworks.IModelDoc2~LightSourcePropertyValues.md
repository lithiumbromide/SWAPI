---
title: "LightSourcePropertyValues Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "LightSourcePropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html"
---

# LightSourcePropertyValues Property (IModelDoc2)

Gets and sets the light source property values.

## Syntax

### Visual Basic (Declaration)

```vb
Property LightSourcePropertyValues( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ID As System.Integer
Dim value As System.Object

instance.LightSourcePropertyValues(ID) = value

value = instance.LightSourcePropertyValues(ID)
```

### C#

```csharp
System.object LightSourcePropertyValues(
   System.int ID
) {get; set;}
```

### C++/CLI

```cpp
property System.Object^ LightSourcePropertyValues {
   System.Object^ get(System.int ID);
   void set (System.int ID, System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Light source ID

### Property Value

Array of 19 doubles containing the light source properties (see **Remarks**)

## VBA Syntax

See [ModelDoc2::LightSourcePropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~LightSourcePropertyValues.html).

## Examples

[Redirect Spotlight (VBA)](Redirect_Spotlight_Example_VB.htm)
[Turn Lights On (VBA)](Turn_Lights_On_Example_VB.htm)

## Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use [IModelDoc2::GetLightSourceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceCount.html).

The return values for this property is the following array of 19 doubles:

[ type, Intensity, Color[3], Position[3], Direction[3], coneAngle, falloff[3], Ambient, Specular, isDisabled, SpotExponent ]

where:

- type = an integer packed into a double that represents the light source type where valid types are taken from openGL definitions (LIGHT_EYE, LIGHT_AMBIENT, LIGHT_SPOT, LIGHT_POINT, LIGHT_DISTANT)
- Intensity = Light-source intensity (diffuseness) where values range from 0 to 1.
- Color[3] = Light-source color in the form of an array of 3 doubles (R, G, B) where values range from 0 to 1.
- Position[3] = Light-source position for spot lights in the form of an array of 3 doubles (X, Y, Z) in model space.
- Direction[3] = Light-source direction in the form of an array of 3 doubles (i, j, k)
- coneAngle = Light-source cone half angle in degrees where valid values are from 0 to 90 and 180.
- falloff[3] = Light-source falloff in the form of an array of 3 doubles (Kc, Kl, Kq). These values result in changes in light intensity as the distance between the light position and the vertex change.

  **NOTE:** The falloff[3] values are not supported in SOLIDWORKS 2011 and later.

  The result is driven by the following equation:

[ 1 / (Kc + D*Kl + D*D*Kq ) ]

where:

D = the distance.between the light's position and the vertex

Kc = constant attenuation

Kl = linear attenuation

Kq = quadratic attenuation

- Ambient = light-source ambient Intensity
- Specular = light-source specular Intensity
- isDisabled = an integer packed into a double. True means that the light is disabled and false means the light is not disabled.
- SpotExponent = spot exponent

  **NOTE:** The SpotExponent value is not supported in SOLIDWORKS 2011 and later.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ILightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html)
[IModelDoc2::LightSourceUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.html)
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.html)
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html)
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.html)
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.html)
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.html)
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.html)
[IModelDoc2::SetLightSourcePropertyValuesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html)
[IModelDocExtension::GetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues.html)
[IModelDocExtension::SetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
