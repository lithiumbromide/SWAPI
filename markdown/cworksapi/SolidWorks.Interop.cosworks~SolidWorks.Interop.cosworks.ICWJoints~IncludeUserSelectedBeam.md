---
title: "IncludeUserSelectedBeam Property (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "IncludeUserSelectedBeam"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeUserSelectedBeam.html"
---

# IncludeUserSelectedBeam Property (ICWJoints)

Gets or sets whether to include only the user-selected beams.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeUserSelectedBeam As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Boolean

instance.IncludeUserSelectedBeam = value

value = instance.IncludeUserSelectedBeam
```

### C#

```csharp
System.bool IncludeUserSelectedBeam {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeUserSelectedBeam {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include only the user-selected beams, false to not

## VBA Syntax

See [CWJoints::IncludeUserSelectedBeam](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~IncludeUserSelectedBeam.html).

## Remarks

To include only the user-selected beams:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Specify to include only the user-selected beams by calling this method.
3. [Save your modification.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html)
4. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
5. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)
[ICWJoints::IncludeAllSelectedBeam Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeAllSelectedBeam.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
