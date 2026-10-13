---
title: "AngleMadeWithViewHorizontal Property (IAnnotationView)"
project: "SOLIDWORKS API Help"
interface: "IAnnotationView"
member: "AngleMadeWithViewHorizontal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AngleMadeWithViewHorizontal.html"
---

# AngleMadeWithViewHorizontal Property (IAnnotationView)

Gets the angle used to make the annotation view horizontal.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AngleMadeWithViewHorizontal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotationView
Dim value As System.Double

value = instance.AngleMadeWithViewHorizontal
```

### C#

```csharp
System.double AngleMadeWithViewHorizontal {get;}
```

### C++/CLI

```cpp
property System.double AngleMadeWithViewHorizontal {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle

## VBA Syntax

See [AnnotationView::AngleMadeWithViewHorizontal](ms-its:sldworksapivb6.chm::/sldworks~AnnotationView~AngleMadeWithViewHorizontal.html).

## See Also

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
