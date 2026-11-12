---
title: "IGetAllConfigurationNames Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "IGetAllConfigurationNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames.html"
---

# IGetAllConfigurationNames Method (ILibraryFeatureData)

Gets the names of the library feature configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllConfigurationNames( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetAllConfigurationNames(Count)
```

### C#

```csharp
System.string IGetAllConfigurationNames(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetAllConfigurationNames(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of library configurations

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the library feature configurations

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ILibraryFeatureData::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~GetConfigurationCount.html) to determine the size of the array.

If the library feature part document is not open or the library feature is not linked to the library feature part, then only the name of the active library feature configuration is returned.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetAllConfigurationNames.html)
[ILibraryFeatureData::ConfigurationName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ConfigurationName.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
