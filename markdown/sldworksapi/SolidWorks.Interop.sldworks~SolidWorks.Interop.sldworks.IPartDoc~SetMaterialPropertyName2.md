---
title: "SetMaterialPropertyName2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetMaterialPropertyName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html"
---

# SetMaterialPropertyName2 Method (IPartDoc)

Sets the name of the material property for the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaterialPropertyName2( _
   ByVal ConfigName As System.String, _
   ByVal Database As System.String, _
   ByVal Name As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ConfigName As System.String
Dim Database As System.String
Dim Name As System.String

instance.SetMaterialPropertyName2(ConfigName, Database, Name)
```

### C#

```csharp
void SetMaterialPropertyName2(
   System.string ConfigName,
   System.string Database,
   System.string Name
)
```

### C++/CLI

```cpp
void SetMaterialPropertyName2(
   System.String^ ConfigName,
   System.String^ Database,
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of configuration
- `Database`: Name of the material database (see **Remarks**)
- `Name`: Name of material (see **Remarks**)

## VBA Syntax

See [PartDoc::SetMaterialPropertyName2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetMaterialPropertyName2.html).

## Examples

[Get and Set Material Visual Properties (VBA)](Get_and_Set_Material_Visual_Properties_Example_VB.htm)
[Get and Set Material Visual Properties (VB.NET)](Get_and_Set_Material_Visual_Properties_Example_VBNET.htm)
[Get and Set Material Visual Properties (C#)](Get_and_Set_Material_Visual_Properties_Example_CSharp.htm)

## Remarks

This method only supports parts.

Click **Tools > Options > System Options > File Locations > Material Databases** to verify that a folder for Database is specified.

If Database is an empty string, then the default sldmaterials is used. Otherwise, specify the material database file name with the .sldmat filename extension. For example:

PartDoc.SetMaterialPropertyName2 "AddHoles", "solidworks materials.sldmat", "Alloy Steel"

- or -

PartDoc.SetMaterialPropertyName2 "AddHoles", "c:\Program Files\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Alloy Steel"

To remove a material, pass an empty string to Name.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.html)
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.html)
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
