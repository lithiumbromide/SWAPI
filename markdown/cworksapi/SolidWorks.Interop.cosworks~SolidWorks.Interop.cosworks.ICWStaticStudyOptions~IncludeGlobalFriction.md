---
title: "IncludeGlobalFriction Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "IncludeGlobalFriction"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeGlobalFriction.html"
---

# IncludeGlobalFriction Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::IncludeGlobalFriction2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeGlobalFriction2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeGlobalFriction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.IncludeGlobalFriction = value

value = instance.IncludeGlobalFriction
```

### C#

```csharp
System.int IncludeGlobalFriction {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeGlobalFriction {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to include global friction, 0 to not

## VBA Syntax

See [CWStaticStudyOptions::IncludeGlobalFriction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~IncludeGlobalFriction.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

After setting this property to 1, set the friction coefficient using [ICWStaticStudyOptions::FrictionCoefficient](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FrictionCoefficient.html).

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::IgnoreClearanceForSurfaceContact Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IgnoreClearanceForSurfaceContact.html)
[ICWStaticStudyOptions::NoPenetration Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~NoPenetration.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
