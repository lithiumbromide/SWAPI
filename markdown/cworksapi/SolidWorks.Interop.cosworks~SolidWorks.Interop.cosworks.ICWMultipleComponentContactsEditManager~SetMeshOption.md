---
title: "SetMeshOption Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetMeshOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetMeshOption.html"
---

# SetMeshOption Method (ICWMultipleComponentContactsEditManager)

Sets the mesh compatibility option.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMeshOption( _
   ByVal NMeshOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim NMeshOption As System.Integer
Dim value As System.Integer

value = instance.SetMeshOption(NMeshOption)
```

### C#

```csharp
System.int SetMeshOption(
   System.int NMeshOption
)
```

### C++/CLI

```cpp
System.int SetMeshOption(
   System.int NMeshOption
)
```

### Parameters

- `NMeshOption`: Mesh compatibility option as defined in [swsMeshCompatibility_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshCompatibility_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::SetMeshOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetMeshOption.html).

## Remarks

This method is valid only if [ICWMultipleComponentContactsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetContactType.html)'s NType is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeBonded.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
