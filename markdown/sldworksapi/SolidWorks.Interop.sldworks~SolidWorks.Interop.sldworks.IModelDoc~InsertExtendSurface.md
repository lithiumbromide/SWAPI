---
title: "InsertExtendSurface Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertExtendSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertExtendSurface.html"
---

# InsertExtendSurface Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertExtendSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertExtendSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertExtendSurface( _
   ByVal ExtendLinear As System.Boolean, _
   ByVal EndCondition As System.Integer, _
   ByVal Distance As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ExtendLinear As System.Boolean
Dim EndCondition As System.Integer
Dim Distance As System.Double

instance.InsertExtendSurface(ExtendLinear, EndCondition, Distance)
```

### C#

```csharp
void InsertExtendSurface(
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Distance
)
```

### C++/CLI

```cpp
void InsertExtendSurface(
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExtendLinear`:
- `EndCondition`:
- `Distance`:

## VBA Syntax

See [ModelDoc::InsertExtendSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertExtendSurface.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
