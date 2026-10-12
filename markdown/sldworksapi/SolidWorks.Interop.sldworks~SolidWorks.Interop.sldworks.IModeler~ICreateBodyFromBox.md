---
title: "ICreateBodyFromBox Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodyFromBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox.html"
---

# ICreateBodyFromBox Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateBodyFromBox2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromBox2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromBox( _
   ByRef BoxDimArray As System.Double _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim BoxDimArray As System.Double
Dim value As Body

value = instance.ICreateBodyFromBox(BoxDimArray)
```

### C#

```csharp
Body ICreateBodyFromBox(
   ref System.double BoxDimArray
)
```

### C++/CLI

```cpp
Body^ ICreateBodyFromBox(
   System.double% BoxDimArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxDimArray`:

## VBA Syntax

See [Modeler::ICreateBodyFromBox](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodyFromBox.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
