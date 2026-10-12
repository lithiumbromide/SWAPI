---
title: "IsHidden Method (ISwDMComponent)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent"
member: "IsHidden"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~IsHidden.html"
---

# IsHidden Method (ISwDMComponent)

Gets whether or not the component is hidden.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsHidden() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent
Dim value As System.Boolean

value = instance.IsHidden()
```

### C#

```csharp
System.bool IsHidden()
```

### C++/CLI

```cpp
System.bool IsHidden();
```

### Return Value

True if component is hidden, false if not

## VBA Syntax

See [SwDMComponent::IsHidden](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent~IsHidden.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.html)
[ISwDMComponent Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent_members.html)
[ISwDMComponent::IsSuppressed Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
