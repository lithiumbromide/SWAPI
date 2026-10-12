---
title: "SelectByMark Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SelectByMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SelectByMark.html"
---

# SelectByMark Method (IAnnotation)

Obsolete. Superseded by [IAnnotation::Select3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Select3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByMark( _
   ByVal AppendFlag As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim AppendFlag As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.SelectByMark(AppendFlag, Mark)
```

### C#

```csharp
System.bool SelectByMark(
   System.bool AppendFlag,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool SelectByMark(
   System.bool AppendFlag,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppendFlag`:
- `Mark`:

## VBA Syntax

See [Annotation::SelectByMark](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SelectByMark.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
