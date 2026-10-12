---
title: "SelectByMark Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SelectByMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SelectByMark.html"
---

# SelectByMark Method (IFeature)

Obsolete. Superseded by [IFeature::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Select2.html).

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
Dim instance As IFeature
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

See [Feature::SelectByMark](ms-its:sldworksapivb6.chm::/sldworks~Feature~SelectByMark.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
