---
title: "BaseExcitationEndEdit Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "BaseExcitationEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~BaseExcitationEndEdit.html"
---

# BaseExcitationEndEdit Method (ICWBaseExcitation)

Ends editing base excitation.

## Syntax

### Visual Basic (Declaration)

```vb
Function BaseExcitationEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim value As System.Integer

value = instance.BaseExcitationEndEdit()
```

### C#

```csharp
System.int BaseExcitationEndEdit()
```

### C++/CLI

```cpp
System.int BaseExcitationEndEdit();
```

### Return Value

Error as defined in [swsBaseExcitationEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBaseExcitationEndEditError_e.html)

## VBA Syntax

See [CWBaseExcitation::BaseExcitationEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~BaseExcitationEndEdit.html).

## Remarks

You must call [ICWBaseExcitation::BaseExcitationBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~BaseExcitationBeginEdit.html) to start editing a base excitation. To end editing a base excitation, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
