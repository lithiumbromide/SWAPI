---
title: "IgnoreClearanceForSurfaceContact Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "IgnoreClearanceForSurfaceContact"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IgnoreClearanceForSurfaceContact.html"
---

# IgnoreClearanceForSurfaceContact Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::IgnoreClearanceForSurfaceContact2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IgnoreClearanceForSurfaceContact2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreClearanceForSurfaceContact As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.IgnoreClearanceForSurfaceContact = value

value = instance.IgnoreClearanceForSurfaceContact
```

### C#

```csharp
System.int IgnoreClearanceForSurfaceContact {get; set;}
```

### C++/CLI

```cpp
property System.int IgnoreClearanceForSurfaceContact {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Ignore clearance for surface contact
- 0 = Do not ignore clearance for surface contact

## VBA Syntax

See [CWStaticStudyOptions::IgnoreClearanceForSurfaceContact](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~IgnoreClearanceForSurfaceContact.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

You can override this setting when defining [contact sets](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html).

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::ClearanceUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceUnit.html)
[ICWStaticStudyOptions::ClearanceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceValue.html)
[ICWStaticStudyOptions::IncludeGlobalFriction Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeGlobalFriction.html)
[ICWStaticStudyOptions::NoPenetration Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~NoPenetration.html)
[ICWStaticStudyOptions::FrictionCoefficient Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FrictionCoefficient.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
