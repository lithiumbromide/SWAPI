---
title: "Get3DExperienceType Method (ISwDMDocument26)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument26"
member: "Get3DExperienceType"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26~Get3DExperienceType.html"
---

# Get3DExperienceType Method (ISwDMDocument26)

Gets the type of 3DEXPERIENCE application that created this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DExperienceType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument26
Dim value As System.Integer

value = instance.Get3DExperienceType()
```

### C#

```csharp
System.int Get3DExperienceType()
```

### C++/CLI

```cpp
System.int Get3DExperienceType();
```

### Return Value

3DEXPERIENCE model type as defined by [swDm3DExperienceModelType_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDm3DExperienceModelType_e.html)

## VBA Syntax

See [SwDMDocument26::Get3DExperienceType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument26~Get3DExperienceType.html).

## See Also

[ISwDMDocument26 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26.html)
[ISwDMDocument26 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26_members.html)

## Availability

SOLIDWORKS Document Manager API 2021 SP0
