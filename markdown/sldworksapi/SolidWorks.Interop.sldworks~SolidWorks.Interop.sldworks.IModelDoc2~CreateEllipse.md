---
title: "CreateEllipse Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateEllipse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipse.html"
---

# CreateEllipse Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipse2.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::CreateEllipse](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateEllipse.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
