---
title: "GetRepresentationParent Method (ISwDMConfiguration17)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration17"
member: "GetRepresentationParent"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~GetRepresentationParent.html"
---

# GetRepresentationParent Method (ISwDMConfiguration17)

Gets the Physical Product represented by this configuration in [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRepresentationParent() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration17
Dim value As System.String

value = instance.GetRepresentationParent()
```

### C#

```csharp
System.string GetRepresentationParent()
```

### C++/CLI

```cpp
System.String^ GetRepresentationParent();
```

### Return Value

Physical Product name

## VBA Syntax

See [SwDMConfiguration17::GetRepresentationParent](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration17~GetRepresentationParent.html).

## Examples

See the [ISwDMConfiguration17](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.html) examples.

## Remarks

This method is valid only:

- For [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm)

- and -

- If [ISWDMConfiguration17::Get3DExperienceType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~Get3DExperienceType.html) does not return 0.

## See Also

[ISwDMConfiguration17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.html)
[ISwDMConfiguration17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17_members.html)

## Availability

SOLIDWORKS Document Manager API 2020 SP03.1
