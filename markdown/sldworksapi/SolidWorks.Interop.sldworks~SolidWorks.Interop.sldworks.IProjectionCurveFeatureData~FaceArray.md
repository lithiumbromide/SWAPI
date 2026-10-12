---
title: "FaceArray Property (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "FaceArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.html"
---

# FaceArray Property (IProjectionCurveFeatureData)

Gets or sets the target faces for this projected curve.

## Syntax

### Visual Basic (Declaration)

```vb
Property FaceArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
Dim value As System.Object

instance.FaceArray = value

value = instance.FaceArray
```

### C#

```csharp
System.object FaceArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FaceArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of faces that describe the projected curve

## VBA Syntax

See [ProjectionCurveFeatureData::FaceArray](ms-its:sldworksapivb6.chm::/sldworks~ProjectionCurveFeatureData~FaceArray.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)
[IProjectionCurveFeatureData::GetFaceArrayCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~GetFaceArrayCount.html)
[IProjectionCurveFeatureData::IGetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~IGetFaceArray.html)
[IProjectionCurveFeatureData::ISetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ISetFaceArray.html)
[IProjectionCurveFeatureData::Reverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Reverse.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
