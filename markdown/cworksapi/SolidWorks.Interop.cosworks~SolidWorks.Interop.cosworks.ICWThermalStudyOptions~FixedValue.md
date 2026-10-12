---
title: "FixedValue Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "FixedValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~FixedValue.html"
---

# FixedValue Property (ICWThermalStudyOptions)

Gets or sets the fixed value of the relaxation factor.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Double

instance.FixedValue = value

value = instance.FixedValue
```

### C#

```csharp
System.double FixedValue {get; set;}
```

### C++/CLI

```cpp
property System.double FixedValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Fixed under-relaxation factor

## VBA Syntax

See [CWThermalStudyOptions::FixedValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~FixedValue.html).

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
