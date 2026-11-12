---
title: "GetDimensions Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions.html"
---

# GetDimensions Method (ILibraryFeatureData)

Gets the names and values of the specified type of dimension for this library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimensions( _
   ByVal Type As System.Integer, _
   ByRef DimName As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Type As System.Integer
Dim DimName As System.Object
Dim value As System.Object

value = instance.GetDimensions(Type, DimName)
```

### C#

```csharp
System.object GetDimensions(
   System.int Type,
   out System.object DimName
)
```

### C++/CLI

```cpp
System.Object^ GetDimensions(
   System.int Type,
   [Out] System.Object^ DimName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of dimension as defined in [swLibFeatDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatDimensionType_e.html)
- `DimName`: Array of the dimension names

### Return Value

Array of the values of the dimensions

## VBA Syntax

See [LibraryFeatureData::GetDimensions](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetDimensions.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::IGetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetDimensions.html)
[ILibraryFeatureData::GetDimensionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.html)
[ILibraryFeatureData::OverrideDimension Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~OverrideDimension.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
