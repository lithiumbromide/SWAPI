---
title: "GetTableAnnotations Method (IRevisionTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableFeature"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IRevisionTableFeature)

Gets the revision table annotations for this revision table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableFeature
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the [revision table annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation.html)

## VBA Syntax

See [RevisionTableFeature::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableFeature~GetTableAnnotations.html).

## See Also

[IRevisionTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.html)
[IRevisionTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature_members.html)
[IRevisionTableFeature::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotationCount.html)
[IRevisionTableFeature::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
