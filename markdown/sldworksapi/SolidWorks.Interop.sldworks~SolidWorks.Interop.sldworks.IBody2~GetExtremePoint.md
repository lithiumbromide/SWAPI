---
title: "GetExtremePoint Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetExtremePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetExtremePoint.html"
---

# GetExtremePoint Method (IBody2)

Calculates the extreme point of the model in the specified direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtremePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByRef Outx As System.Double, _
   ByRef Outy As System.Double, _
   ByRef Outz As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Outx As System.Double
Dim Outy As System.Double
Dim Outz As System.Double
Dim value As System.Boolean

value = instance.GetExtremePoint(X, Y, Z, Outx, Outy, Outz)
```

### C#

```csharp
System.bool GetExtremePoint(
   System.double X,
   System.double Y,
   System.double Z,
   out System.double Outx,
   out System.double Outy,
   out System.double Outz
)
```

### C++/CLI

```cpp
System.bool GetExtremePoint(
   System.double X,
   System.double Y,
   System.double Z,
   [Out] System.double Outx,
   [Out] System.double Outy,
   [Out] System.double Outz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X component of the direction vector
- `Y`: Y component of the direction vector
- `Z`: Z component of the direction vector
- `Outx`: Extreme point X coordinate
- `Outy`: Extreme point Y coordinate
- `Outz`: Extreme point Z coordinate

### Return Value

True if a point was found, false if not

## VBA Syntax

See [Body2::GetExtremePoint](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetExtremePoint.html).

## Remarks

This method returns the furthest possible point of intersection between a plane normal to the direction vector specified and the model as the plane moves along the direction vector. For example, if the model is a right cube centered on the origin and the direction vector is (1.0, 1.0, 1.0), then the extreme point is the vertex at (1.0,
1.0, 1.0).

If there is more than one point (for example, if there is a face perpendicular to the direction vector), SOLIDWORKS returns a unique point that it finds in a deterministic way.

**COM example**

HRESULT auBody_c::XDispatch2::GetExtremePoint( double x, double y, double z, double*
outx, double* outy, double* outz, VARIANT_BOOL* found ) {

METHOD_PROLOGUE_EX_(auBody_c, Dispatch2)

AU_INTERFACE_VERIFY_NOT_DISCONNECTED

BOOL gotIt = pThis->GetExtremePoint(x, y, z, outx, outy, outz);
*found = gotIt ? VARIANT_True : VARIANT_false;
return gotIt ? S_OK : S_false;

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
