---
title: "AddVerticalDimension Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddVerticalDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddVerticalDimension.html"
---

# AddVerticalDimension Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddVerticalDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddVerticalDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddVerticalDimension( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.AddVerticalDimension(X, Y, Z)
```

### C#

```csharp
System.bool AddVerticalDimension(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool AddVerticalDimension(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::AddVerticalDimension](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddVerticalDimension.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
