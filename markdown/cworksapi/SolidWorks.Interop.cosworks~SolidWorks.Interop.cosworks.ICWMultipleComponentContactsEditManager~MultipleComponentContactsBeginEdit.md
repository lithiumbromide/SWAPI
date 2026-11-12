---
title: "MultipleComponentContactsBeginEdit Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "MultipleComponentContactsBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~MultipleComponentContactsBeginEdit.html"
---

# MultipleComponentContactsBeginEdit Method (ICWMultipleComponentContactsEditManager)

Starts editing multiple contact components.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MultipleComponentContactsBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager

instance.MultipleComponentContactsBeginEdit()
```

### C#

```csharp
void MultipleComponentContactsBeginEdit()
```

### C++/CLI

```cpp
void MultipleComponentContactsBeginEdit();
```

## VBA Syntax

See [CWMultipleComponentContactsEditManager::MultipleComponentContactsBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~MultipleComponentContactsBeginEdit.html).

## Examples

See the [ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html) examples.

## Remarks

To start editing multiple contact components, call this method. You must call [ICWMultipleComponentContactsEditManager::MultipleComponentContactsEndEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~MultipleComponentContactsEndEdit.html) to finish editing multiple contact components. Changes are not applied unless you call both methods.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
