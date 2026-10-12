---
title: "GetPrincipalMomentOfInertia Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "GetPrincipalMomentOfInertia"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalMomentOfInertia.html"
---

# GetPrincipalMomentOfInertia Method (ICWMassPropertiesManager)

Gets the moments of inertia with respect to the principal axes and the center of mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrincipalMomentOfInertia() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Object

value = instance.GetPrincipalMomentOfInertia()
```

### C#

```csharp
System.object GetPrincipalMomentOfInertia()
```

### C++/CLI

```cpp
System.Object^ GetPrincipalMomentOfInertia();
```

### Return Value

Array of three principal moments of inertia (see **Remarks**)

## VBA Syntax

See [CWMassPropertiesManager::GetPrincipalMomentOfInertia](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~GetPrincipalMomentOfInertia.html).

## Examples

See the [ICWMassPropertiesManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html) examples.

## Remarks

The moment of inertia is calculated with respect to the output coordinate system. Before calling this method, call [ICWMassPropertiesManager::SetCoordinateSystemName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~SetCoordinateSystemName.html) or [ICWMassPropertiesManager::SetCoordinateSystemToDefault](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~SetCoordinateSystemToDefault.html).

The moments of inertia are in units of kilograms * meters squared.

This method returns three doubles as follows:

[ `Px`, `Py`, `Pz` ]

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::GetMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertia.html)
[ICWMassPropertiesManager::GetMomentOfInertiaAtOutputCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertiaAtOutputCoordinateSystem.html)
[ICWMassPropertiesManager::GetPrincipalAxesOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalAxesOfInertia.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
