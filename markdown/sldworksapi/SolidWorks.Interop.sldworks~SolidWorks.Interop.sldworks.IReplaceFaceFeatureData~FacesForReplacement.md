---
title: "FacesForReplacement Property (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "FacesForReplacement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~FacesForReplacement.html"
---

# FacesForReplacement Property (IReplaceFaceFeatureData)

Gets or sets the faces to replace for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FacesForReplacement As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IReplaceFaceFeatureData
Dim value As System.Object

instance.FacesForReplacement = value

value = instance.FacesForReplacement
```

### C#

```csharp
System.object FacesForReplacement {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FacesForReplacement {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to replace

## VBA Syntax

See [ReplaceFaceFeatureData::FacesForReplacement](ms-its:sldworksapivb6.chm::/sldworks~ReplaceFaceFeatureData~FacesForReplacement.html).

## Examples

See the [IReplaceFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFaceFeatureData::GetFacesForReplacementCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetFacesForReplacementCount.html)
[IReplaceFaceFeatureData::IGetFacesForReplacement Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetFacesForReplacement.html)
[IReplaceFaceFeatureData::ISetFacesForReplacement Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetFacesForReplacement.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
