---
title: "RevisionTableFeature Property (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "RevisionTableFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~RevisionTableFeature.html"
---

# RevisionTableFeature Property (IRevisionTableAnnotation)

Gets the revision table for this revision table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RevisionTableFeature As RevisionTableFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim value As RevisionTableFeature

value = instance.RevisionTableFeature
```

### C#

```csharp
RevisionTableFeature RevisionTableFeature {get;}
```

### C++/CLI

```cpp
property RevisionTableFeature^ RevisionTableFeature {
   RevisionTableFeature^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Revision table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableFeature.html)

## VBA Syntax

See [RevisionTableAnnotation::RevisionTableFeature](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~RevisionTableFeature.html).

## Examples

See the [IRevisionTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html) examples.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
