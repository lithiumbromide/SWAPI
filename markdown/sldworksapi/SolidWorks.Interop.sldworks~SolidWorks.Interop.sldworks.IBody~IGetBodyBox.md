---
title: "IGetBodyBox Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IGetBodyBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IGetBodyBox.html"
---

# IGetBodyBox Method (IBody)

Obsolete. Superseded by [IBody2::IGetBodyBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetBodyBox.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetBodyBox( _
   ByRef BoxCorners As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim BoxCorners As System.Double

instance.IGetBodyBox(BoxCorners)
```

### C#

```csharp
void IGetBodyBox(
   ref System.double BoxCorners
)
```

### C++/CLI

```cpp
void IGetBodyBox(
   System.double% BoxCorners
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxCorners`:

## VBA Syntax

See [Body::IGetBodyBox](ms-its:sldworksapivb6.chm::/sldworks~Body~IGetBodyBox.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
