---
title: "SetAsDefaultContactSet Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetAsDefaultContactSet"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetAsDefaultContactSet.html"
---

# SetAsDefaultContactSet Method (ICWMultipleContactSetsEditManager)

Sets the specified contact set as the default contact set in the set of contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAsDefaultContactSet( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim SName As System.String
Dim value As System.Integer

value = instance.SetAsDefaultContactSet(SName)
```

### C#

```csharp
System.int SetAsDefaultContactSet(
   System.string SName
)
```

### C++/CLI

```cpp
System.int SetAsDefaultContactSet(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of contact set to make the default contact set

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetAsDefaultContactSet](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetAsDefaultContactSet.html).

## Examples

See the [ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html) examples.

## Remarks

The default contact set is one of the contact sets in the selection list on the Multiple Contact Sets PropertyManager page. Its properties apply to all of the contact sets in the selection list.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
