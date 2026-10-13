---
title: "GetArcEndCondition Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetArcEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetArcEndCondition.html"
---

# GetArcEndCondition Method (IDimension)

Gets the end conditions for linear dimensions that end on an arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcEndCondition( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetArcEndCondition(Index)
```

### C#

```csharp
System.int GetArcEndCondition(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetArcEndCondition(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the endpoint to get the end condition from; 1 is the first endpoint, 2 is the second endpoint

### Return Value

End condition as defined in [swArcEndCondition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArcEndCondition_e.html)

## VBA Syntax

See [Dimension::GetArcEndCondition](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetArcEndCondition.html).

## Remarks

In a linear dimension, the distance measured is from one point to another. If one or both of those points are on an arc, you can change the point to be the center of the arc, the nearest point on the arc, or the furthest point on the arc. The arc end condition describes which point is used.

Use [IDimension::SetArcEndCondition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~SetArcEndCondition.html) to set the arc end conditions.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::SetArcEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetArcEndCondition.html)

## Availability

SOLIDWORKS 99, datecode 1999207
