---
title: "AddBodies Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "AddBodies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddBodies.html"
---

# AddBodies Method (ICWMassPropertiesManager)

Adds the specified bodies to the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddBodies( _
   ByVal DispArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim DispArray As System.Object
Dim value As System.Integer

value = instance.AddBodies(DispArray)
```

### C#

```csharp
System.int AddBodies(
   System.object DispArray
)
```

### C++/CLI

```cpp
System.int AddBodies(
   System.Object^ DispArray
)
```

### Parameters

- `DispArray`: Array of bodies

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::AddBodies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~AddBodies.html).

## Examples

See the [ICWMassPropertiesManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html) examples.

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::AddBoltConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddBoltConnectors.html)
[ICWMassPropertiesManager::AddDistributedMasses Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddDistributedMasses.html)
[ICWMassPropertiesManager::AddPinConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddPinConnectors.html)
[ICWMassPropertiesManager::AddRemoteLoadMasses Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddRemoteLoadMasses.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
