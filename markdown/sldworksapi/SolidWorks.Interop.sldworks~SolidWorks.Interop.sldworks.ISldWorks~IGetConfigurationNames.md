---
title: "IGetConfigurationNames Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetConfigurationNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames.html"
---

# IGetConfigurationNames Method (ISldWorks)

Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConfigurationNames( _
   ByVal FilePathName As System.String, _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetConfigurationNames(FilePathName, Count)
```

### C#

```csharp
System.string IGetConfigurationNames(
   System.string FilePathName,
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetConfigurationNames(
   System.String^ FilePathName,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path and file name for the SOLIDWORKS document
- `Count`: Number of configurations

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings containing the names of the configurations in this SOLIDWORKS document

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISldWorks::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetConfigurationCount.html) to get the value for Count.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetActiveConfigurationName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveConfigurationName.html)
[ISldWorks::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationNames.html)
[IModelDoc2::GetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::IGetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
