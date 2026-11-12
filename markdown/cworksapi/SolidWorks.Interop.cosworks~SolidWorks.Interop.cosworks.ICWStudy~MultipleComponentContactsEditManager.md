---
title: "MultipleComponentContactsEditManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "MultipleComponentContactsEditManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MultipleComponentContactsEditManager.html"
---

# MultipleComponentContactsEditManager Property (ICWStudy)

Gets the Multiple Component Contacts Edit Manager which provides the simultaneous editing of multiple component contacts.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MultipleComponentContactsEditManager As CWMultipleComponentContactsEditManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWMultipleComponentContactsEditManager

value = instance.MultipleComponentContactsEditManager
```

### C#

```csharp
CWMultipleComponentContactsEditManager MultipleComponentContactsEditManager {get;}
```

### C++/CLI

```cpp
property CWMultipleComponentContactsEditManager^ MultipleComponentContactsEditManager {
   CWMultipleComponentContactsEditManager^ get();
}
```

### Property Value

[ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)

## VBA Syntax

See [CWStudy::MultipleComponentContactsEditManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~MultipleComponentContactsEditManager.html).

## Examples

See the [ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html) examples.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::ContactManager Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ContactManager.html)
[ICWStudy::MultipleContactSetsEditManager Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MultipleContactSetsEditManager.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
