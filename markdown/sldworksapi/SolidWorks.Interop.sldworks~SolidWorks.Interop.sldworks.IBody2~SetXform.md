---
title: "SetXform Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetXform.html"
---

# SetXform Method (IBody2)

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
Dim instance As IBody2
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

See [Body2::SetXform](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetXform.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
