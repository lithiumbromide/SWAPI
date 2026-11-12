---
title: "IsSuppressed Method (ISwDMComponent)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent"
member: "IsSuppressed"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.html"
---

# IsSuppressed Method (ISwDMComponent)

Gets whether or not the component is suppressed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSuppressed() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent
Dim value As System.Boolean

value = instance.IsSuppressed()
```

### C#

```csharp
System.bool IsSuppressed()
```

### C++/CLI

```cpp
System.bool IsSuppressed();
```

### Return Value

True if component is suppressed, false if not

## VBA Syntax

See [SwDMComponent::IsSuppressed](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent~IsSuppressed.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.html)
[ISwDMComponent Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent_members.html)
[ISwDMComponent::IsHidden Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~IsHidden.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
