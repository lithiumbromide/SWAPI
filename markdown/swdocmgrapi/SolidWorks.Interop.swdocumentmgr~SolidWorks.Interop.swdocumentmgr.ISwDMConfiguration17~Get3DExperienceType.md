---
title: "Get3DExperienceType Method (ISwDMConfiguration17)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration17"
member: "Get3DExperienceType"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~Get3DExperienceType.html"
---

# Get3DExperienceType Method (ISwDMConfiguration17)

Gets how [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm) views this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DExperienceType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration17
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

Treatment of this configuration as defined by [swDm3DExperienceCfgType_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDm3DExperienceCfgType_e.html)

## VBA Syntax

See [SwDMConfiguration17::Get3DExperienceType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration17~Get3DExperienceType.html).

## Examples

See the [ISwDMConfiguration17](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.html) examples.

## See Also

[ISwDMConfiguration17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.html)
[ISwDMConfiguration17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17_members.html)
[ISwDMConfiguration17::GetRepresentationParent Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~GetRepresentationParent.html)

## Availability

SOLIDWORKS Document Manager API 2020 SP03.1
