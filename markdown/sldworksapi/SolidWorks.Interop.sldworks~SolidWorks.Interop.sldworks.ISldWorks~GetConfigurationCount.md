---
title: "GetConfigurationCount Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetConfigurationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationCount.html"
---

# GetConfigurationCount Method (ISldWorks)

Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationCount( _
   ByVal FilePathName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim value As System.Integer

value = instance.GetConfigurationCount(FilePathName)
```

### C#

```csharp
System.int GetConfigurationCount(
   System.string FilePathName
)
```

### C++/CLI

```cpp
System.int GetConfigurationCount(
   System.String^ FilePathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path and file name for the SOLIDWORKS document

### Return Value

Number of configurations in SOLIDWORKS document

## VBA Syntax

See [SldWorks::GetConfigurationCount](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetConfigurationCount.html).

## Examples

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

Call this method before calling [ISldWorks::IGetConfigurationNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetConfigurationNames.html) to get the size of the array for that method.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationNames.html)
[ISldWorks::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames.html)
[ISldWorks::GetActiveConfigurationName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveConfigurationName.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
