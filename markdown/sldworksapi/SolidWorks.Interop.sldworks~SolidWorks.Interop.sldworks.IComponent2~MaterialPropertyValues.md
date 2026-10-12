---
title: "MaterialPropertyValues Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "MaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html"
---

# MaterialPropertyValues Property (IComponent2)

Gets or sets the material properties for the selected component in the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialPropertyValues As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

instance.MaterialPropertyValues = value

value = instance.MaterialPropertyValues
```

### C#

```csharp
System.object MaterialPropertyValues {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MaterialPropertyValues {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles that describes the material values on this component (see **Remarks**)

## VBA Syntax

See [Component2::MaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Component2~MaterialPropertyValues.html).

## Examples

[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)
[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)

## Remarks

The material values include the component color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are from 0 to 1 for all values.

The format of the parameters or return values is an array of doubles as follows:

**[** `R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission` **]**

To see a color change, you must:

1. Specify `R`, `G`, and `B`, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after setting this property.

This method returns a NULL VARIANT if the user has not explicitly modified this component from the material property values of the underlying part document. For example, the user can right-click a component in the FeatureManager design tree and select **Component Properties** to change the color. If the user has not done this, then this method returns NULL color information.

The default component color can be obtained from the component's [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object ([IComponent2::GetModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelDoc.html)) using IModelDoc2::MaterialPropertyValues.

You might also want to check for specific face colors using [IFace2::MaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~MaterialPropertyValues.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IMaterialPropertyValues.html)
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)
[IComponent2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.html)
[IComponent2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IRemoveMaterialProperty2.html)
[IComponent2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.html)
[IComponent2::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.html)
[IComponent2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.html)
[IComponent2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
