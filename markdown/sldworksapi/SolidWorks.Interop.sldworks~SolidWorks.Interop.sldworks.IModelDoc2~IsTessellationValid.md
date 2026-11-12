---
title: "IsTessellationValid Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IsTessellationValid"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsTessellationValid.html"
---

# IsTessellationValid Method (IModelDoc2)

Gets whether the current set of facets is valid.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsTessellationValid() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.IsTessellationValid()
```

### C#

```csharp
System.bool IsTessellationValid()
```

### C++/CLI

```cpp
System.bool IsTessellationValid();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the facet data is valid; false if not

## VBA Syntax

See [ModelDoc2::IsTessellationValid](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IsTessellationValid.html).

## Remarks

This method captures operations that invalidate the current set of facets, but does not send a RegenNotify event. For example, if the user changes the rendering tolerance, the RegenNotify event is not sent. However, the current set of facets would be invalid. This action triggers a RepaintNotify from which you can call this method before attempting to use your current set of facet data.

If false is returned, then valid facet information would not be available until SOLIDWORKS completes a repaint operation (RepaintPostNotify). In other words, SOLIDWORKS does not have any valid facet information at this time, and any facet data obtained in earlier calls is invalid.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
