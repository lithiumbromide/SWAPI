---
title: "RestraintEndEdit Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "RestraintEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintEndEdit.html"
---

# RestraintEndEdit Method (ICWRestraint)

Ends editing a restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function RestraintEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim value As System.Integer

value = instance.RestraintEndEdit()
```

### C#

```csharp
System.int RestraintEndEdit()
```

### C++/CLI

```cpp
System.int RestraintEndEdit();
```

### Return Value

Error code as defined in [swsRestraintEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintEndEditError_e.html)

## VBA Syntax

See [CWRestraint::RestraintEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~RestraintEndEdit.html).

## Examples

See the [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html) examples.

## Remarks

You must call [ICWRestraint::RestraintBeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintBeginEdit.html) to start editing a restraint. To end editing a restraint, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
