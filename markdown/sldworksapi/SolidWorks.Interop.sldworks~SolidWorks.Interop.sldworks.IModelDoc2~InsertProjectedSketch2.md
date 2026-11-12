---
title: "InsertProjectedSketch2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertProjectedSketch2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertProjectedSketch2.html"
---

# InsertProjectedSketch2 Method (IModelDoc2)

Obsolete. See [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html) and [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertProjectedSketch2( _
   ByVal Reverse As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Reverse As System.Integer
Dim value As System.Object

value = instance.InsertProjectedSketch2(Reverse)
```

### C#

```csharp
System.object InsertProjectedSketch2(
   System.int Reverse
)
```

### C++/CLI

```cpp
System.Object^ InsertProjectedSketch2(
   System.int Reverse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reverse`: 1 to reverse the projected direction, 0 to not reverse the projected direction

### Return Value

Newly created [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) or Nothing or null if the operation fails

## VBA Syntax

See [ModelDoc2::InsertProjectedSketch2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertProjectedSketch2.html).

## Examples

[Get Projected Curve Feature Data (C#)](Get_Projected_Curve_Feature_Data_Example_CSharp.htm)
[Get Projected Curve Feature Data (VB.NET)](Get_Projected_Curve_Feature_Data_Example_VBNET.htm)
[Get Projected Curve Feature Data (VBA)](Get_Projected_Curve_Feature_Data_Example_VB.htm)

## Remarks

You can reverse the direction in which the curve is projected. This is necessary only when the selected face wraps around the plane of the curve. For example, if the sketch being projected is surrounded by a cylindrical face, then two possible projections exist. The reverse argument switches the direction based on the normal vector of the sketch. The default direction is along the sketch normal.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IInsertProjectedSketch2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertProjectedSketch2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
