---
title: "Select2 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select2.html"
---

# Select2 Method (IAnnotation)

Obsolete. Superseded by [IAnnotation::Select3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Select3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.Select2(Append, Mark)
```

### C#

```csharp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`:
- `Mark`:

## VBA Syntax

See [Annotation::Select2](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Select2.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
