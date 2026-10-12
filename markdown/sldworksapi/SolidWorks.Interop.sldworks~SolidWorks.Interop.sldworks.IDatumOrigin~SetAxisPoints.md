---
title: "SetAxisPoints Method (IDatumOrigin)"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin"
member: "SetAxisPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~SetAxisPoints.html"
---

# SetAxisPoints Method (IDatumOrigin)

Sets the points that define the geometry of this datum origin.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAxisPoints( _
   ByVal PointData As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumOrigin
Dim PointData As System.Object
Dim value As System.Boolean

value = instance.SetAxisPoints(PointData)
```

### C#

```csharp
System.bool SetAxisPoints(
   System.object PointData
)
```

### C++/CLI

```cpp
System.bool SetAxisPoints(
   System.Object^ PointData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointData`: Array of 4 doubles (see [Remarks](#Remarks))

## VBA Syntax

See [DatumOrigin::SetAxisPoints](ms-its:sldworksapivb6.chm::/sldworks~DatumOrigin~SetAxisPoints.html).

## Remarks

This method gives you control over the shape of the symbol.

The array of 4 doubles is 2 (X,Y) coordinates in drawing space:

- The first coordinate (array items 0 and 1) is the tip of the arrowhead on the X leader portion of the symbol.
- The second coordinate (array items 2 and 3) is the tip of the arrowhead on the Y leader portion of the symbol.

The interactive user has this control via the selection drag handles of the symbol.

This method returns a BOOLEAN indicating success or failure of the operation. The operation can fail if either of the coordinates is so close to the symbol origin that the symbol cannot be drawn properly. There must be:

- Room to draw the arrow at the end of the origin leaders
- A gap between the symbol origin and the beginning of the first leader.

You can get:

- Coordinates of the symbol origin using [IAnnotation::GetPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetPosition.html).
- Arrowhead length using [IModelDocExtension::GetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html) - swDetailingArrowWidth
- Gap using IModelDocExtension::GetUserPreferenceDouble - swDetailingWitnessLineGap

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html)
[IDatumOrigin::ISetAxisPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~ISetAxisPoints.html)
[IDatumOrigin::IGetAxisPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~IGetAxisPoints2.html)
[IDatumOrigin::GetAxisPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetAxisPoints2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
