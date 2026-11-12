---
title: "GlobalContact2 Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "GlobalContact2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~GlobalContact2.html"
---

# GlobalContact2 Property (ICWContactComponent)

Sets whether to apply a global contact condition.

## Syntax

### Visual Basic (Declaration)

```vb
Property GlobalContact2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Boolean

instance.GlobalContact2 = value

value = instance.GlobalContact2
```

### C#

```csharp
System.bool GlobalContact2 {get; set;}
```

### C++/CLI

```cpp
property System.bool GlobalContact2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to apply a global contact condition, 0 or false to not

## VBA Syntax

See [CWContactComponent::GlobalContact2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~GlobalContact2.html).

## Remarks

To set this property, you can specify either the boolean or the integer.

Set this property to -1 or true to apply a bonded contact to all components in an assembly.

If you set this property to 0 or false, call [ICWContactComponent::InsertEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~InsertEntity.html) to specify contact components.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
