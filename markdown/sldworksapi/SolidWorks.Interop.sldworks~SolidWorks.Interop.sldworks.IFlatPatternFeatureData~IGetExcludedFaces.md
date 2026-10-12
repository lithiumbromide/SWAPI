---
title: "IGetExcludedFaces Method (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "IGetExcludedFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFaces.html"
---

# IGetExcludedFaces Method (IFlatPatternFeatureData)

Gets the faces that are excluded from this Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetExcludedFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Object

value = instance.IGetExcludedFaces()
```

### C#

```csharp
System.object IGetExcludedFaces()
```

### C++/CLI

```cpp
System.Object^ IGetExcludedFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IFace2s](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To get the size of the array returned by this method, call [IFlatPatternFeatureData::IGetExcludedFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFacesCount.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::ExcludedFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ExcludedFaces.html)
[IFlatPatternFeatureData::ISetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ISetExcludedFaces.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20
