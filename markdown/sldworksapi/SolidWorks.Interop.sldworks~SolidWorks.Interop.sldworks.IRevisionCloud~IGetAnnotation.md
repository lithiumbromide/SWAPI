---
title: "IGetAnnotation Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "IGetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetAnnotation.html"
---

# IGetAnnotation Method (IRevisionCloud)

Gets the annotation object for this revision cloud.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim value As Annotation

value = instance.IGetAnnotation()
```

### C#

```csharp
Annotation IGetAnnotation()
```

### C++/CLI

```cpp
Annotation^ IGetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)
[IRevisionCloud::GetAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetAnnotation.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
