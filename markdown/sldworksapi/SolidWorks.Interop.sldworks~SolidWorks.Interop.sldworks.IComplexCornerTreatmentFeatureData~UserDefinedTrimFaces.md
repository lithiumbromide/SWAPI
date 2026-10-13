---
title: "UserDefinedTrimFaces Property (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "UserDefinedTrimFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~UserDefinedTrimFaces.html"
---

# UserDefinedTrimFaces Property (IComplexCornerTreatmentFeatureData)

Gets and sets the user-defined trim faces for this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserDefinedTrimFaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
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

See [ComplexCornerTreatmentFeatureData::UserDefinedTrimFaces](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~UserDefinedTrimFaces.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This property is valid only if [IComplexCornerTreatmentFeatureData::PlanarTrimToolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~PlanarTrimToolType.html) is set to [swCornerTreatmentPlanarTrimToolType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html).CornerTreatmentPlanarTrimTool_UserDefined.

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
