---
title: "GetTableAnnotationCount Method (IRevisionTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableFeature"
member: "GetTableAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotationCount.html"
---

# GetTableAnnotationCount Method (IRevisionTableFeature)

Gets the number of revision table annotations for this revision table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableFeature
Dim value As System.Integer

value = instance.GetTableAnnotationCount()
```

### C#

```csharp
System.int GetTableAnnotationCount()
```

### C++/CLI

```cpp
System.int GetTableAnnotationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of revision table annotations

## VBA Syntax

See [RevisionTableFeature::GetTableAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableFeature~GetTableAnnotationCount.html).

## Examples

See the [IRevisionTableFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.html) examples.

## Remarks

Call this method before calling [IRevisionTableFeature::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableFeature~IGetTableAnnotations.html) to get the size of the array for that method.

## See Also

[IRevisionTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature.html)
[IRevisionTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature_members.html)
[IRevisionTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
