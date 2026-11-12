---
title: "CreateEllipse Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateEllipse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateEllipse.html"
---

# CreateEllipse Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipse.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateEllipse( _
   ByVal Center As System.Object, _
   ByVal Major As System.Object, _
   ByVal Minor As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Center As System.Object
Dim Major As System.Object
Dim Minor As System.Object
Dim value As System.Boolean

value = instance.CreateEllipse(Center, Major, Minor)
```

### C#

```csharp
System.bool CreateEllipse(
   System.object Center,
   System.object Major,
   System.object Minor
)
```

### C++/CLI

```cpp
System.bool CreateEllipse(
   System.Object^ Center,
   System.Object^ Major,
   System.Object^ Minor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Major`:
- `Minor`:

## VBA Syntax

See [ModelDoc::CreateEllipse](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateEllipse.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
