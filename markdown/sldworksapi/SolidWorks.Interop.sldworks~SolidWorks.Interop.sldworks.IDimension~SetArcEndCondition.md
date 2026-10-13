---
title: "SetArcEndCondition Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetArcEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetArcEndCondition.html"
---

# SetArcEndCondition Method (IDimension)

Sets the end conditions for linear dimensions that end on an arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetArcEndCondition( _
   ByVal Index As System.Integer, _
   ByVal Condition As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Index As System.Integer
Dim Condition As System.Integer
Dim value As System.Integer

value = instance.SetArcEndCondition(Index, Condition)
```

### C#

```csharp
System.int SetArcEndCondition(
   System.int Index,
   System.int Condition
)
```

### C++/CLI

```cpp
System.int SetArcEndCondition(
   System.int Index,
   System.int Condition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the endpoint on which to set the end condition; 1 is the first endpoint, 2 is the second endpoint
- `Condition`: End condition as defined in [swArcEndCondition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArcEndCondition_e.html) ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArcEndCondition_e.html

### Return Value

Indicates the success or failure of this method:

| 0 | Command was successful; the arc end condition was set |
| --- | --- |
| -1 | Command failed for an unknown reason; the arc end condition was not set |
| -2 | Index parameter is invalid |
| -3 | Condition parameter is invalid |
| -4 | Endpoint 1 is not related to an arc |
| -5 | Endpoint 2 is not related to an arc |

## VBA Syntax

See [Dimension::SetArcEndCondition](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetArcEndCondition.html).

## Remarks

Linear dimensions measure the distance from one point to another. If one or both of those points is on an arc, the point can be changed to the center point of the arc, the nearest point on the arc, or the furthest point on the arc. The arc end condition describes which point to use.

Use [IDimension::GetArcEndCondition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetArcEndCondition.html) to get the arc end conditions.

To see the effects of changing the arc endpoint conditions, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::GetArcEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetArcEndCondition.html)

## Availability

SOLIDWORKS 99, datecode 1999207
