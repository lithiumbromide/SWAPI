---
title: "ISetXform Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ISetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ISetXform.html"
---

# ISetXform Method (IBody)

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
Dim instance As IBody
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

See [Body::ISetXform](ms-its:sldworksapivb6.chm::/sldworks~Body~ISetXform.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
