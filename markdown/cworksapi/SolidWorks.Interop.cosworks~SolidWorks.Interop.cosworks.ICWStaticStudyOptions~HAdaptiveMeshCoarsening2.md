---
title: "HAdaptiveMeshCoarsening2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "HAdaptiveMeshCoarsening2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMeshCoarsening2.html"
---

# HAdaptiveMeshCoarsening2 Property (ICWStaticStudyOptions)

Gets or sets whether to allow h-adaptive mesh coarsening.

## Syntax

### Visual Basic (Declaration)

```vb
Property HAdaptiveMeshCoarsening2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.HAdaptiveMeshCoarsening2 = value

value = instance.HAdaptiveMeshCoarsening2
```

### C#

```csharp
System.bool HAdaptiveMeshCoarsening2 {get; set;}
```

### C++/CLI

```cpp
property System.bool HAdaptiveMeshCoarsening2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to allow mesh coarsening in areas that do not need a highly defined mesh, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::HAdaptiveMeshCoarsening2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~HAdaptiveMeshCoarsening2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
