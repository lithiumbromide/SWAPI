---
title: "ISetXform Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ISetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISetXform.html"
---

# ISetXform Method (IBody2)

Obsolete. Superseded by [IBody2::ApplyTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ApplyTransform.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetXform( _
   ByRef XformIn As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim XformIn As System.Double
Dim value As System.Boolean

value = instance.ISetXform(XformIn)
```

### C#

```csharp
System.bool ISetXform(
   ref System.double XformIn
)
```

### C++/CLI

```cpp
System.bool ISetXform(
   System.double% XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`:

## VBA Syntax

See [Body2::ISetXform](ms-its:sldworksapivb6.chm::/sldworks~Body2~ISetXform.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
