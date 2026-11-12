---
title: "MaterialPropertyValues Property (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "MaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html"
---

# MaterialPropertyValues Property (IPartDoc)

Gets or sets a material's properties in the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialPropertyValues As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
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

Array of doubles describing the material's values (see **Remarks**)

## VBA Syntax

See [PartDoc::MaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~MaterialPropertyValues.html).

## Remarks

The material values include the color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency and emission.

The format of the parameters or return values is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

To see a color change, you must:

1. Specify `R`, `G`, and `B`, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after setting this property.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.html)
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html)
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html)
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.html)
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.html)
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.html)
