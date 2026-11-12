---
title: "NoPenetration2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "NoPenetration2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~NoPenetration2.html"
---

# NoPenetration2 Property (ICWStaticStudyOptions)

Gets or sets whether to improve accuracy for no penetration contacting surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Property NoPenetration2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.NoPenetration2 = value

value = instance.NoPenetration2
```

### C#

```csharp
System.bool NoPenetration2 {get; set;}
```

### C++/CLI

```cpp
property System.bool NoPenetration2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to improve accuracy for no penetration contacting surfaces, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::NoPenetration2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~NoPenetration2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
