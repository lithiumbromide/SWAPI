---
title: "SetFlipOffsetDirAtEnd2 Method (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "SetFlipOffsetDirAtEnd2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~SetFlipOffsetDirAtEnd2.html"
---

# SetFlipOffsetDirAtEnd2 Method (ICWLinkageRod)

Sets the flip direction of the offset at End 2 of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFlipOffsetDirAtEnd2( _
   ByVal NFlipDir As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod
Dim NFlipDir As System.Integer

instance.SetFlipOffsetDirAtEnd2(NFlipDir)
```

### C#

```csharp
void SetFlipOffsetDirAtEnd2(
   System.int NFlipDir
)
```

### C++/CLI

```cpp
void SetFlipOffsetDirAtEnd2(
   System.int NFlipDir
)
```

### Parameters

- `NFlipDir`: Offset flip direction as defined by [swsFlipOffsetDir_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFlipOffsetDir_e.html)

## VBA Syntax

See [CWLinkageRod::SetFlipOffsetDirAtEnd2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~SetFlipOffsetDirAtEnd2.html).

## Remarks

This method is not valid if End 2 is a vertex.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
