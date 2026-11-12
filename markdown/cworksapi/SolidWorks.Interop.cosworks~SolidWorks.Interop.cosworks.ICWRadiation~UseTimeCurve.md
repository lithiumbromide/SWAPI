---
title: "UseTimeCurve Property (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "UseTimeCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTimeCurve.html"
---

# UseTimeCurve Property (ICWRadiation)

Obsolete. Superseded by [ICWRadiation::UseTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim value As System.Integer

instance.UseTimeCurve = value

value = instance.UseTimeCurve
```

### C#

```csharp
System.int UseTimeCurve {get; set;}
```

### C++/CLI

```cpp
property System.int UseTimeCurve {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use time curve, 0 to not

## VBA Syntax

See [CWRadiation::UseTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~UseTimeCurve.html).

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiation::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~GetTimeCurve.html)
[ICWRadiation::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
