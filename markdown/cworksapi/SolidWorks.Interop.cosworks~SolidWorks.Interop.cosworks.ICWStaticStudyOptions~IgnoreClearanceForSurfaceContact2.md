---
title: "IgnoreClearanceForSurfaceContact2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "IgnoreClearanceForSurfaceContact2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IgnoreClearanceForSurfaceContact2.html"
---

# IgnoreClearanceForSurfaceContact2 Property (ICWStaticStudyOptions)

Gets or sets whether to consider contact conditions regardless of the initial distance between user-defined face pairs.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreClearanceForSurfaceContact2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.IgnoreClearanceForSurfaceContact2 = value

value = instance.IgnoreClearanceForSurfaceContact2
```

### C#

```csharp
System.bool IgnoreClearanceForSurfaceContact2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreClearanceForSurfaceContact2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Ignore clearance for surface contact
- 0 or false = Do not ignore clearance for surface contact

(see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::IgnoreClearanceForSurfaceContact2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~IgnoreClearanceForSurfaceContact2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
