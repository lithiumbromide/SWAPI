---
title: "CurrentRevision Property (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "CurrentRevision"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html"
---

# CurrentRevision Property (IRevisionTableAnnotation)

Gets the latest revision of this revision table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentRevision As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim value As System.String

value = instance.CurrentRevision
```

### C#

```csharp
System.string CurrentRevision {get;}
```

### C++/CLI

```cpp
property System.String^ CurrentRevision {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Latest revision

## VBA Syntax

See [RevisionTableAnnotation::CurrentRevision](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~CurrentRevision.html).

## Examples

See the [IRevisionTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html) examples.

## Remarks

Use [IRevisionTableAnnotation::AddRevision](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~AddRevision.html) to add a revision and get its revision ID.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::DeleteRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision.html)
[IRevisionTableAnnotation::GetIdForRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber.html)
[IRevisionTableAnnotation::GetRevisionForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId.html)
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
