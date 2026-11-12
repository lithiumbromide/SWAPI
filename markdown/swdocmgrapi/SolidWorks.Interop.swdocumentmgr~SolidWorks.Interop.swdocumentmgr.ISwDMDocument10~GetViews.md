---
title: "GetViews Method (ISwDMDocument10)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument10"
member: "GetViews"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetViews.html"
---

# GetViews Method (ISwDMDocument10)

Gets the views in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViews() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument10
Dim value As System.Object

value = instance.GetViews()
```

### C#

```csharp
System.object GetViews()
```

### C++/CLI

```cpp
System.Object^ GetViews();
```

### Return Value

Array of [views](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMView.html)

## VBA Syntax

See [SwDMDocument10::GetViews](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument10~GetViews.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2008 and later.

## See Also

[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.html)
[ISwDMDocument10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
