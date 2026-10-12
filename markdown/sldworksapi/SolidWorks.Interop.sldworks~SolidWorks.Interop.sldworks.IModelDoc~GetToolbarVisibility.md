---
title: "GetToolbarVisibility Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetToolbarVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetToolbarVisibility.html"
---

# GetToolbarVisibility Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetToolbarVisibility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetToolbarVisibility.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToolbarVisibility( _
   ByVal Toolbar As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Toolbar As System.Integer
Dim value As System.Boolean

value = instance.GetToolbarVisibility(Toolbar)
```

### C#

```csharp
System.bool GetToolbarVisibility(
   System.int Toolbar
)
```

### C++/CLI

```cpp
System.bool GetToolbarVisibility(
   System.int Toolbar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Toolbar`:

## VBA Syntax

See [ModelDoc::GetToolbarVisibility](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetToolbarVisibility.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
