---
title: "MaterialIdName Property (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "MaterialIdName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.html"
---

# MaterialIdName Property (IPartDoc)

Gets or sets the material name.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialIdName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.String

instance.MaterialIdName = value

value = instance.MaterialIdName
```

### C#

```csharp
System.string MaterialIdName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialIdName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Material name (see **Remarks**)

## VBA Syntax

See [PartDoc::MaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~MaterialIdName.html).

## Examples

[Get Material Property Names (VBA)](Get_Material_Property_Names_Example_VB.htm)
[Set Material Property Name (VBA)](Set_Material_Property_Name_Example_VB.htm)

## Remarks

This property returns a string that contains three pieces of information separated by a pipe "|":

- Database name
- Material name
- Database ID of material

Example:

MY MATERIALS|1.0038 (S235JR)|277

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.html)
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.html)
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html)
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html)
