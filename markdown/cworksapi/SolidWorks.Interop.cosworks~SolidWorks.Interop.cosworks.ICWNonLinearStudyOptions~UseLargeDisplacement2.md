---
title: "UseLargeDisplacement2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "UseLargeDisplacement2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeDisplacement2.html"
---

# UseLargeDisplacement2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to use large displacement formulation.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseLargeDisplacement2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.UseLargeDisplacement2 = value

value = instance.UseLargeDisplacement2
```

### C#

```csharp
System.bool UseLargeDisplacement2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseLargeDisplacement2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use large displacement formulation
- 0 or false = Do not use large displacement formulation

(see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::UseLargeDisplacement2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~UseLargeDisplacement2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
