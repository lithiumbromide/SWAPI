---
title: "MultiSelectByRay Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "MultiSelectByRay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~MultiSelectByRay.html"
---

# MultiSelectByRay Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::MultiSelectByRay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~MultiSelectByRay.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MultiSelectByRay( _
   ByVal DoubleInfoIn As System.Object, _
   ByVal TypeWanted As System.Integer, _
   ByVal Append As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim DoubleInfoIn As System.Object
Dim TypeWanted As System.Integer
Dim Append As System.Boolean
Dim value As System.Boolean

value = instance.MultiSelectByRay(DoubleInfoIn, TypeWanted, Append)
```

### C#

```csharp
System.bool MultiSelectByRay(
   System.object DoubleInfoIn,
   System.int TypeWanted,
   System.bool Append
)
```

### C++/CLI

```cpp
System.bool MultiSelectByRay(
   System.Object^ DoubleInfoIn,
   System.int TypeWanted,
   System.bool Append
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DoubleInfoIn`:
- `TypeWanted`:
- `Append`:

## VBA Syntax

See [ModelDoc::MultiSelectByRay](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~MultiSelectByRay.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
