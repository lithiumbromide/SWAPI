---
title: "SelectByRay Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectByRay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectByRay.html"
---

# SelectByRay Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectByRay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectByRay.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByRay( _
   ByVal DoubleInfoIn As System.Object, _
   ByVal TypeWanted As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim DoubleInfoIn As System.Object
Dim TypeWanted As System.Integer
Dim value As System.Boolean

value = instance.SelectByRay(DoubleInfoIn, TypeWanted)
```

### C#

```csharp
System.bool SelectByRay(
   System.object DoubleInfoIn,
   System.int TypeWanted
)
```

### C++/CLI

```cpp
System.bool SelectByRay(
   System.Object^ DoubleInfoIn,
   System.int TypeWanted
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DoubleInfoIn`:
- `TypeWanted`:

## VBA Syntax

See [ModelDoc::SelectByRay](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectByRay.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
