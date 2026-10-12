---
title: "RestraintType Property (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "RestraintType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html"
---

# RestraintType Property (ICWRestraint)

Gets or sets the type of this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Property RestraintType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim value As System.Integer

instance.RestraintType = value

value = instance.RestraintType
```

### C#

```csharp
System.int RestraintType {get; set;}
```

### C++/CLI

```cpp
property System.int RestraintType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of restraint as defined in [swsRestraintType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintType_e.html)

## VBA Syntax

See [CWRestraint::RestraintType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~RestraintType.html).

## Examples

See the [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html) examples.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReferenceGeometry.html)
[ICWRestraint::SetTranslationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTranslationComponentsValues.html)
[ICWRestraint::SetRotationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetRotationComponentsValues.html)
[ICWRestraint::GetTranslationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues.html)
[ICWRestraint::GetRotationComponentsValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues.html)
[ICWRestraint::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTimeCurve.html)
[ICWRestraint::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
