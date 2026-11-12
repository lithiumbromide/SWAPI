---
title: "GetConfigurationCount Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetConfigurationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetConfigurationCount.html"
---

# GetConfigurationCount Method (ILibraryFeatureData)

Gets the number of library feature configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim value As System.Integer

value = instance.GetConfigurationCount()
```

### C#

```csharp
System.int GetConfigurationCount()
```

### C++/CLI

```cpp
System.int GetConfigurationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of library feature configurations

## VBA Syntax

See [LibraryFeatureData::GetConfigurationCount](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetConfigurationCount.html).

## Remarks

Call this method before calling [ILibraryFeatureData::IGetAllConfigurationNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames.html).

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetAllConfigurationNames.html)
[ILibraryFeatureData::IGetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames.html)
[ILibraryFeatureData::ConfigurationName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ConfigurationName.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
