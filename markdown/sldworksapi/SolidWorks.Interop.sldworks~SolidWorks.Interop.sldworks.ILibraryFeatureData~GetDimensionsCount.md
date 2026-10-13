---
title: "GetDimensionsCount Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetDimensionsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.html"
---

# GetDimensionsCount Method (ILibraryFeatureData)

Gets the number of dimensions of the specified type for this library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimensionsCount( _
   ByVal Type As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Type As System.Integer
Dim value As System.Integer

value = instance.GetDimensionsCount(Type)
```

### C#

```csharp
System.int GetDimensionsCount(
   System.int Type
)
```

### C++/CLI

```cpp
System.int GetDimensionsCount(
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of dimension as defined in [swLibraryFeatDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatDimensionType_e.html)

### Return Value

Number of dimensions

## VBA Syntax

See [LibraryFeatureData::GetDimensionsCount](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetDimensionsCount.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

Call this method before calling [ILibraryFeatureData::IGetDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~IGetDimensions.html) to determine the size of the size of the array.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions.html)
[ILibraryFeatureData::OverrideDimension Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~OverrideDimension.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
