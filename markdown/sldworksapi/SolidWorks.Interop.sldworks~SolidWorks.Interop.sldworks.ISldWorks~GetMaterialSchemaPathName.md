---
title: "GetMaterialSchemaPathName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetMaterialSchemaPathName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialSchemaPathName.html"
---

# GetMaterialSchemaPathName Method (ISldWorks)

Gets the path for the XML material schema file.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialSchemaPathName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

value = instance.GetMaterialSchemaPathName()
```

### C#

```csharp
System.string GetMaterialSchemaPathName()
```

### C++/CLI

```cpp
System.String^ GetMaterialSchemaPathName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Path for the XML material schema file

## VBA Syntax

See [SldWorks::GetMaterialSchemaPathName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetMaterialSchemaPathName.html).

## Examples

[Get Material Database and XML Schema File Names (VBA)](Get_Material_Database_and_XML_Schema_File_Names_Example_VB.htm)
[Set Material (C#)](Set_Material_Example_CSharp.htm)
[Set Material (VB.NET)](Set_Material_Example_VBNET.htm)
[Set Material (VBA)](Set_Material_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMaterialDatabases.html)
[ISldWorks::GetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabases.html)
[ISldWorks::GetMaterialDatabaseCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabaseCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
