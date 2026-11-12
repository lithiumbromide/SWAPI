---
title: "Finalize Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "Finalize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~Finalize.html"
---

# Finalize Method (IRevisionCloud)

Finalizes the creation of this revision cloud annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function Finalize() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim value As System.Boolean

value = instance.Finalize()
```

### C#

```csharp
System.bool Finalize()
```

### C++/CLI

```cpp
System.bool Finalize();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this revision cloud was successfully finalized, false if not

## VBA Syntax

See [RevisionCloud::Finalize](ms-its:sldworksapivb6.chm::/sldworks~RevisionCloud~Finalize.html).

## Examples

See [IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html) examples.

## Remarks

You must call this method after all revision cloud path points have been added to the annotation. After finalizing the revision cloud annotation, no new points can be added to the cloud path. The positions of existing cloud path points can be modified at any time.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
