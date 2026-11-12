---
title: "UseTimeCurve Property (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "UseTimeCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseTimeCurve.html"
---

# UseTimeCurve Property (ICWConvection)

Obsolete. Superseded by [ICWConvection::UseTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
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

1 to use a time curve, 0 to not

## VBA Syntax

See [CWConvection::UseTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~UseTimeCurve.html).

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)
[ICWConvection::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~GetTimeCurve.html)
[ICWConvection::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
