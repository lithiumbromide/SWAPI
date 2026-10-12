---
title: "InsertCoordinateSystem Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCoordinateSystem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.html"
---

# InsertCoordinateSystem Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertCoordinateSystem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCoordinateSystem.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCoordinateSystem( _
   ByVal XFlippedIn As System.Boolean, _
   ByVal YFlippedIn As System.Boolean, _
   ByVal ZFlippedIn As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim XFlippedIn As System.Boolean
Dim YFlippedIn As System.Boolean
Dim ZFlippedIn As System.Boolean
Dim value As System.Boolean

value = instance.InsertCoordinateSystem(XFlippedIn, YFlippedIn, ZFlippedIn)
```

### C#

```csharp
System.bool InsertCoordinateSystem(
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

### C++/CLI

```cpp
System.bool InsertCoordinateSystem(
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XFlippedIn`: True to flip the x direction, false to not
- `YFlippedIn`: True to flip the y direction, false to not
- `ZFlippedIn`: True to flip the z direction, false to not

### Return Value

True if coordinate system is added successfully, false if not

## VBA Syntax

See [ModelDoc2::InsertCoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCoordinateSystem.html).

## Examples

[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)

## Remarks

Make the selections using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a mark of:

- 1 - Origin
- 2 - X axis
- 4 - Y axis
- 8 - Z axis

This method:

- does not require all three axis to be selected. The behavior is the same as interactively creating a coordinate system. See the SOLIDWORKS Help for more information.
- works in section-view mode, but not if temporary geometry that only exists in section-view mode is selected.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetCurrentCoordinateSystemName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCurrentCoordinateSystemName.html)
[IModelDocExtension::GetCoordinateSystemTransformByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
