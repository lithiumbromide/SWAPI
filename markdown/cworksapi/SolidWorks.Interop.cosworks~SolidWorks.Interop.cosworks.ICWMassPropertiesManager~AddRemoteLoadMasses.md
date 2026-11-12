---
title: "AddRemoteLoadMasses Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "AddRemoteLoadMasses"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddRemoteLoadMasses.html"
---

# AddRemoteLoadMasses Method (ICWMassPropertiesManager)

Adds the specified remote load masses to the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRemoteLoadMasses( _
   ByVal NameArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NameArray As System.Object
Dim value As System.Integer

value = instance.AddRemoteLoadMasses(NameArray)
```

### C#

```csharp
System.int AddRemoteLoadMasses(
   System.object NameArray
)
```

### C++/CLI

```cpp
System.int AddRemoteLoadMasses(
   System.Object^ NameArray
)
```

### Parameters

- `NameArray`: Array of names of remote load masses

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::AddRemoteLoadMasses](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~AddRemoteLoadMasses.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
