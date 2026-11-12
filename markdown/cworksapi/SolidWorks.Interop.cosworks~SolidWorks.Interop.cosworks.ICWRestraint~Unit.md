---
title: "Unit Property (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~Unit.html"
---

# Unit Property (ICWRestraint)

Gets or sets the units of translation or rotation for this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- Units of translation as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- Units of angular rotation as defined in [swsRotationUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRotationUnit_e.html)

## VBA Syntax

See [CWRestraint::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~Unit.html).

## Examples

See the [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html) examples.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::GetRotationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues.html)
[ICWRestraint::GetTranslationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues.html)
[ICWRestraint::SetRotationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetRotationComponentsValues.html)
[ICWRestraint::SetTranslationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTranslationComponentsValues.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
