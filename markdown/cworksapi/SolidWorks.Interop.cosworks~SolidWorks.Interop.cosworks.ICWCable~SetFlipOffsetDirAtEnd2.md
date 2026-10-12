---
title: "SetFlipOffsetDirAtEnd2 Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "SetFlipOffsetDirAtEnd2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~SetFlipOffsetDirAtEnd2.html"
---

# SetFlipOffsetDirAtEnd2 Method (ICWCable)

Sets the specified flip offset direction at End 2.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFlipOffsetDirAtEnd2( _
   ByVal NFlipDir As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
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

See [CWCable::SetFlipOffsetDirAtEnd2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~SetFlipOffsetDirAtEnd2.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## Remarks

This method is not valid if End 2 is a vertex.

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
