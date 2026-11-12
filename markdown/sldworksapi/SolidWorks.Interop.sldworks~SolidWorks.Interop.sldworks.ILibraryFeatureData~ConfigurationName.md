---
title: "ConfigurationName Property (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "ConfigurationName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ConfigurationName.html"
---

# ConfigurationName Property (ILibraryFeatureData)

Gets or sets the name of the active library feature configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim value As System.String

instance.ConfigurationName = value

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of active library feature configuration

## VBA Syntax

See [LibraryFeatureData::ConfigurationName](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~ConfigurationName.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

If the size dimensions are overridden, then the get version of this property returns an empty string.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetAllConfigurationNames.html)
[ILibraryFeatureData::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetConfigurationCount.html)
[ILibraryFeatureData::IGetAllConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetAllConfigurationNames.html)
[ILibraryFeatureData::OverrideDimension Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~OverrideDimension.html)
[ILibraryFeatureData::GetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions.html)
[ILibraryFeatureData::GetDimensionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.html)
[ILibraryFeatureData::IGetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetDimensions.html)
[ILibraryFeatureData::SetDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetDimension.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
