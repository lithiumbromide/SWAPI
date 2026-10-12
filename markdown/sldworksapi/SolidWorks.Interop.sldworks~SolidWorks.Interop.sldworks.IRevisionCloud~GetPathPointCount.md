---
title: "GetPathPointCount Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "GetPathPointCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointCount.html"
---

# GetPathPointCount Method (IRevisionCloud)

Gets the number of points on the path of this revision cloud annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathPointCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim value As System.Integer

value = instance.GetPathPointCount()
```

### C#

```csharp
System.int GetPathPointCount()
```

### C++/CLI

```cpp
System.int GetPathPointCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of points on the path of this revision cloud annotation

## VBA Syntax

See [RevisionCloud::GetPathPointCount](ms-its:sldworksapivb6.chm::/sldworks~RevisionCloud~GetPathPointCount.html).

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)
[IRevisionCloud::GetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointAtIndex.html)
[IRevisionCloud::IGetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetPathPointAtIndex.html)
[IRevisionCloud::SetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
