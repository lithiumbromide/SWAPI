---
title: "GetMomentOfInertia Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "GetMomentOfInertia"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertia.html"
---

# GetMomentOfInertia Method (ICWMassPropertiesManager)

Gets the moments of inertia with respect to the center of mass and the output coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMomentOfInertia() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Object

value = instance.GetMomentOfInertia()
```

### C#

```csharp
System.object GetMomentOfInertia()
```

### C++/CLI

```cpp
System.Object^ GetMomentOfInertia();
```

### Return Value

Array of nine moment of inertia components

## VBA Syntax

See [CWMassPropertiesManager::GetMomentOfInertia](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~GetMomentOfInertia.html).

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
[ICWMassPropertiesManager::GetMomentOfInertiaAtOutputCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertiaAtOutputCoordinateSystem.html)
[ICWMassPropertiesManager::GetPrincipalAxesOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalAxesOfInertia.html)
[ICWMassPropertiesManager::GetPrincipalMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalMomentOfInertia.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
