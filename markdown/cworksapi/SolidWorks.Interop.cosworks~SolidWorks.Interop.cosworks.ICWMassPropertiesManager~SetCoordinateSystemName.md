---
title: "SetCoordinateSystemName Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "SetCoordinateSystemName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~SetCoordinateSystemName.html"
---

# SetCoordinateSystemName Method (ICWMassPropertiesManager)

Applies the specified coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCoordinateSystemName( _
   ByVal SCoordinateSystemName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim SCoordinateSystemName As System.String

instance.SetCoordinateSystemName(SCoordinateSystemName)
```

### C#

```csharp
void SetCoordinateSystemName(
   System.string SCoordinateSystemName
)
```

### C++/CLI

```cpp
void SetCoordinateSystemName(
   System.String^ SCoordinateSystemName
)
```

### Parameters

- `SCoordinateSystemName`: Name of coordinate system

## VBA Syntax

See [CWMassPropertiesManager::SetCoordinateSystemName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~SetCoordinateSystemName.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::SetCoordinateSystemToDefault Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~SetCoordinateSystemToDefault.html)
[ICWMassPropertiesManager::GetMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertia.html)
[ICWMassPropertiesManager::GetMomentOfInertiaAtOutputCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetMomentOfInertiaAtOutputCoordinateSystem.html)
[ICWMassPropertiesManager::GetPrincipalMomentOfInertia Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~GetPrincipalMomentOfInertia.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
