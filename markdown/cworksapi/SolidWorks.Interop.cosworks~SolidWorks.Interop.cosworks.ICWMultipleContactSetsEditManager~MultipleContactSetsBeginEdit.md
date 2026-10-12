---
title: "MultipleContactSetsBeginEdit Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "MultipleContactSetsBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~MultipleContactSetsBeginEdit.html"
---

# MultipleContactSetsBeginEdit Method (ICWMultipleContactSetsEditManager)

Starts editing multiple contact sets.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MultipleContactSetsBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager

instance.MultipleContactSetsBeginEdit()
```

### C#

```csharp
void MultipleContactSetsBeginEdit()
```

### C++/CLI

```cpp
void MultipleContactSetsBeginEdit();
```

## VBA Syntax

See [CWMultipleContactSetsEditManager::MultipleContactSetsBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~MultipleContactSetsBeginEdit.html).

## Examples

See the [ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html) examples.

## Remarks

To start editing a contact set, call this method. You must call [ICWMultipleContactSetsEditManager::MultipleContactSetsEndEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~MultipleContactSetsEndEdit.html) to end editing that contact set. Changes are not applied unless you call both methods.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
