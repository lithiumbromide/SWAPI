---
title: "MultipleContactSetsEndEdit Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "MultipleContactSetsEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~MultipleContactSetsEndEdit.html"
---

# MultipleContactSetsEndEdit Method (ICWMultipleContactSetsEditManager)

Finishes editing multiple contact sets.

## Syntax

### Visual Basic (Declaration)

```vb
Function MultipleContactSetsEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim value As System.Integer

value = instance.MultipleContactSetsEndEdit()
```

### C#

```csharp
System.int MultipleContactSetsEndEdit()
```

### C++/CLI

```cpp
System.int MultipleContactSetsEndEdit();
```

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::MultipleContactSetsEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~MultipleContactSetsEndEdit.html).

## Examples

See the [ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html) examples.

## Remarks

To start editing a contact set, call [ICWMultipleContactSetsEditManager::MultipleContactSetsBeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~MultipleContactSetsBeginEdit.html). You must call this method to end editing that contact set. Changes are not applied unless you call both methods.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
