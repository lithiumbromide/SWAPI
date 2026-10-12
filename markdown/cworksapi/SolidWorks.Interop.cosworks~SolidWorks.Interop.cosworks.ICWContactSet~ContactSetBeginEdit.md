---
title: "ContactSetBeginEdit Method (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ContactSetBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetBeginEdit.html"
---

# ContactSetBeginEdit Method (ICWContactSet)

Starts editing this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ContactSetBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet

instance.ContactSetBeginEdit()
```

### C#

```csharp
void ContactSetBeginEdit()
```

### C++/CLI

```cpp
void ContactSetBeginEdit();
```

## VBA Syntax

See [CWContactSet::ContactSetBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ContactSetBeginEdit.html).

## Remarks

To start editing a contact set, call this method. You must call [ICWContactSet::ContactSetEndEit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~ContactSetEndEdit.html) to end editing that contact set. Changes are not applied unless you call both methods.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)

## Availability

SolidWork Simulation API 2008 SP1.0
