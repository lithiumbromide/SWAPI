---
title: "GetCSYSEulersAngularRotation Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCSYSEulersAngularRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSEulersAngularRotation.html"
---

# GetCSYSEulersAngularRotation Method (IModelDocExtension)

Gets the specified Eulers angular rotation values that transform one selected coordinate system into another.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCSYSEulersAngularRotation( _
   ByRef phiAngle As System.Double, _
   ByRef thetaAngle As System.Double, _
   ByRef psiAngle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim phiAngle As System.Double
Dim thetaAngle As System.Double
Dim psiAngle As System.Double
Dim value As System.Boolean

value = instance.GetCSYSEulersAngularRotation(phiAngle, thetaAngle, psiAngle)
```

### C#

```csharp
System.bool GetCSYSEulersAngularRotation(
   out System.double phiAngle,
   out System.double thetaAngle,
   out System.double psiAngle
)
```

### C++/CLI

```cpp
System.bool GetCSYSEulersAngularRotation(
   [Out] System.double phiAngle,
   [Out] System.double thetaAngle,
   [Out] System.double psiAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `phiAngle`: Roll or rotation about the longitudinal axis (see **Remarks**)
- `thetaAngle`: Pitch or rotation about the lateral axis (see **Remarks**)
- `psiAngle`: Yaw or rotation about the vertical axis (see **Remarks**)

### Return Value

True if rotation values successfully retrieved, false if not

## VBA Syntax

See [ModelDocExtension::GetCSYSEulersAngularRotation](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetCSYSEulersAngularRotation.html).

## Remarks

phiAngle is the roll or rotation about the longitudinal axis. Rolling corresponds to moving one side of an object upward while moving the other side downward (no pitch or yaw).

thetaAngle is the pitch or rotation around the lateral axis. Pitching corresponds to tilting the front of an object up or down (no yaw or roll).

psiAngle is the yaw or rotation about the vertical axis. Yawing corresponds to turning the front of an object left or right (no pitch or roll).

This method corresponds to the SOLIDWORKS measure tool's calculation of angular rotation between two coordinate systems. See **SOLIDWORKS online help > Fundamentals > Measure Tool** for more information.

Use Wikipedia to learn more about Euler's angles.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetCSYSDistances Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSDistances.html)
[IModelDocExtension::GetCSYSXYZAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSXYZAngularRotation.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
