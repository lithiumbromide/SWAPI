---
title: "MultipleContactSetsEditManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "MultipleContactSetsEditManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MultipleContactSetsEditManager.html"
---

# MultipleContactSetsEditManager Property (ICWStudy)

Gets the Multiple Contact Sets Edit Manager which provides the simultaneous editing of multiple contact sets.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MultipleContactSetsEditManager As CWMultipleContactSetsEditManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWMultipleContactSetsEditManager

value = instance.MultipleContactSetsEditManager
```

### C#

```csharp
CWMultipleContactSetsEditManager MultipleContactSetsEditManager {get;}
```

### C++/CLI

```cpp
property CWMultipleContactSetsEditManager^ MultipleContactSetsEditManager {
   CWMultipleContactSetsEditManager^ get();
}
```

### Property Value

[ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)

## VBA Syntax

See [CWStudy::MultipleContactSetsEditManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~MultipleContactSetsEditManager.html).

## Examples

See the [ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html) examples.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::ContactManager Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ContactManager.html)
[ICWStudy::MultipleComponentContactsEditManager Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MultipleComponentContactsEditManager.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
