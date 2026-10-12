---
title: "InsertCurveFile Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertCurveFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertCurveFile.html"
---

# InsertCurveFile Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertCurveFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFile.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCurveFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertCurveFile(FileName)
```

### C#

```csharp
System.bool InsertCurveFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertCurveFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [ModelDoc::InsertCurveFile](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertCurveFile.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
