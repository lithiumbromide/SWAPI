---
title: "GetAllConfigurationNames Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetAllConfigurationNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetAllConfigurationNames.html"
---

# GetAllConfigurationNames Method (ILibraryFeatureData)

Gets the names of the library feature configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllConfigurationNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim value As System.Object

value = instance.GetAllConfigurationNames()
```

### C#

```csharp
System.object GetAllConfigurationNames()
```

### C++/CLI

```cpp
System.Object^ GetAllConfigurationNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Names of the library feature configurations

## VBA Syntax

See [LibraryFeatureData::GetAllConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetAllConfigurationNames.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

If the library feature part document is not open or the library feature is not linked to the library feature part, then only the name of the active library feature configuration is returned.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::IGetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames.html)
[ILibraryFeatureData::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetConfigurationCount.html)
[ILibraryFeatureData::ConfigurationName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ConfigurationName.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
