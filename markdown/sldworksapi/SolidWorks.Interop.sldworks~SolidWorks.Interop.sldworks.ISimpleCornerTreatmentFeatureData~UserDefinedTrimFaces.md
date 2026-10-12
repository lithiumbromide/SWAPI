---
title: "UserDefinedTrimFaces Property (ISimpleCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleCornerTreatmentFeatureData"
member: "UserDefinedTrimFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~UserDefinedTrimFaces.html"
---

# UserDefinedTrimFaces Property (ISimpleCornerTreatmentFeatureData)

Gets and sets the user-defined trim faces for this simple corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserDefinedTrimFaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleCornerTreatmentFeatureData
Dim value As System.Object

instance.UserDefinedTrimFaces = value

value = instance.UserDefinedTrimFaces
```

### C#

```csharp
System.object UserDefinedTrimFaces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ UserDefinedTrimFaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SimpleCornerTreatmentFeatureData::UserDefinedTrimFaces](ms-its:sldworksapivb6.chm::/sldworks~SimpleCornerTreatmentFeatureData~UserDefinedTrimFaces.html).

## Remarks

This property is valid only if [ISimpleCornerTreatmentFeatureData::PlanarTrimToolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~PlanarTrimToolType.html) is set to [swCornerTreatmentPlanarTriimToolType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html).CornerTreatmentPlanarTrimTool_UserDefined.

## See Also

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.html)
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
