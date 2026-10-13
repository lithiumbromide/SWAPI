---
title: "MultipleComponentContactsEndEdit Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "MultipleComponentContactsEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~MultipleComponentContactsEndEdit.html"
---

# MultipleComponentContactsEndEdit Method (ICWMultipleComponentContactsEditManager)

Finishes editing multiple contact components.

## Syntax

### Visual Basic (Declaration)

```vb
Function MultipleComponentContactsEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim value As System.Integer

value = instance.MultipleComponentContactsEndEdit()
```

### C#

```csharp
System.int MultipleComponentContactsEndEdit()
```

### C++/CLI

```cpp
System.int MultipleComponentContactsEndEdit();
```

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::MultipleComponentContactsEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~MultipleComponentContactsEndEdit.html).

## Examples

See the [ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html) examples.

## Remarks

To start editing multiple contact components, call [ICWMultipleComponentContactsEditManager::MultipleComponentContactsBeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~MultipleComponentContactsBeginEdit.html). You must call this method to finish editing multiple contact components. Changes are not applied unless you call both methods.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
