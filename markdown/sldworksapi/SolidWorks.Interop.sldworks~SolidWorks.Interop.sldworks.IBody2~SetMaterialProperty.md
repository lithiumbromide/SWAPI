---
title: "SetMaterialProperty Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetMaterialProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html"
---

# SetMaterialProperty Method (IBody2)

Sets the material for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialProperty( _
   ByVal ConfigName As System.String, _
   ByVal Database As System.String, _
   ByVal MaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ConfigName As System.String
Dim Database As System.String
Dim MaterialName As System.String
Dim value As System.Integer

value = instance.SetMaterialProperty(ConfigName, Database, MaterialName)
```

### C#

```csharp
System.int SetMaterialProperty(
   System.string ConfigName,
   System.string Database,
   System.string MaterialName
)
```

### C++/CLI

```cpp
System.int SetMaterialProperty(
   System.String^ ConfigName,
   System.String^ Database,
   System.String^ MaterialName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of configuration
- `Database`: "solidworks material.sldmat" or **""** or "custom materials.sldmat" (see **Remarks**)
- `MaterialName`: Name of the SOLIDWORKS material to apply to the body (see **Remarks**)

### Return Value

Return status as defined by [swBodyMaterialApplicationError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyMaterialApplicationError_e.html)

## VBA Syntax

See [Body2::SetMaterialProperty](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetMaterialProperty.html).

## Examples

[Set Material (C#)](Set_Material_Example_CSharp.htm)
[Set Material (VB.NET)](Set_Material_Example_VBNET.htm)
[Set Material (VBA)](Set_Material_Example_VB.htm)

## Remarks

Click **Tools > Options > System Options > File Locations > Material Databases** to verify that a folder for Database is specified.

You can only use materials from a valid SOLIDWORKS materials database. You can specify either "solidworks materials.sldmat" or "" for the SOLIDWORKS Materials database or "custom materials.sldmat" for the Custom Materials database.

You can also find out the names of the materials in the materials database by opening the database as an XML stream and work with the XML API to get the data.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialPropertyName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.html)
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.html)
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html)
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html)
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)
[IBody2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
