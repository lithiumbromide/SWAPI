---
title: "ContactComponentBeginEdit Method (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "ContactComponentBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactComponentBeginEdit.html"
---

# ContactComponentBeginEdit Method (ICWContactComponent)

Start editing of this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ContactComponentBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent

instance.ContactComponentBeginEdit()
```

### C#

```csharp
void ContactComponentBeginEdit()
```

### C++/CLI

```cpp
void ContactComponentBeginEdit();
```

## VBA Syntax

See [CWContactComponent::ContactComponentBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~ContactComponentBeginEdit.html).

## Remarks

To start editing a contact, you must call this method. You must call [ICWContactComponent::ContactComponentEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactComponent~ContactComponentEndEdit.html) to end editing that contact. Changes are not applied unless you call both methods.

[Contact sets](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html) override both global and component contacts. Component contacts override global contacts.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
