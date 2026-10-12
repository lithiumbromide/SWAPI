---
title: "ContactComponentEndEdit Method (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "ContactComponentEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactComponentEndEdit.html"
---

# ContactComponentEndEdit Method (ICWContactComponent)

Ends editing of this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Function ContactComponentEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

value = instance.ContactComponentEndEdit()
```

### C#

```csharp
System.int ContactComponentEndEdit()
```

### C++/CLI

```cpp
System.int ContactComponentEndEdit();
```

### Return Value

Error as defined in [swsContactComponentEndEditError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactComponentEndEditError_e.html)

## VBA Syntax

See [CWContactComponent::ContactComponentEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~ContactComponentEndEdit.html).

## Remarks

To start editing a contact, call [ICWContactComponent::ContactComponentBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactComponent~ContactComponentBeginEdit.html). You must call this method to end editing that contact. Changes are not applied unless you call both methods.

[Contact sets](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html) override both global and component contacts. Component contacts override global contacts.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
