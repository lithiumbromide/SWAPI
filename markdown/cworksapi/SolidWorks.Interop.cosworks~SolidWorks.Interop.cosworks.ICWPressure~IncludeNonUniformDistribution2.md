---
title: "IncludeNonUniformDistribution2 Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "IncludeNonUniformDistribution2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution2.html"
---

# IncludeNonUniformDistribution2 Property (ICWPressure)

Gets or sets whether to use a nonuniform distribution of pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeNonUniformDistribution2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Boolean

instance.IncludeNonUniformDistribution2 = value

value = instance.IncludeNonUniformDistribution2
```

### C#

```csharp
System.bool IncludeNonUniformDistribution2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeNonUniformDistribution2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to use a nonuniform distribution of pressure, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWPressure::IncludeNonUniformDistribution2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~IncludeNonUniformDistribution2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
