---
title: "SetJointTypeAtEnd2 Method (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "SetJointTypeAtEnd2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~SetJointTypeAtEnd2.html"
---

# SetJointTypeAtEnd2 Method (ICWLinkageRod)

Sets the joint type of End 2 of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetJointTypeAtEnd2( _
   ByVal NJointType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod
Dim NJointType As System.Integer

instance.SetJointTypeAtEnd2(NJointType)
```

### C#

```csharp
void SetJointTypeAtEnd2(
   System.int NJointType
)
```

### C++/CLI

```cpp
void SetJointTypeAtEnd2(
   System.int NJointType
)
```

### Parameters

- `NJointType`: Joint type as defined by [swsJointType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsJointType_e.html)

## VBA Syntax

See [CWLinkageRod::SetJointTypeAtEnd2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~SetJointTypeAtEnd2.html).

## Examples

See the [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html) examples

## Remarks

If End 2 is a vertex, then you cannot set NJointType with swsJointType_e.swsPivot.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
