---
title: "IGetAnnotation Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "IGetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IGetAnnotation.html"
---

# IGetAnnotation Method (IDisplayDimension)

Gets the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object for this specific annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
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

See [DisplayDimension::IGetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~IGetAnnotation.html).

## Remarks

The [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object is a higher-level object that contains methods that are general to all types of annotations.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAnnotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
