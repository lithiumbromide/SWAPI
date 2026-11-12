---
title: "OverrideDimension Property (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "OverrideDimension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~OverrideDimension.html"
---

# OverrideDimension Property (ILibraryFeatureData)

Gets or sets whether to override the existing size dimension values of the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDimension As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim value As System.Boolean

instance.OverrideDimension = value

value = instance.OverrideDimension
```

### C#

```csharp
System.bool OverrideDimension {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideDimension {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the existing size dimensions values of the library feature, false to not

## VBA Syntax

See [LibraryFeatureData::OverrideDimension](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~OverrideDimension.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions.html)
[ILibraryFeatureData::GetDimensionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.html)
[ILibraryFeatureData::IGetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetDimensions.html)
[ILibraryFeatureData::SetDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetDimension.html)
[ILibraryFeatureData::ConfigurationName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ConfigurationName.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
