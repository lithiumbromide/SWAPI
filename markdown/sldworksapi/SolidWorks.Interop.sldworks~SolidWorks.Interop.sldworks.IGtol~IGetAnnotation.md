---
title: "IGetAnnotation Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetAnnotation.html"
---

# IGetAnnotation Method (IGtol)

Gets the annotation for this specific GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

Pointer to the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object

## VBA Syntax

See [Gtol::IGetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~Gtol~IGetAnnotation.html).

## Remarks

The IAnnotation object is a higher-level object that contains methods that are available to all types of annotations.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAnnotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
