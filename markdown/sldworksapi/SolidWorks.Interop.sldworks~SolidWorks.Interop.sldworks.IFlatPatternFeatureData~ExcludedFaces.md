---
title: "ExcludedFaces Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "ExcludedFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ExcludedFaces.html"
---

# ExcludedFaces Property (IFlatPatternFeatureData)

Gets and sets the faces to exclude from this Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludedFaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Object

instance.ExcludedFaces = value

value = instance.ExcludedFaces
```

### C#

```csharp
System.object ExcludedFaces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ExcludedFaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IFace2s](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [FlatPatternFeatureData::ExcludedFaces](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~ExcludedFaces.html).

## Examples

[Exclude Faces Before Flattening (VBA)](Exclude_Faces_Before_Flattening_Example_VB.htm)
[Exclude Faces Before Flattening (VB.NET)](Exclude_Faces_Before_Flattening_Example_VBNET.htm)
[Exclude Faces Before Flattening (C#)](Exclude_Faces_Before_Flattening_Example_CSharp.htm)

## Remarks

To get the size of the array returned by this method, call [IFlatPatternFeatureData::IGetExcludedFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFacesCount.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::IGetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFaces.html)
[IFlatPatternFeatureData::ISetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ISetExcludedFaces.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20
