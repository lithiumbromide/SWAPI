---
title: "GetPrincipalAxesOfInertia Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "GetPrincipalAxesOfInertia"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalAxesOfInertia.html"
---

# GetPrincipalAxesOfInertia Method (ICWMassPropertiesManager)

Gets the principal axes of inertia with respect to the center of mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrincipalAxesOfInertia() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Object

value = instance.GetPrincipalAxesOfInertia()
```

### C#

```csharp
System.object GetPrincipalAxesOfInertia()
```

### C++/CLI

```cpp
System.Object^ GetPrincipalAxesOfInertia();
```

### Return Value

2D array of vector coefficients of the three principal axes of inertia (see **Remarks**)

## VBA Syntax

See [CWMassPropertiesManager::GetPrincipalAxesOfInertia](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~GetPrincipalAxesOfInertia.html).

## Examples

See the [ICWMassPropertiesManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html) examples.

## Remarks

A principal axis is one of three mutually perpendicular axes in a body about which the moment of inertia is at a maximum.

This method returns nine doubles as follows:

[ `axis1_lx`, `axis1_ly`, `axis1_lz`, `axis2_lx`, `axis2_ly`, `axis2_lz`, `axis3_lx`, `axis3_ly`, `axis3_lz` ]

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::GetMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertia.html)
[ICWMassPropertiesManager::GetMomentOfInertiaAtOutputCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertiaAtOutputCoordinateSystem.html)
[ICWMassPropertiesManager::GetPrincipalMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalMomentOfInertia.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
