---
title: "MaterialPropertyValues2 Property (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "MaterialPropertyValues2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html"
---

# MaterialPropertyValues2 Property (IBody2)

Gets or sets the material properties for a body other than the base body in the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialPropertyValues2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

instance.MaterialPropertyValues2 = value

value = instance.MaterialPropertyValues2
```

### C#

```csharp
System.object MaterialPropertyValues2 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MaterialPropertyValues2 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Body2::MaterialPropertyValues2](ms-its:sldworksapivb6.chm::/sldworks~Body2~MaterialPropertyValues2.html).

## Examples

[Get Material Property Values (VBA)](Get_Material_Property_Values_Example_VB.htm)

## Remarks

The material values include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid settings are from 0 to 1 for all values.

This property is intended to be used on bodies other than the base body and should follow a call to [IPartDoc::EnumRelatedBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumRelatedBodies2.html). The format of the parameters or return values is an array of 9 doubles as follows:

**[** `R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission` **]**

To see a color change, you must:

1. Specify `R`, `G`, and `B`, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after setting this property.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html)
[IFace2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialPropertyValues.html)
[IModelDoc2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialPropertyValues.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialPropertyName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.html)
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.html)
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html)
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html)
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.html)
[IBody2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.html)
[IBody2::Display3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
