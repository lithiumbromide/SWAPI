---
title: "GetActiveConfigurationName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetActiveConfigurationName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveConfigurationName.html"
---

# GetActiveConfigurationName Method (ISldWorks)

Gets the name of the active configuration in the specified SOLIDWORKS document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActiveConfigurationName( _
   ByVal FilePathName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim value As System.String

value = instance.GetActiveConfigurationName(FilePathName)
```

### C#

```csharp
System.string GetActiveConfigurationName(
   System.string FilePathName
)
```

### C++/CLI

```cpp
System.String^ GetActiveConfigurationName(
   System.String^ FilePathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path for the SOLIDWORKS document

### Return Value

Name of the active configuration

## VBA Syntax

See [SldWorks::GetActiveConfigurationName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetActiveConfigurationName.html).

## Examples

[Get Name of Active Configuration (VBA)](Get_Name_of_Active_Configuration_Example_VB.htm)

## Remarks

The SOLIDWORKS document does not need to be open. The configuration that was active when the SOLIDWORKS document was closed is returned. If the SOLIDWORKS document is open, then the name of the active configuration is returned.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationCount.html)
[ISldWorks::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetConfigurationNames.html)
[ISldWorks::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetConfigurationNames.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
