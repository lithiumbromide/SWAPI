---
title: "SetXform Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "SetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~SetXform.html"
---

# SetXform Method (IBody)

Obsolete. Superseded by [IBody2::ApplyTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ApplyTransform.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetXform( _
   ByVal XformIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim XformIn As System.Object
Dim value As System.Boolean

value = instance.SetXform(XformIn)
```

### C#

```csharp
System.bool SetXform(
   System.object XformIn
)
```

### C++/CLI

```cpp
System.bool SetXform(
   System.Object^ XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`:

## VBA Syntax

See [Body::SetXform](ms-its:sldworksapivb6.chm::/sldworks~Body~SetXform.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
