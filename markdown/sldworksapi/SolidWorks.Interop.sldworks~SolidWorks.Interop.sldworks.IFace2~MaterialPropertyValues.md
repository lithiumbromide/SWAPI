---
title: "MaterialPropertyValues Property (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "MaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialPropertyValues.html"
---

# MaterialPropertyValues Property (IFace2)

Gets or sets the material properties for the selected face in the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialPropertyValues As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
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

Array of doubles describing the material values on this face (see **Remarks**)

## VBA Syntax

See [Face2::MaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Face2~MaterialPropertyValues.html).

## Examples

[Get Faces Associated with Feature (C#)](Get_Faces_Associated_with_Feature_Example_CSharp.htm)
[Get Faces Associated with Feature (VB.NET)](Get_Faces_Associated_with_Feature_Example_VBNET.htm)
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)

## Remarks

The material values include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency and emission. All values can be from 0 to 1.

This method returns a NULL VARIANT (or an S_false HRESULT for COM implementations) if this face has not been explicitly modified from the material property values of the body. If you create a body and change the body color to red, then [IFace2::IGetMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetMaterialPropertyValues2.html) and [IFace2::GetMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetMaterialPropertyValues2.html) return a NULL array because you did not specifically change the values of the face.

The format of the parameters or return values is an array of doubles as follows:

```vb
[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]
```

To see a color change, you must:

1. Specify `R`, `G`, and `B`, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after setting this property.

To reset the face to use the default part material properties, use [IModelDoc2::SelectedFaceProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectedFaceProperties.html).

This method does not support faces obtained from reference surface bodies.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IMaterialPropertyValues.html)
[IFace2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetMaterialPropertyValues2.html)
[IFace2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveMaterialProperty2.html)
[IFace2::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ISetMaterialPropertyValues2.html)
[IFace2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveMaterialProperty2.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)
[IComponent2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IMaterialPropertyValues.html)
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html)
[IModelDoc2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMaterialPropertyValues.html)
[IModelDoc2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialPropertyValues.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IFace2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
