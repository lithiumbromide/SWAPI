---
title: "GetConfigurationNames Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetConfigurationNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationNames.html"
---

# GetConfigurationNames Method (ISldWorks)

Gets the names of the configuration in this SOLIDWORKS Design document, whether the document is opened or closed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationNames( _
   ByVal FilePathName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim value As System.Object

value = instance.GetConfigurationNames(FilePathName)
```

### C#

```csharp
System.object GetConfigurationNames(
   System.string FilePathName
)
```

### C++/CLI

```cpp
System.Object^ GetConfigurationNames(
   System.String^ FilePathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path and file name for the SOLIDWORKS Design document

### Return Value

Array of strings containing the names of the configurations in this SOLIDWORKS Design document

## VBA Syntax

See [SldWorks::GetConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetConfigurationNames.html).

## Examples

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetActiveConfigurationName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveConfigurationName.html)
[ISldWorks::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationCount.html)
[ISldWorks::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
