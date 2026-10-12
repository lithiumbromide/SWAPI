---
title: "IGetDimensions Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "IGetDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetDimensions.html"
---

# IGetDimensions Method (ILibraryFeatureData)

Gets the names and values of the specified type of dimension for this library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDimensions( _
   ByVal Type As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef DimName As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Type As System.Integer
Dim Count As System.Integer
Dim DimName As System.String
Dim value As System.Double

value = instance.IGetDimensions(Type, Count, DimName)
```

### C#

```csharp
System.double IGetDimensions(
   System.int Type,
   System.int Count,
   out System.string DimName
)
```

### C++/CLI

```cpp
System.double IGetDimensions(
   System.int Type,
   System.int Count,
   [Out] System.String^ DimName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of dimension as defined in [swLibraryFeatDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatDimensionType_e.html)
- `Count`: Number of dimensions
- `DimName`: - in-process, unmanaged C++: Pointer to an array of dimension names

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of dimension values

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ILibraryFeatureData::GetDimensionsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.html) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions.html)
[ILibraryFeatureData::OverrideDimension Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~OverrideDimension.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
