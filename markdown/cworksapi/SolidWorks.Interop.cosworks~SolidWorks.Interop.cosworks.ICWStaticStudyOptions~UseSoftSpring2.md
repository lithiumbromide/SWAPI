---
title: "UseSoftSpring2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "UseSoftSpring2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseSoftSpring2.html"
---

# UseSoftSpring2 Property (ICWStaticStudyOptions)

Gets or sets whether to solve using a soft spring to stabilize the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSoftSpring2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.UseSoftSpring2 = value

value = instance.UseSoftSpring2
```

### C#

```csharp
System.bool UseSoftSpring2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseSoftSpring2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use soft spring to stabilize model
- 0 or false = Do not use soft spring

(see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::UseSoftSpring2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~UseSoftSpring2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
