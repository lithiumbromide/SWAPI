---
title: "ISplitFaceOnParam2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ISplitFaceOnParam2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam2.html"
---

# ISplitFaceOnParam2 Method (IModeler)

Splits and retrieves the faces on the U or V parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISplitFaceOnParam2() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim value As Face2

value = instance.ISplitFaceOnParam2()
```

### C#

```csharp
Face2 ISplitFaceOnParam2()
```

### C++/CLI

```cpp
Face2^ ISplitFaceOnParam2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of new [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Modeler::ISplitFaceOnParam2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ISplitFaceOnParam2.html).

## Remarks

The split is defined by calling [IModeler::ISplitFaceOnParamCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.html). Then call this method to retrieve the list of new faces allocated.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::SplitFaceOnParam Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
