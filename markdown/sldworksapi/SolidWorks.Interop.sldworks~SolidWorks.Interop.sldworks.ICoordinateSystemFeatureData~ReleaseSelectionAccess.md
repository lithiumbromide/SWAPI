---
title: "ReleaseSelectionAccess Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICoordinateSystemFeatureData)

Releases access to selections that describe this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData

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

See [CoordinateSystemFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~ReleaseSelectionAccess.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)
[Insert Coordinate System Feature at Center of Mass (VBA)](Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm)
[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)

## Remarks

[ICoordinateSystemFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~AccessSelections.html) and [ICoordinateSystemFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~IAccessSelections.html) puts the model into a rollback state to allow access to the selections that define the coordinate system feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
