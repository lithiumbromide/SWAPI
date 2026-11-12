---
title: "GetMomentOfInertiaAtOutputCoordinateSystem Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "GetMomentOfInertiaAtOutputCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertiaAtOutputCoordinateSystem.html"
---

# GetMomentOfInertiaAtOutputCoordinateSystem Method (ICWMassPropertiesManager)

Gets the moments of inertia with respect to the output coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMomentOfInertiaAtOutputCoordinateSystem() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Object

value = instance.GetMomentOfInertiaAtOutputCoordinateSystem()
```

### C#

```csharp
System.object GetMomentOfInertiaAtOutputCoordinateSystem()
```

### C++/CLI

```cpp
System.Object^ GetMomentOfInertiaAtOutputCoordinateSystem();
```

### Return Value

Array of nine moment of inertia components (see **Remarks**)

## VBA Syntax

See [CWMassPropertiesManager::GetMomentOfInertiaAtOutputCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~GetMomentOfInertiaAtOutputCoordinateSystem.html).

## Examples

See the [ICWMassPropertiesManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html) examples.

## Remarks

The moment of inertia is calculated with respect to the output coordinate system. Before calling this method, call [ICWMassPropertiesManager::SetCoordinateSystemName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~SetCoordinateSystemName.html) or [ICWMassPropertiesManager::SetCoordinateSystemToDefault](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~SetCoordinateSystemToDefault.html).

The moment of inertia components are in units of kilograms * meters squared.

This method returns nine doubles as follows:

[ `lxx`, `lxy`, `lxz`, l`yx`, `lyy`, `lyz`, `lzx`, `lzy`, `lzz` ]

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::GetMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertia.html)
[ICWMassPropertiesManager::GetPrincipalAxesOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalAxesOfInertia.html)
[ICWMassPropertiesManager::GetPrincipalMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalMomentOfInertia.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
