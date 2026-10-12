---
title: "ContactName Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "ContactName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactName.html"
---

# ContactName Property (ICWContactComponent)

Gets the name of the contact.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ContactName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.String

value = instance.ContactName
```

### C#

```csharp
System.string ContactName {get;}
```

### C++/CLI

```cpp
property System.String^ ContactName {
   System.String^ get();
}
```

### Property Value

Name of contact

## VBA Syntax

See [CWContactComponent::ContactName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~ContactName.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactManager::DeleteContactComponent Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactComponent.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
