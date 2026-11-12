---
title: "SetTitle2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetTitle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetTitle2.html"
---

# SetTitle2 Method (IModelDoc2)

Sets the title of a new document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTitle2( _
   ByVal NewTitle As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim NewTitle As System.String
Dim value As System.Boolean

value = instance.SetTitle2(NewTitle)
```

### C#

```csharp
System.bool SetTitle2(
   System.string NewTitle
)
```

### C++/CLI

```cpp
System.bool SetTitle2(
   System.String^ NewTitle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewTitle`: Name to give to the document window

### Return Value

True if successfully renamed, false otherwise

## VBA Syntax

See [ModelDoc2::SetTitle2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetTitle2.html).

## Remarks

This title appears in the active window's title bar.

This method:

- Does not save this model document to disk; instead, it renames the document window.
- Is only valid when for a new document that has not yet been saved.
- Does not change the title of a document that has already been saved and exists on disk. If you want to rename an existing document, use ModelDoc2::SaveAs.

To retrieve the title of a document, use [IModelDoc2::GetTitle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetTitle.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
