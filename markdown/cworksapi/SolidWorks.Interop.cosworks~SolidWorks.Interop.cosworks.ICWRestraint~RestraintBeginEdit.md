---
title: "RestraintBeginEdit Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "RestraintBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintBeginEdit.html"
---

# RestraintBeginEdit Method (ICWRestraint)

Starts editing a restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RestraintBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint

instance.RestraintBeginEdit()
```

### C#

```csharp
void RestraintBeginEdit()
```

### C++/CLI

```cpp
void RestraintBeginEdit();
```

## VBA Syntax

See [CWRestraint::RestraintBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~RestraintBeginEdit.html).

## Examples

See the [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html) examples.

## Remarks

To start editing a restraint, you must call this method. You must call [ICWRestraint::RestraintEndEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintEndEdit.html) to end editing a restraint. Changes are not applied unless you call both methods.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
