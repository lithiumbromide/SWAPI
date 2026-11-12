---
title: "GetMaterialPropertyName2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetMaterialPropertyName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.html"
---

# GetMaterialPropertyName2 Method (IPartDoc)

Gets the names of the material database and the material for the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialPropertyName2( _
   ByVal ConfigName As System.String, _
   ByRef Database As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ConfigName As System.String
Dim Database As System.String
Dim value As System.String

value = instance.GetMaterialPropertyName2(ConfigName, Database)
```

### C#

```csharp
System.string GetMaterialPropertyName2(
   System.string ConfigName,
   out System.string Database
)
```

### C++/CLI

```cpp
System.String^ GetMaterialPropertyName2(
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

See [PartDoc::GetMaterialPropertyName2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetMaterialPropertyName2.html).

## Examples

[Get Material Database Paths of Document (VBA)](Get_Material_Database_Paths_of_Document_Example_VB.htm)
[Get Material (VBA)](Get_Material_Example_VB.htm)

## Remarks

This method gets the name of the material database and an entry in the material database that you need for the XML lookup. Open the database as an XML stream and work with the XML API to get the data.

| If... | Then... |
| --- | --- |
| Only the default configuration exists for the part | Use "" for ConfigName |
| A material was not applied to the configuration | Database name and return value are blank |

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.html)
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html)
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.html)
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
