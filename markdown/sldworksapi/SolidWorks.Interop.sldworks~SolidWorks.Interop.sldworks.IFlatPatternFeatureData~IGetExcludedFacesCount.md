---
title: "IGetExcludedFacesCount Method (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "IGetExcludedFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFacesCount.html"
---

# IGetExcludedFacesCount Method (IFlatPatternFeatureData)

Gets the number of faces that are excluded from this Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetExcludedFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Integer

value = instance.IGetExcludedFacesCount()
```

### C#

```csharp
System.int IGetExcludedFacesCount()
```

### C++/CLI

```cpp
System.int IGetExcludedFacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of excluded faces

## VBA Syntax

See [FlatPatternFeatureData::IGetExcludedFacesCount](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~IGetExcludedFacesCount.html).

## Remarks

Call this method to get the size of the array returned by [IFlatPatternFeatureData::IGetExcludedFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFaces.html) and [IFlatPatternFeatureData::ExcludedFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFeatureData~ExcludedFaces.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::ISetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ISetExcludedFaces.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20
