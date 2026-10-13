---
title: "ContactSetEndEdit Method (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ContactSetEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetEndEdit.html"
---

# ContactSetEndEdit Method (ICWContactSet)

Ends editing this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Function ContactSetEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

value = instance.ContactSetEndEdit()
```

### C#

```csharp
System.int ContactSetEndEdit()
```

### C++/CLI

```cpp
System.int ContactSetEndEdit();
```

### Return Value

Error as defined in [swsContactSetEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetEndEditError_e.html)

## VBA Syntax

See [CWContactSet::ContactSetEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ContactSetEndEdit.html).

## Remarks

To start editing a contact set, call [ICWContactSet::ContactSetBeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetBeginEdit.html). You must call this method to end editing that contact set. Changes are not applied unless you call both methods.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
