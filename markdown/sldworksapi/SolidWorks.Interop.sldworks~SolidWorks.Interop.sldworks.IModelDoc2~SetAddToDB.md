---
title: "SetAddToDB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetAddToDB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.html"
---

# SetAddToDB Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAddToDB( _
   ByVal Setting As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Setting As System.Boolean

instance.SetAddToDB(Setting)
```

### C#

```csharp
void SetAddToDB(
   System.bool Setting
)
```

### C++/CLI

```cpp
void SetAddToDB(
   System.bool Setting
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Setting`: True to add items directly to the SOLIDWORKS database, false if not

## VBA Syntax

See [ModelDoc2::SetAddToDB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetAddToDB.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)
[Calculate Closest Distance Between Model Components (VBA)](Calculate_Closest_Distance_Between_Model_Components_Example_VB.htm)
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)
[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)

## Remarks

One of the benefits of adding sketch entities directly to the database is that you can avoid grid and entity snapping. For example, if you create a sketch line whose endpoint is near another entity or near a grid point, the new line endpoint snaps to the other item or grid point. Setting ModelDoc2::SetAddToDB to True avoids this behavior during sketch entity creation.

IModelDoc2::SetAddToDb and [IModelDoc2::SetDisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html) also increase performance during sketch entity creation. IModelDoc2::SetDisplayWhenAdded requires that IModelDoc2::SetAddToDB is True.

If you want to constrain all the sketch entities after creation, use [ISketch::ConstrainAll](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ConstrainAll.html).

After setting IModelDoc2::SetAddToDB to True, you must set it back to false to restore SOLIDWORKS to its normal operating mode.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetAddToDB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAddToDB.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
