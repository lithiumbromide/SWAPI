---
title: "Select Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select.html"
---

# Select Method (IFeature)

Obsolete. Superseded by [IFeature::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Select2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.Select(AppendFlag)
```

### C#

```csharp
System.bool Select(
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppendFlag`:

## VBA Syntax

See [Feature::Select](ms-its:sldworksapivb6.chm::/sldworks~Feature~Select.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
