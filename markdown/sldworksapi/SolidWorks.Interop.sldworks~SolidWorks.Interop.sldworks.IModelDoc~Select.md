---
title: "Select Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~Select.html"
---

# Select Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::Select](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Select.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Select( _
   ByVal SelID As System.String, _
   ByVal SelParams As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim SelID As System.String
Dim SelParams As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.Select(SelID, SelParams, X, Y, Z)
```

### C#

```csharp
void Select(
   System.string SelID,
   System.string SelParams,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void Select(
   System.String^ SelID,
   System.String^ SelParams,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelID`:
- `SelParams`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::Select](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~Select.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
