---
title: "RemoveBodies Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveBodies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveBodies.html"
---

# RemoveBodies Method (ICWMassPropertiesManager)

Removes the specified bodies from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveBodies( _
   ByVal DispArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim DispArray As System.Object
Dim value As System.Integer

value = instance.RemoveBodies(DispArray)
```

### C#

```csharp
System.int RemoveBodies(
   System.object DispArray
)
```

### C++/CLI

```cpp
System.int RemoveBodies(
   System.Object^ DispArray
)
```

### Parameters

- `DispArray`: Array of bodies to remove

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveBodies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveBodies.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveAllBodies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllBodies.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
