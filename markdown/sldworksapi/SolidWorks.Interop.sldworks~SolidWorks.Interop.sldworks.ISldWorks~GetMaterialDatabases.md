---
title: "GetMaterialDatabases Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetMaterialDatabases"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabases.html"
---

# GetMaterialDatabases Method (ISldWorks)

Gets the names of the material databases.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialDatabases() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetMaterialDatabases()
```

### C#

```csharp
System.object GetMaterialDatabases()
```

### C++/CLI

```cpp
System.Object^ GetMaterialDatabases();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of the names of the material databases

## VBA Syntax

See [SldWorks::GetMaterialDatabases](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetMaterialDatabases.html).

## Examples

[Get Material Database and XML Schema File Names (VBA)](Get_Material_Database_and_XML_Schema_File_Names_Example_VB.htm)
[Get Material Database Paths of Document (VBA)](Get_Material_Database_Paths_of_Document_Example_VB.htm)
[Set Material (C#)](Set_Material_Example_CSharp.htm)
[Set Material (VB.NET)](Set_Material_Example_VBNET.htm)
[Set Material (VBA)](Set_Material_Example_VB.htm)

## Remarks

Material database names must be unique. Do not re-use the name of a material database.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetMaterialDatabaseCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabaseCount.html)
[ISldWorks::IGetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMaterialDatabases.html)
[ISldWorks::GetMaterialSchemaPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialSchemaPathName.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
