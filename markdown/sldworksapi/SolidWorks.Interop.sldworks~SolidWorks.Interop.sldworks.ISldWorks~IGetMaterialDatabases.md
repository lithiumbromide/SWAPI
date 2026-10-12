---
title: "IGetMaterialDatabases Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetMaterialDatabases"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMaterialDatabases.html"
---

# IGetMaterialDatabases Method (ISldWorks)

Gets the names of the material databases.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaterialDatabases( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetMaterialDatabases(Count)
```

### C#

```csharp
System.string IGetMaterialDatabases(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetMaterialDatabases(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of material databases

### Return Value

- in-process, unmanaged C++: Pointer to the an array of the names of the material databases
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISldWorks::GetMaterialDatabaseCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetMaterialDatabaseCount.html) to get the value for Count.

Material database names must be unique. Do not re-use the name of a material database.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetMaterialDatabases Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMaterialDatabases.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
