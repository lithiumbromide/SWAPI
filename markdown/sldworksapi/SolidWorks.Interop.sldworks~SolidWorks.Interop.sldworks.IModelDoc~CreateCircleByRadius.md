---
title: "CreateCircleByRadius Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCircleByRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircleByRadius.html"
---

# CreateCircleByRadius Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCircleByRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircleByRadius.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCircleByRadius( _
   ByVal P1 As System.Object, _
   ByVal Radius As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim P1 As System.Object
Dim Radius As System.Double
Dim value As System.Boolean

value = instance.CreateCircleByRadius(P1, Radius)
```

### C#

```csharp
System.bool CreateCircleByRadius(
   System.object P1,
   System.double Radius
)
```

### C++/CLI

```cpp
System.bool CreateCircleByRadius(
   System.Object^ P1,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `Radius`:

## VBA Syntax

See [ModelDoc::CreateCircleByRadius](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCircleByRadius.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
