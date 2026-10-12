---
title: "UseInPlaneEffect2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "UseInPlaneEffect2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInPlaneEffect2.html"
---

# UseInPlaneEffect2 Property (ICWStaticStudyOptions)

Gets or sets whether to solve using inplane effect.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseInPlaneEffect2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.UseInPlaneEffect2 = value

value = instance.UseInPlaneEffect2
```

### C#

```csharp
System.bool UseInPlaneEffect2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseInPlaneEffect2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use inplane effect
- 0 or false = Do not use inplane effect

(see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::UseInPlaneEffect2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~UseInPlaneEffect2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
