---
title: "BaseExcitationBeginEdit Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "BaseExcitationBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~BaseExcitationBeginEdit.html"
---

# BaseExcitationBeginEdit Method (ICWBaseExcitation)

Starts editing base excitation.

## Syntax

### Visual Basic (Declaration)

```vb
Sub BaseExcitationBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation

instance.BaseExcitationBeginEdit()
```

### C#

```csharp
void BaseExcitationBeginEdit()
```

### C++/CLI

```cpp
void BaseExcitationBeginEdit();
```

## VBA Syntax

See [CWBaseExcitation::BaseExcitationBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~BaseExcitationBeginEdit.html).

## Remarks

To start editing a base excitation, you must call this method. You must call [ICWBaseExcitation::BaseExcitationEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~BaseExcitationEndEdit.html) to end editing a base excitation. Changes are not applied unless you call both methods.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
