---
title: "Transform Property (ISwDMComponent)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent"
member: "Transform"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~Transform.html"
---

# Transform Property (ISwDMComponent)

Gets the transform for this component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Transform As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent
Dim value As System.Object

value = instance.Transform
```

### C#

```csharp
System.object Transform {get;}
```

### C++/CLI

```cpp
property System.Object^ Transform {
   System.Object^ get();
}
```

### Property Value

Array containing 16 elements that define the transform:

- First 12 elements are in a 4x3 matrix:
  |a, b, c|
  |d, e, f|
  |g, h, i|
  |j, k, l|
- Next 3 elements define translation:
  |m, n, o|
- Last 1 element is the scaling value:
  |n|

Be aware that the SOLIDWORKS API method IComponent2::Transform2 returns an IMathTransform object, whose 16 elements are ordered differently. See the SOLIDWORKS API Help for details about IComponent2::Transform2 and IMathTransform.

## VBA Syntax

See [SwDMComponent::Transform](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent~Transform.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.html)
[ISwDMComponent Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
