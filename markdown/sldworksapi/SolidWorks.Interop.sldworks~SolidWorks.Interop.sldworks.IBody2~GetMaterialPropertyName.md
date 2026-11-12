---
title: "GetMaterialPropertyName Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetMaterialPropertyName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html"
---

# GetMaterialPropertyName Method (IBody2)

Gets the names of the material database and the material for the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialPropertyName( _
   ByVal ConfigName As System.String, _
   ByRef Database As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ConfigName As System.String
Dim Database As System.String
Dim value As System.String

value = instance.GetMaterialPropertyName(ConfigName, Database)
```

### C#

```csharp
System.string GetMaterialPropertyName(
   System.string ConfigName,
   out System.string Database
)
```

### C++/CLI

```cpp
System.String^ GetMaterialPropertyName(
   System.String^ ConfigName,
   [Out] System.String^ Database
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of configuration (see **Remarks**)
- `Database`: Name of material database

### Return Value

Name of material

## VBA Syntax

See [Body2::GetMaterialPropertyName](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetMaterialPropertyName.html).

## Examples

[Set Material (C#)](Set_Material_Example_CSharp.htm)
[Set Material (VB.NET)](Set_Material_Example_VBNET.htm)
[Set Material (VBA)](Set_Material_Example_VB.htm)

## Remarks

This method gets the name of the material database and an entry in the material database that you need for the XML lookup. Open the database as an XML stream and work with the XML API to get the data.

| If... | Then... |
| --- | --- |
| Only the Default configuration exists for the part | Use "" for ConfigName |
| A material was not applied to the configuration | Database name and return value are blank |

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.html)
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.html)
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html)
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html)
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)
[IBody2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
