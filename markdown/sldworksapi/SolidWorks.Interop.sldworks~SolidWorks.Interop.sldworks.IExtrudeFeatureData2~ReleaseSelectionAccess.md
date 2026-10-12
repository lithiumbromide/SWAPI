---
title: "ReleaseSelectionAccess Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IExtrudeFeatureData2)

Releases access to the selections used to define the extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2

instance.ReleaseSelectionAccess()
```

### C#

```csharp
void ReleaseSelectionAccess()
```

### C++/CLI

```cpp
void ReleaseSelectionAccess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ExtrudeFeatureData2::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~ReleaseSelectionAccess.html).

## Examples

[Create Extruded Thin Feature (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)
[Determine if Sketch Contour or Sketch Region (VBA)](Determine_if_Sketch_Contour_or_Sketch_Region_Example_VB.htm)
[Create Extrude Feature Using Sketch Contours (C#)](Create_Extrude_Feature_Using_Sketch_Contours_Example_CSharp.htm)
[Create Extrude Feature Using Sketch Contours (VB.NET)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm)
[Create Extrude Feature Using Sketch Contours (VBA)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm)

## Remarks

[IExtrudeFeatureData2::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~AccessSelections.html) or [IExtrudeFeatureData2::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~IAccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature. Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
