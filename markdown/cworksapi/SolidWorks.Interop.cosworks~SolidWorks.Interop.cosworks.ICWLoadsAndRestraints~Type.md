---
title: "Type Property (ICWLoadsAndRestraints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraints"
member: "Type"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints~Type.html"
---

# Type Property (ICWLoadsAndRestraints)

Gets the type of the load or restraint.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraints
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

### Property Value

Type of load and restraint as defined in [swsLoadsAndRestraintsType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLoadsAndRestraintsType_e.html)

## VBA Syntax

See [CWLoadsAndRestraints::Type](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraints~Type.html).

## Examples

See the [ICWLoadsAndRestraints](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html) examples.

## See Also

[ICWLoadsAndRestraints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html)
[ICWLoadsAndRestraints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints_members.html)

## Availability

SolidWork Simulation API 2008 SP1.0
