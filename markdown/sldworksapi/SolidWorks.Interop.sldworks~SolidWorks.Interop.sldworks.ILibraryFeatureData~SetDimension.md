---
title: "SetDimension Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "SetDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetDimension.html"
---

# SetDimension Method (ILibraryFeatureData)

Sets a dimension's type, name, and value for the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDimension( _
   ByVal Type As System.Integer, _
   ByVal DimName As System.String, _
   ByVal DimVal As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim Type As System.Integer
Dim DimName As System.String
Dim DimVal As System.Double
Dim value As System.Boolean

value = instance.SetDimension(Type, DimName, DimVal)
```

### C#

```csharp
System.bool SetDimension(
   System.int Type,
   System.string DimName,
   System.double DimVal
)
```

### C++/CLI

```cpp
System.bool SetDimension(
   System.int Type,
   System.String^ DimName,
   System.double DimVal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of dimension as defined in [swLibFeatDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatDimensionType_e.html)
- `DimName`: Name of dimension
- `DimVal`: Name of dimension

### Return Value

True is the dimension is set, false if not

## VBA Syntax

See [LibraryFeatureData::SetDimension](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~SetDimension.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions.html)
[ILibraryFeatureData::GetDimensionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.html)
[ILibraryFeatureData::IGetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetDimensions.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
