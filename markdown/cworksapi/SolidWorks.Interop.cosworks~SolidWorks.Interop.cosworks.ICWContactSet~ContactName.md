---
title: "ContactName Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ContactName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactName.html"
---

# ContactName Property (ICWContactSet)

Gets the name of this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ContactName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
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

Name of this contact set

## VBA Syntax

See [CWContactSet::ContactName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ContactName.html).

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactManager::DeleteContactSet Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactSet.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
