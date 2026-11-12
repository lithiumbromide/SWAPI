---
title: "DefaultUnitSystem Property (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "DefaultUnitSystem"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DefaultUnitSystem.html"
---

# DefaultUnitSystem Property (ICWModelDoc)

Gets and sets the default unit system for this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultUnitSystem As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim value As System.Integer

instance.DefaultUnitSystem = value

value = instance.DefaultUnitSystem
```

### C#

```csharp
System.int DefaultUnitSystem {get; set;}
```

### C++/CLI

```cpp
property System.int DefaultUnitSystem {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWModelDoc::DefaultUnitSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~DefaultUnitSystem.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
