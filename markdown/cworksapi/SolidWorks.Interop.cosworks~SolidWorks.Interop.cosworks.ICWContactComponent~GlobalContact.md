---
title: "GlobalContact Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "GlobalContact"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~GlobalContact.html"
---

# GlobalContact Property (ICWContactComponent)

Obsolete. Superseded by [ICWContactComponent::GlobalContact2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~GlobalContact2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property GlobalContact As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

instance.GlobalContact = value

value = instance.GlobalContact
```

### C#

```csharp
System.int GlobalContact {get; set;}
```

### C++/CLI

```cpp
property System.int GlobalContact {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to apply a global contact condition, 0 to not

## VBA Syntax

See [CWContactComponent::GlobalContact](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~GlobalContact.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## Remarks

Set this property to 1 to apply a bonded contact to all components in an assembly.

If you set this property to 0, call [ICWContactComponent::InsertEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~InsertEntity.html) to specify contact components.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
